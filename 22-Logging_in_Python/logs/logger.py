## Configuring Logging
import logging
logging.basicConfig(
    filename='app.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # asctime: timestamp, name: logger's name, levelname: level of the log message, message: actual log message
    datefmt='%Y-%m-%d %H:%M:%S',
)