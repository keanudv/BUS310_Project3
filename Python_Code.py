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
columns = df[["City","Sold_Price"]]

# Create a new dataframe with the selected columns
new_df = columns
new_df.head()

# Drop missing values and create the final dataframe for analysis
final_df = new_df.dropna()
final_df.isnull().sum()

# Exploratory Data Analysis (EDA)
final_df.shape
final_df.dtypes
final_df.describe()
final_df.max()
final_df.min()

# Set the null hypothesis and significance level
null_hypothesis = 1_500_000
alpha = 0.05

# Extract the sold prices
sold_prices = final_df["Sold_Price"]

# Calculate the Test Statistic, P-Value, and Critical Value
t_stat, p_value = stats.ttest_1samp(sold_prices, null_hypothesis)
critical_value = stats.t.ppf(1-alpha/2, len(sold_prices)-1)
print(f"t-STAT: {t_stat:.4f}")
print(f"P-Value: {p_value:.4f}")
print(f"Critical Value: {critical_value:.4f}")

# Conclusion using the Test-Statistic
if t_stat > critical_value:
  print("Reject the null hypothesis. There is sufficient evidence to conclude that the mean sold price of homes in Maui is not $1.5 million.")
else:
  print("Do not reject the null hypothesis. There is not sufficient evidence to conclude that the mean sold price of homes in Maui is different from $1.5 million")

# Conclusion using the P-Value
if p_value < alpha:
  print("Reject the null hypothesis. There is sufficient evidence to conclude that the mean sold price of homes in Maui is not $1.5 million.")
else:
  print("Do not reject the null hypothesis. There is not sufficient evidence to conclude that the mean sold price of homes in Maui is different from $1.5 million.")

# Create the sampling distribution
x = np.linspace(-4,4,1000)
y = stats.t.pdf(x, len(sold_prices)-1)
plt.plot(x,y, label="t-dist", color="blue")
plt.fill_between(x,y, where=(x > critical_value) | (x < -critical_value), color="red", alpha=alpha, label="Rejection Region")
plt.axvline(t_stat, color="green", linestyle="--", label=f"t-STAT = {t_stat:.4f}")
plt.text(t_stat, 0.05, f'{t_stat:.3f}', color='green', horizontalalignment='center')
plt.text(critical_value, 0.05, f'{critical_value:.3f}', color='red', horizontalalignment='right')
plt.text(-critical_value, 0.05, f'{-critical_value:.3f}', color='red', horizontalalignment='left')
plt.show()
