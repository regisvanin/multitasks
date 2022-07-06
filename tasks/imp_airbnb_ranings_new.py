import sys
sys.path.insert(0, './')

from db_postgres import *
from logging_cfg import *

postgres_dataframe(connect_postgres(), 'datasets', 'airbnb_ratings_new.csv', 'tb_airbnb_ratings_new', 'latin1')
