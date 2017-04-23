import logging

from channels import Channel

from blocks.models import Transaction, Block
from blocks.utils.rpc import send_rpc

logger = logging.getLogger('block_parser')


def parse_transaction(message):
    rpc = None
    # get the transaction hash from the message and return if none found
    tx_hash = message.get('tx_hash')

    if not tx_hash:
        logger.error('no transaction hash in message')
        return
    # get the index from the message
    tx_index = message.get('tx_index')

    if tx_index is None:
        logger.warning('no tx index in message')
        tx_index = -1
    # get the block from the message
    block_hash = message.get('block_hash')

    if not block_hash:
        logger.warning('no block id in message')
        # we are scanning just the transaction so fetch the raw data
        rpc = send_rpc(
            {
                'method': 'getrawtransaction',
                'params': [tx_hash, 1]
            }
        )
        if rpc['error']:
            logger.error('rpc error: {}'.format(rpc['error']))
            return

        # get the block_hash from the transaction
        block_hash = rpc['result']['blockhash']

    block, created = Block.objects.get_or_create(hash=block_hash)
    if created:
        logger.warning('block is newly created so parsing full block')
        Channel('parse_block').send({'block_hash': block_hash})
        return

    logger.info('parsing tx {} for block {}'.format(tx_hash, block.height))
    tx, created = Transaction.objects.get_or_create(
        tx_id=tx_hash,
        block=block,
        index=tx_index
    )
    if created:
        logger.info('new tx')
        # fetch the rpc data for the block
        if not rpc:
            rpc = send_rpc(
                {
                    'method': 'getrawtransaction',
                    'params': [tx_hash, 1]
                }
            )
            if rpc['error']:
                logger.error('rpc error: {}'.format(rpc['error']))
                return
        # parse the block to save it
        tx.parse_rpc_tx(rpc['result'])
        logger.info('saved tx {} at block {}'.format(tx_hash, block.height))
    else:
        logger.info('existing tx found at {}'.format(block.height))
        # validate the block
        valid, error_message = tx.validate()
        if not valid:
            # transaction is invalid so re-fetch from rpc and save again
            logger.warning('INVALID TX at {}! {}'.format(block.height, error_message))
            # get it again to redo the inputs
            rpc = send_rpc(
                {
                    'method': 'getrawtransaction',
                    'params': [tx_hash, 1]
                }
            )
            if rpc['error']:
                logger.error('rpc error: {}'.format(rpc['error']))
                return
            # parse the block to save it
            tx.parse_rpc_tx(rpc['result'])
            logger.info('re scanned and save saved tx')

