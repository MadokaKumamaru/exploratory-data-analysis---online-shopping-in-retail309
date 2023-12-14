# This file contains code to extract data from the RDS database

# Import required packages
from sqlalchemy import create_engine
import pandas as pd
import yaml

# Create a function which loads the yaml credentials file and return 
# the data dictionary contained within
def import_yaml():
    with open('credentials.yaml', 'r') as file:
        return yaml.safe_load(file)
yaml_dictionary = import_yaml()    

# Create a class which will contain the methods we will use to 
# extract data from the RDS database
class RDSDatabaseConnector:
    def __init__(self, yaml_dictionary):
        self.yaml_dictionary = yaml_dictionary
        
    # Define a method which initialises a SQLAlchemy engine 
    # from the credentials provided to the class
    def connect_database(self):
        DATABASE_TYPE = 'postgresql'
        DBAPI = 'psycopg2'
        ENDPOINT = self.yaml_dictionary['RDS_HOST']
        USER = self.yaml_dictionary['RDS_USER']
        PASSWORD = self.yaml_dictionary['RDS_PASSWORD']
        PORT = self.yaml_dictionary['RDS_PORT']
        DATABASE = self.yaml_dictionary['RDS_DATABASE']
        return create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}:{PORT}/{DATABASE}")
            
    # Define a method which extracts data from the RDS 
    # database and returns it as a Pandas DataFrame
    def extract_data(self, engine):
        return pd.read_sql_table('customer_activity', engine)
            
        
