import psycopg2, sys, shutil, chardet
from sqlalchemy import create_engine
import pandas as pd
from logging_cfg import *

def connect_postgres():
    conn = None
    try:
        conn_string = 'postgresql+psycopg2://postgres:123456@localhost:5432/postgres'
        db = create_engine(conn_string)
        conn = db.connect()
    except (Exception, psycopg2.DatabaseError) as e:
        logging.error(f"Falha ao conectar no Postgres {e}.")
        sys.exit(1)
    return conn 

def postgres_dataframe(conn, directory, file, name_table, enc):
    logging.info(f"[{file}] - Lendo arquivo CSV [{datetime.now()}].")
    h_start = datetime.now()
    
    try:
        df = pd.read_csv(directory+'/'+file, delimiter=',', low_memory=False, encoding=enc)
        logging.debug(f"[{file}] - Numero de Registros é [{len(df.index)}].")
        
        try:
            df.to_sql(name_table, con=conn, if_exists='fail', index=False)
        except (Exception, psycopg2.DatabaseError) as e:
            logging.error(f"[{file}] - Erro ao tentar importar.")
            logging.error(e)
            conn.close()
            return 1
        
        origem = directory+'/'+file
        destino = directory+'/ok/'+file
        shutil.move(origem, destino)
        
    except Exception as e:
        logging.error(f"[{file}] - Erro ao tentar abrir o DataFrame [{e}]")
        
    
    
    h_fim = datetime.now()
    h_total = (h_fim - h_start)
    logging.info(f"[{file}] - Tabela criada com sucesso [{datetime.now()}].")
    logging.debug(f"[{file}] - Tempo de Execução [{h_total}]")
    
