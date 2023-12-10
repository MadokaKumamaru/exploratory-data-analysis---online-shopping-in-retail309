# This file will contain code to conduct EDA

# Import required module
import db_utils

# Import data from the Database
customer_activity_class = db_utils.RDSDatabaseConnector(db_utils.yaml_dictionary)
engine = customer_activity_class.connect_database()
customer_activity = customer_activity_class.extract_data(engine)

# Get the information about the DataFrame
customer_activity.info()

# Create a class which contains methods that can be appplied
# to DataFrame columns to handle datatype conversions
def DataTransform:
    def __init__(self): 
        
    # Define a method which will convert columns to category datatype
    def convert_to_category(self, column_name):
         