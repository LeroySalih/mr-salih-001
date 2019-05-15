import logging

# Create a custom logger
logger = logging.getLogger(__name__)

# Create handlers
c_handler = logging.StreamHandler()
c_handler.setLevel(logging.INFO)
c_format = logging.Formatter('%(asctime)s %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)

# Create handlers
f_handler = logging.FileHandler('logs/app.log')
f_handler.setLevel(logging.INFO)
f_format = logging.Formatter('%(asctime)s %(name)s - %(levelname)s - %(message)s')
f_handler.setFormatter(f_format)



# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)



