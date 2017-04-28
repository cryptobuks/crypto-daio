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
                logger.info('block {} OK'.format(block.height))
                return True

        else:
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
                return

            self.validate_block(block)
            return

        # no block specified so validate all blocks starting from start_height
        blocks = Block.objects.filter(
            height__gte=options['start_height']
        ).order_by(
            'height'
        )

        # paginate to speed the initial load up a bit
        paginator = Paginator(blocks, 1000)

        invalid_blocks = []
        try:
            for page_num in paginator.page_range:
                for block in paginator.page(page_num):
                    try:
                        if not self.validate_block(block):
                            invalid_blocks.append(block.height)
                    except BaseChannelLayer.ChannelFull:
                        logger.warning('Channel Full. Sleeping for a bit')
                        time.sleep(600)
                        self.validate_block(block)
        except KeyboardInterrupt:
            pass
        logger.info('invalid blocks: {}'.format(invalid_blocks))
