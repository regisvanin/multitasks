import os
from logging_cfg import *
from subprocess import Popen
from multiprocessing import Pool, freeze_support

def run_command(path):
    Popen(path, shell=True)


#logging.info(f"########################  Inicio das Importações [{datetime.now()}]  ########################")
# Le o diretorio e pega as tarefas do dia
directory = 'tasks'
all_tasks = []
for file in os.listdir(directory):
    if file.endswith('.py'):
        task = os.path.join(directory, file)
        all_tasks.append(task)
        
        #p = Popen([sys.executable,task], shell=False, stdin=PIPE, stdout=PIPE)
        #output = p.communicate()
        #logging.debug(output)
        
#logging.info(f"########################  Fim das Importações [{datetime.now()}]  ########################")


if __name__ == "__main__":
    freeze_support()
    pool = Pool(processes=2) #, maxtasksperchild=2
    pool.map(run_command, all_tasks)