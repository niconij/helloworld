# logspul

import logging
logger = logging.getLogger('myLog')
#logging.basicConfig(level=logging.DEBUG)
#logger.setLevel(logging.DEBUG)

def bla():
    return 'bla'

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    x = bla()
    logger.debug('Dit wordt niet wat')
