# This file contains code to transfrom DataFrame

# Import required packages
import numpy as np
from scipy import stats
from scipy.stats import yeojohnson

# Create a class to perform EDA transformations on the DataFrame
class DataFrameTransform:
    def __init__(self, dataframe):
        self.dataframe = dataframe
        
    # Define a method to impute NULLs with mode
    def mode_impute(self, column):
        column_mode = self.dataframe[column].mode().iloc[0]
        self.dataframe[column].fillna(column_mode, inplace=True)
   
    # Define a method to impute NULLs with median
    def median_impute(self, column):
        self.dataframe[column] = self.dataframe[column].fillna(self.dataframe[column].median())
        
    # Define a method to compute Yeo-Johnson transform
    def yeo_johnson_transform(self, column):
        self.dataframe[column] = stats.yeojohnson(self.dataframe[column])[0]
        
    # Define a method to drop outliers
    def drop_outliers(self, column):
        outliers = self.dataframe[(self.dataframe[column] >= 3) | (self.dataframe[column] <= -3)]
        self.dataframe.drop(outliers.index, inplace = True)
        
    # Define a method to drop columns
    def drop_column(self, column):
        self.dataframe.drop(column, axis = 1, inplace = True)