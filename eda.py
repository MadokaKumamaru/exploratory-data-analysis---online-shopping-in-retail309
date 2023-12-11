# This file will contain code to conduct EDA

# Import required packages
from statsmodels.graphics.gofplots import qqplot
import matplotlib.pyplot as plt
import pandas as pd

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
    

# Create a class which contains methods to extract information
# from the DataFrame and its columns
class DataFrameInfo:
    def __init__(self, dataframe):
        self.dataframe = dataframe
        
    # Define a method to describe all columns in the DataFrame
    def get_description(self):
        print(self.dataframe.describe())
        
    # Define a method to extract statistical values (mean, median
    # and standard deviation) from the float64 columns
    def get_statistical_values(self, column):
        print('Mean:', self.dataframe[column].mean())
        print('Median:', self.dataframe[column].median())
        print('Standard Deviation:', self.dataframe[column].std())
        
    # Define a method to count distinct values in categorical columns
    def get_counts(self, column):
        self.dataframe[column].value_counts()
        
    # Define a method to print out the shape of the DataFrame
    def get_shape(self):
        print('Shape:', self.dataframe.shape)
        
    # Define a method to generate a count and percentage of NULL values 
    # in each column
    def get_NULL_counts(self, column):
        print('Number of NULLs for', column, self.dataframe[column].isnull().sum())
        print('Percentage of NULLs for', column, self.dataframe[column].isnull().sum()/
              len(self.dataframe) * 100)
        

# Create a class to visualise insights from data
class Plotter:
    def __init__(self, dataframe):
        self.dataframe = dataframe
    
    # Define a method to plot histogram to check skewness
    def plot_histograms(self, column):
        self.dataframe[column].hist(bins = 20)
        plt.title(f'Histogram for {column}')
        plt.show()
        
    # Define a method to plot Q-Q plot to check skewness
    def plot_qqplot(self, column):
        qq_plot = qqplot(self.dataframe[column], scale = 1, line = 'q', fit = True)
        plt.title(f'Q-Q plot for {column}')
        plt.show()

# Create a class to perform EDA transformations on 
# data
class DataFrameTransform:
    def __init__(self, dataframe):
        self.dataframe = dataframe
        
    # Define a method to impute NULLs with mode
    def mode_impute(self, column):
        column_mode = self.dataframe[column].mode().iloc[0]
        self.dataframe[column].fillna(column_mode, inplace=True)
        
    # Define a method to impute NULLs with mean
    def mean_imputation(self, column):
        self.dataframe[column] = self.dataframe[column].fillna(self.dataframe[column].mean())
        
    # Define a method to impute NULLs with median
    def median_imputation(self, column):
        self.dataframe[column] = self.dataframe[column].fillna(self.dataframe[column].median())
        
# Get all the column names from the dataset
columns = list(customer_activity.columns)

# Use a method to determine the amount of NULLs in each column
customer_activity_info = DataFrameInfo(customer_activity)
for column in columns:
    print(customer_activity_info.get_NULL_counts(column))
    
# Conduct mode impute for categorical columns and check all NULLs have been imputed
customer_activity_transform = DataFrameTransform(customer_activity)
categorical_missing_columns = ['administrative', 'product_related', 'operating_systems']
for column in categorical_missing_columns:
    customer_activity_transform.mode_impute(column)
    print(customer_activity_info.get_NULL_counts(column))
    
# Plot numerical columns with missing values to check skewness
customer_activity_plotter = Plotter(customer_activity)
numeric_missing_columns = ['administrative_duration', 'product_related_duration']
for column in numeric_missing_columns:
    customer_activity_plotter.plot_histograms(column)
    
# Conduct median imputation for numerical columns with missing values and check all 
# NULLs have been imputed
for column in numeric_missing_columns:
    customer_activity_transform.median_imputation(column)
    print(customer_activity_info.get_NULL_counts(column))

    
    
# Identify skewness in each numerical column
df_for_skewness = customer_activity[['administrative_duration', 'informational_duration', 'product_related_duration',
                   'bounce_rates', 'exit_rates', 'page_values']].copy()
print(df_for_skewness.skew())

# Q-Q plot for numerical columns
numeric_columns = list(customer_activity.columns)
for column in numeric_columns:
    customer_activity_plotter.plot_qqplot(column)