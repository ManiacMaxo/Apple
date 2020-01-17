import logging
from logging.handlers import RotatingFileHandler

info_logger = logging.getLogger('info_logger')
info_logger.setLevel(logging.INFO)
info_file_handler = RotatingFileHandler('static/logs/info.log', maxBytes=10000, backupCount=5)

error_logger = logging.getLogger('error_logger')
error_logger.setLevel(logging.ERROR)
error_file_handler = RotatingFileHandler('static/logs/error.log', maxBytes=10000, backupCount=5)

log_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

info_file_handler.setFormatter(log_formatter)
error_file_handler.setFormatter(log_formatter)

info_logger.addHandler(info_file_handler)
error_logger.addHandler(error_file_handler) 