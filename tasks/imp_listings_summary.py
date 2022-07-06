import sys
sys.path.insert(0, './')

from db_postgres import *
from logging_cfg import *

postgres_dataframe(connect_postgres(), 'datasets', 'listings_summary.csv', 'tb_listings_summary', 'utf-8')