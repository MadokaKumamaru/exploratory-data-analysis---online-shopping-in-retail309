# This file will contain code to conduct EDA

# Import required module
import db_utils

# Import data from the Database
customer_activity_class = db_utils.RDSDatabaseConnector(db_utils.yaml_dictionary)
engine = customer_activity_class.connect_database()
customer_activity = customer_activity_class.extract_data(engine)

# Get the data type of each column
print(customer_activity.dtypes)

# Create a class which contains methods that can be appplied
# to DataFrame columns to handle datatype conversions
class DataTransform:
    def __init__(self, dataframe): 
        self.dataframe = dataframe
        
    # Define a method which will convert columns to category datatype
    def convert_to_category(self, column_name):
        self.dataframe[column_name] = self.dataframe[column_name].astype('category')
         

# Covert data types for some columns to category 
customer_activity_DataTransform = DataTransform(customer_activity)
columns_to_transform = ['administrative', 'product_related', 'informational', 
                        'month', 'operating_systems', 'browser', 'region', 
                        'traffic_type', 'visitor_type']
for column in columns_to_transform:
    customer_activity_DataTransform.convert_to_category(column)
print(customer_activity.dtypes)
    
