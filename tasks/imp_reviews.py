import sys
sys.path.insert(0, './')

from db_postgres import *
from logging_cfg import *

postgres_dataframe(connect_postgres(), 'datasets', 'reviews.csv', 'tb_reviews', 'utf-8')