# logspul


def bla():
    return 'bla'

if __name__ == '__main__':
    from argparse import ArgumentParser
    import logging
    parser = ArgumentParser(description='Logtool')
    parser.add_argument('-ll', '--loglevel', type=str, choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], help='Set the logging level')
    args = parser.parse_args()

    logger = logging.getLogger('myLog')
    logging.basicConfig(level=args.loglevel)
    #logger.setLevel(logging.DEBUG)
    #logging.basicConfig(level=logging.DEBUG)
    x = bla()
    logger.debug('Dit wordt niet wat')
    logger.info('Hier verwacht ik niets van')
    logger.warning('Dit gaat helemaal niet goed')
