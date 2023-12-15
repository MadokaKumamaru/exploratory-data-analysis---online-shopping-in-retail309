# Create a class which contains methods that can be appplied
# to the columns to handle data type conversions
class DatatypeTransform:
    def __init__(self, dataframe): 
        self.dataframe = dataframe
        
    # Define a method which converts columns to category datatype
    def convert_to_category(self, column):
        self.dataframe[column] = self.dataframe[column].astype('category')
        
    # Define a method which converts columns to int64 datatype
    def convert_to_int(self, column):
        self.dataframe[column] = self.dataframe[column].astype('int64')