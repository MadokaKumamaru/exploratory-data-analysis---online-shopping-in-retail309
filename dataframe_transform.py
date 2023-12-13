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
        
    # Define a method to impute NULLs with mean
    def mean_impute(self, column):
        self.dataframe[column] = self.dataframe[column].fillna(self.dataframe[column].mean())
        
    # Define a method to impute NULLs with median
    def median_impute(self, column):
        self.dataframe[column] = self.dataframe[column].fillna(self.dataframe[column].median())
        
    # Define a method to compute log transform
    def log_transform(self, column):
        self.dataframe[column] = self.dataframe[column].map(lambda i: np.log(i) if i > 0 else 0)
        
    # Define a method to compute Yeo-Johnson transform
    def yeo_johnson_transform(self, column):
        self.dataframe[column] = stats.yeojohnson(self.dataframe[column])[0]
        
    # Define a method to drop outliers
    def drop_outliers(self, z_score_column):
        outliers = self.dataframe[(self.dataframe[z_score_column] >= 3) | (self.dataframe[z_score_column] <= -3)]
        self.dataframe = self.dataframe.drop(outliers.index)
        
    # Define a method to drop columns
    def drop_column(self, column):
        self.dataframe.drop(column, axis = 1)