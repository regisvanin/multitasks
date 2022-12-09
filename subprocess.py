import os
from subprocess import Popen, PIPE
from multiprocessing import Pool, freeze_support
import time

import logging
from datetime import datetime

date_now = datetime.now().strftime("%Y%m%d")
logging.basicConfig(filename=f"{date_now}_LOG.log", 
                    encoding='utf-8', 
                    level=logging.DEBUG,
                    format='[%(asctime)s] [%(name)-6s ][%(levelname)-5s] - %(message)s',
                    datefmt='%d-%m-%Y %HH:%M:%S %p')

directory = 'tasks'
all_tasks = []
number_of_subproccesses = 0
while number_of_subproccesses <= 1:
    for file in os.listdir(directory):
        if file.endswith('.py') and os.path.splitext(file)[0] != "__init__":
            task = os.path.join(directory, file)
            all_tasks.append(task)
            
            p = Popen([sys.executable,task], shell=False, stdin=PIPE, stdout=PIPE)
            output = p.communicate()
            logging.debug(output)
            number_of_subproccesses = number_of_subproccesses + 1
            
            if number_of_subproccesses == 1:
                time.sleep(0.1)
                
            print(number_of_subproccesses)
