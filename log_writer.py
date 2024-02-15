import logging

logging.basicConfig(filename='bot.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO, encoding='UTF-8')
logger = logging.getLogger(__name__)

# Отключение логирования aiogram
logging.getLogger('aiogram').setLevel(logging.WARNING)