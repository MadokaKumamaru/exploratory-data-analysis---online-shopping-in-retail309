# This file will contain code to extract data from the database
import yaml
from sqlalchemy import create_engine
import pandas as pd

# Create a function which loads the yaml credentials file and return 
# the data dictionary contained within
def import_yaml_credentials(yaml_filename):
    with open('yaml_filename', 'r') as file:
        return yaml.safe_load(file)

# Create a class which will contain the methods we will use to 
# extract data from the RDS database
class RDSDatabaseConnector:
    def __init__(self, yaml_filename, yaml_dictionary):
        self.yaml_filename = yaml_filename
        self.yaml_dictionary = import_yaml(file_name)
        
        # Define a method which initialises a SQLAlchemy engine 
        # from the credentials provided to the class
        def create_engine_sqlalchemy(self):
            DATABASE_TYPE = 'postgresql'
            DBAPI = 'psycopg2'
            ENDPOINT = self.yaml_dictionary['RDS_HOST']
            USER = self.yaml_dictionary['RDS_USER']
            PASSWORD = self.yaml_dictoinary['RDS_PASSWORD']
            PORT = self.yaml_dictionary['RDS_PORT']
            DATABASE = self.yaml_dictionary['RDS_DATABASE']
            engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}:{PORT}/{DATABASE}")
            engine.connect()
            
        # Define a method which extracts data from the RDS database
        # and returns it as a Pandas DataFrame
        def extract_data(self):
            ?????????
            
        
# Create a function which saves the data in .csv format to local machine
def save_data(df):
    df.to_csv('customer_activity.csv')
    
# Create a function which will load the data from your local machine
# into a pandas DataFrame
def load_data(df):
    df_csv = pd.read_csv('df')