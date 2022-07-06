import sys
sys.path.insert(0, './')

from db_postgres import *
from logging_cfg import *

postgres_dataframe(connect_postgres(), 'datasets', 'reviews_summary.csv', 'tb_reviews_summary', 'utf-8')