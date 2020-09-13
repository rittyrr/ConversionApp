import logging
import logging.handlers as handlers

logger = logging.getLogger('CurrencyConversionApp')
logger.setLevel(logging.INFO)
logger.setLevel(logging.ERROR)
logger.setLevel(logging.DEBUG)

"""Here we define our formatter"""
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logHandler = handlers.TimedRotatingFileHandler('currency_conversion.log', when='M', interval=1, backupCount=2)
logHandler.setLevel(logging.INFO)
logHandler.setLevel(logging.ERROR)
logHandler.setLevel(logging.DEBUG)

"""Here we set our logHandler's formatter"""
logHandler.setFormatter(formatter)

logger.addHandler(logHandler)

