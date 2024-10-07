'''
Name: Keanu Valencia
Date: 10/2/24
Class: BUS 310
'''

# Import the libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Load the dataset into Python
file_location = "C:\\Users\\keanu\\OneDrive\\Desktop\\School\\Data Science\\BUS 310 Projects\\Hotsheet.csv"
encoding = "UTF-8"
df = pd.read_csv(file_location, encoding=encoding)

# View the data
df.head()
df.tail()

# Select only the needed columns
columns = df["Sold_Price"]
print(columns)

# Create a new dataframe with the selected columns
new_df = columns
new_df.head()

# Drop missing values and create the final dataframe for analysis
final_df = new_df.dropna()

# Exploratory Data Analysis (EDA)
final_df.isnull().sum()
final_df.shape
final_df.describe()
final_df.max()
final_df.min()
final_df.dtypes

# Set the null hypothesis and significance level
null_hypothesis = 1_000_000
alpha = 0.05

# Extract the sold prices
sold_prices = final_df["Sold_Price"]

# Perform the t-test
t_stat, p_value = stats.ttest_1samp(sold_prices, null_hypothesis)
print(f"t-STAT: {t_stat:.4f}")
print(f"P-Value: {p_value:.4f}")

# conclusion
if p_value < alpha:
  print("Reject the null hypothesis. There is sufficient evidence to conclude that the mean sold price of homes in Maui is not $1 million.")
else:
  print("Do not reject the null hypothesis. There is not sufficient evidence to conclude that the mean sold price of homes in Maui is different from $1 million.")
