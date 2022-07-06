import sys
sys.path.insert(0, './')

from db_postgres import *
from logging_cfg import *

postgres_dataframe(connect_postgres(), 'datasets', 'NY_Listings.csv', 'tb_airbnb_ny_listings', 'latin1')
