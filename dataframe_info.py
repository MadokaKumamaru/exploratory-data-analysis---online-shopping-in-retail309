# Create a class which contains methods to extract information
# from the DataFrame and its columns
class DataFrameInfo:
    def __init__(self, dataframe):
        self.dataframe = dataframe
        
    # Define a method to describe numeric columns in the DataFrame
    def get_description(self):
        print('Description for numeric columns:')
        print(self.dataframe.describe())
        
    # Define a method to extract statistical values (mean, median
    # and standard deviation) from the float64 columns
    def get_statistical_values(self, column):
        print(f'Mean for {column}:', self.dataframe[column].mean())
        print(f'Median for {column}:', self.dataframe[column].median())
        print(f'Standard Deviation for {column}:', self.dataframe[column].std())
        
    # Define a method to count distinct values in categorical columns
    def get_counts(self, column):
        self.dataframe[column].value_counts()
        
    # Define a method to print out the shape of the DataFrame
    def get_shape(self):
        print('Shape of the DataFrame:', self.dataframe.shape)
        
    # Define a method to generate a count and percentage of NULL values 
    # in each column
    def get_NULL_counts(self, column):
        print(f'Number of NULLs for {column}:', self.dataframe[column].isnull().sum())
        print(f'Percentage of NULLs for {column}:', round(self.dataframe[column].isnull().sum()/
              len(self.dataframe) * 100, 2), '%')
        
    # Define a method to get skewness for numeric columns
    def get_skewness(self, column):
        print(f'Skew of {column} is', self.dataframe[column].skew())