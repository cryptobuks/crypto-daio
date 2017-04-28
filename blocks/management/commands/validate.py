import time
from asgiref.base_layer import BaseChannelLayer

from channels import Channel
from django.core.management import BaseCommand
from django.core.paginator import Paginator

from blocks.models import Block
from django.utils import timezone

import logging

from blocks.utils.rpc import get_block_hash

logger = logging.getLogger('daio')

tz = timezone.get_current_timezone()


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '-s',
            '--start-height',
            help='The block height to start the parse from',
            dest='start_height',
            default=0
        )
        parser.add_argument(
            '-b',
            '--block',
            help='The block height to validate',
            dest='block',
        )

    @staticmethod
    def validate_block(block):
        if block.height == 0:
            # genesis block is ok
            return True

        valid, error_message = block.validate()

        if valid:
            invalid_txs = []

            for tx in block.transactions.all():
                if not tx.is_valid:
                    Channel('parse_transaction').send(
                        {
                            'tx_hash': tx.tx_id,
                            'block_hash': block.hash,
                            'tx_index': tx.index
                        }
                    )
                    invalid_txs.append('{}:{}'.format(tx.index, tx.tx_id[:8]))

            if invalid_txs:
                logger.error(
                    'block {} has invalid transactions: {}'.format(
                        block.height,
                        invalid_txs
                    )
                )
                return False

            else:
                return True

        else:
            logger.error('block {} is invalid: {}'.format(block.height, error_message))
            Channel('repair_block').send(
                {
                    'block_hash': block.hash,
                    'error_message': error_message,
                }
            )
            return False

    def handle(self, *args, **options):
        """
        Parse the block chain
        """
        if options['block']:
            # just validate the single block specified
            try:
                block = Block.objects.get(height=options['block'])
            except Block.DoesNotExist:
                logger.error('no block found at {}'.format(options['block']))
                Channel('parse_block').send(
                    {'block_hash': get_block_hash(options['block'])}
                )
                return

            self.validate_block(block)
            return

        # no block specified so validate all blocks starting from start_height
        blocks = Block.objects.filter(
            height__gte=options['start_height']
        ).order_by(
            'height'
        )

        logger.info('validating {} blocks'.format(blocks.count()))
        # paginate to speed the initial load up a bit
        paginator = Paginator(blocks, 1000)

        invalid_blocks = []
        try:
            for page_num in paginator.page_range:
                page_invalid_blocks = []
                for block in paginator.page(page_num):
                    try:
                        if not self.validate_block(block):
                            page_invalid_blocks.append(block.height)
                    except BaseChannelLayer.ChannelFull:
                        logger.warning('Channel Full. Sleeping for a bit')
                        time.sleep(600)
                        self.validate_block(block)

                logger.info(
                    '{} blocks validated with {} invalid blocks found: {}'.format(
                        1000 * page_num,
                        len(page_invalid_blocks),
                        page_invalid_blocks,
                    )
                )

                invalid_blocks += page_invalid_blocks
        except KeyboardInterrupt:
            pass
        logger.info('{} invalid blocks: {}'.format(len(invalid_blocks), invalid_blocks))
