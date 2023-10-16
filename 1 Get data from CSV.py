# Get data from CSVs

# Import the pandas library as pd.
# Use read_csv() to load vt_tax_data_2016.csv and assign it to the variable data.
# View the first few lines of the dataframe with the head() method. This code has been written for you.

# Import pandas as pd
import pandas as pd

# Read the CSV and assign it to the variable data
data = pd.read_csv("vt_tax_data_2016.csv")

# View the first few lines of data
print(data.head(5))
