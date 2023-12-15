# This file contains code to visualise the DataFrame

# Import required packages
import matplotlib.pyplot as plt
import seaborn as sns

# Create a class to visualise insights from the DataFrame
class Plotter:
    def __init__(self, dataframe):
        self.dataframe = dataframe
    
    # Define a method to plot histogram to check skewness
    def plot_histograms(self, column):
        plt.figure(figsize=(5,4))
        self.dataframe[column].hist(bins = 3)
        plt.title(f'Histogram for {column}')
        plt.show()
    
    # Define a method to plot counts for categorical columns
    def plot_counts(self, column):
        plt.figure(figsize=(5,4))
        self.dataframe[column].value_counts().plot(kind = 'bar')
        plt.title(f'Barplot for {column}')
        plt.show()
    
    # Define a method to plot correlation matrix
    def plot_correlation_matrix(self):
        sns.heatmap(self.dataframe.corr(), annot = True, cmap = 'coolwarm')
        plt.show()