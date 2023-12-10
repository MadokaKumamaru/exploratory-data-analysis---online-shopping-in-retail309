# This file will contain code to conduct EDA

# Import required module
import db_utils

# Import data from the Database
customer_activity_class = db_utils.RDSDatabaseConnector(db_utils.yaml_dictionary)
engine = customer_activity_class.connect_database()
customer_activity = customer_activity_class.extract_data(engine)

# Get the information about the DataFrame
print(customer_activity.head())
customer_activity.info()