from lgg import get_logger


def test_import():
    get_logger()


def test_logging():
    logger = get_logger()

    logger.info('This is an info message')
    logger.debug('Debugging message')
    logger.error('Error message')
    logger.warning('File not found! An empty one is created')
