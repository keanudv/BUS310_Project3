'''
Name: Keanu Valencia
Date: 10/2/24
Class: BUS 310
'''

# Import the libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset into Python
file_location = "C:\\Users\\keanu\\OneDrive\\Desktop\\School\\Data Science\\BUS 310 Projects\\Hotsheet.csv"
encoding = "UTF-8"
df = pd.read_csv(file_location, encoding=encoding)

# View the data
df.head()
df.tail()

# Select only the needed columns
columns = df[["City", "Sold_Price"]]
print(columns)

# Create a new dataframe with the selected columns
new_df = columns
new_df.head()

# Drop missing values and create the final dataframe for analysis
final_df = new_df.dropna()

#Exploratory Data Analysis (EDA)
final_df.isnull().sum()
final_df.shape
final_df.describe()
final_df.max()
final_df.min()
final_df.dtypes

