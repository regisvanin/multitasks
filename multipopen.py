import os                                                                       
from multiprocessing import Pool, current_process
from subprocess import Popen, PIPE, TimeoutExpired, CalledProcessError
from loggingcfg import *                                        

n_cores = 2
n_iterations = 0


def run_process(process):                                                             
    os.system(f'python {process}') 
    
# FUNCAO OU CLASS PARA EXECUTAR AS ROTINAS
def run_command(path):
    with Popen(path, shell=True, stderr=PIPE, stdout=PIPE, universal_newlines=True) as proc:
        logging.info(f"## Processo ({path}) Pid de Execução ({proc.pid}) Poll ({proc.poll()}) ##")
    
        if proc.stdout.readline():
            logging.warn(f"********* Leitura STDOUT {proc.stdout.readline()} ********")
        
        if proc.stderr.readline():
            logging.error(f"********* Leitura STDOUT {proc.stderr.readline()} ********")
    
    
    # try:
    #     proc = Popen(path, shell=True, stderr=PIPE, stdout=PIPE, universal_newlines=True)
    #     logging.info(f"## Processo ({path}) Pid de Execução ({proc.pid}) Poll ({proc.poll()}) ##")
    # except CalledProcessError as e:
    #     logging.error(f"********* CodError ({e.returncode}) Msg ({e.output})********")
        
        # try:
        #     outs, errs = proc.communicate(timeout=15)
        # except TimeoutExpired:
        #     proc.kill()
        #     outs, errs = proc.communicate()
        #     logging.error(f"Falha na Rotina ({path})")
    

# TAREFAS OU ARQUIVOS A SEREM EXECUTADOS
directory = 'tasks'
all_tasks = []

for i,file in enumerate(os.listdir(directory)):
    if file.endswith('.py') and file != "__init__.py":
        task = os.path.join(directory, file)
        all_tasks.append(task)
        n_iterations =+ 1


if __name__ == '__main__':
    p = Pool(processes=n_cores)
    p.map(run_command, all_tasks)
    logging.debug(f"********** Fim do Processdo, tarefas executadas -> {all_tasks} **********")
