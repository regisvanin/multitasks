import logging, os
from subprocess import Popen, PIPE, TimeoutExpired
from datetime import datetime


class Util:
    logging.basicConfig(filename=f"log/log_{datetime.now().strftime('%Y%m%d')}.log", encoding='utf-8', level=logging.DEBUG, format='[%(asctime)s] [%(name)-s ][%(levelname)-5s] - %(message)s', datefmt='%d-%m-%Y %I:%M:%S %p')  
    
    def __init__(self, directory ):
        self.directory = directory

    def listTasks(self):
        all_tasks = []
        for file in os.listdir(self.directory):
            if file.endswith('.py') and file != '__init__.py':
                task = os.path.join(self.directory, file)
                all_tasks.append(task)
        return all_tasks


       
def runProgram(tasks):
    with Popen(tasks, shell=True, stderr=PIPE, stdout=PIPE) as proc:
        
        if proc.stdout.readline():
            logging.warning(proc.stdout.readlines())
        
        if proc.stderr.readline():
            logging.error(proc.stderr.readlines())
            logging.error(proc.stderr.readlines())
                
        try:
            outs, errs = proc.communicate(timeout=30)
        except TimeoutExpired:
            logging.error(f"Falha na Rotina ({tasks})")
            proc.kill()
            outs, errs = proc.communicate()
            logging.error(errs)
            