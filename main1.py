import os, importlib
from logging_cfg import *
from db_postgres import *

logging.info(f"Inicio das Importações {datetime.now()}")
# Le o diretorio e pega as tarefas do dia
directory = 'tasks'

for file in os.listdir(directory):
    if file.endswith('.py'):
        task = os.path.join(directory, file)
        mod = importlib.import_module(directory+'.'+file)
        mod.run(connect_postgres(), 'datasets')