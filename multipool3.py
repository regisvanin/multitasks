from utils import *
from multiprocessing import Pool
    
directory = 'tasks'
all_tasks = Util(directory=directory).listTasks()

if __name__ == '__main__':
    logging.debug("Inicio do processo de execução das tarefas.")
    logging.info(f"Tarefas Identificadas ({all_tasks})")
    p = Pool(processes=2)
    p.map(runProgram, all_tasks)
