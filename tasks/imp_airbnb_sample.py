import sys
sys.path.insert(0, './')

from db_postgres import *
from logging_cfg import *

postgres_dataframe(connect_postgres(), 'datasets', 'airbnb_sample.csv', 'tb_airbnb_sample', 'utf-8')
