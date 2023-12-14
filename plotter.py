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
        self.dataframe[column].hist(bins = 3)
        plt.title(f'Histogram for {column}')
        plt.show()
    
    # Define a method to plot bar chart for categorical columns
    def plot_barchart(self, column):
        sns.barplot(y = self.dataframe[column].index, x = self.dataframe[column].values)
        plt.title(f'Bar chart for {column}')
        plt.xticks(rotation = 90)
        plt.show()
        
    # Define a method to plot correlation matrix
    def plot_correlation_matrix(self):
        sns.heatmap(self.dataframe.corr(), annot = True, cmap = 'coolwarm')
        plt.show()