import sys
sys.path.insert(0, './')

from db_postgres import *
from logging_cfg import *

postgres_dataframe(connect_postgres(), 'datasets', 'LA_Listings.csv', 'tb_airbnb_la_listings', 'latin1')
