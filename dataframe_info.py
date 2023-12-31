# This file contains code to get information from the DataFrame

# Import required packages
import numpy as np
import pandas as pd

# Create a class which contains methods to extract information
# from the DataFrame and its columns
class DataFrameInfo:
    def __init__(self, dataframe):
        self.dataframe = dataframe
        
    # Define a method to describe numeric columns in the DataFrame
    def get_description(self):
        print('Description for numeric columns:')
        print(self.dataframe.describe())
        
    # Define a method to extract median from the numeric columns
    def get_median(self, column):
        print(f'Median for {column}:', self.dataframe[column].median())
        
    # Define a method to count distinct values in categorical columns
    def get_counts(self, column):
        print(f'Counts for distinct values for {column}')
        df_value_counts = pd.DataFrame(self.dataframe[column].value_counts())
        df_value_counts = df_value_counts.reset_index()
        df_value_counts.columns = [f'{column}', 'counts']
        df_value_counts['percentage'] = round(df_value_counts['counts'] / df_value_counts['counts'].sum() * 100, 2)
        print(df_value_counts.to_string(index=False))
        
    # Define a method to print out the shape of the DataFrame
    def get_shape(self):
        print('Shape of the DataFrame:', self.dataframe.shape)
        
    # Define a method to generate counts and percentage of NULL values 
    # in each column
    def get_NULL_counts(self, column):
        print(f'Number of NULLs for {column}:', self.dataframe[column].isnull().sum())
        print(f'Percentage of NULLs for {column}:', round(self.dataframe[column].isnull().sum()/
              len(self.dataframe) * 100, 2), '%')
        
    # Define a method to get skewness for numeric columns
    def get_skewness(self, column):
        print(f'Skew of {column} is', round(self.dataframe[column].skew(), 2))
        
    # Define a method to get Z-scores for numerical columns
    def get_zscores(self, column):
        column_mean = np.mean(self.dataframe[column])
        column_std = np.std(self.dataframe[column])
        return (self.dataframe[column] - column_mean) / column_std