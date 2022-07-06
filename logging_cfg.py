import logging
from datetime import datetime

date_now = datetime.now().strftime("%Y%m%d")
logging.basicConfig(filename=f"logs/{date_now}_LOG.log", 
                    encoding='utf-8', 
                    level=logging.DEBUG,
                    format='[%(asctime)s] [%(name)-6s ][%(levelname)-5s] - %(message)s',
                    datefmt='%d-%m-%Y %I:%M:%S %p')
