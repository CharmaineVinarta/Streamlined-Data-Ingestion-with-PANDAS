# The agi_stub column contains numbers that correspond to income categories, and zipcode has 5-digit values that should be strings -- treating them as integers means we lose leading 0s, which are meaningful
# Load vt_tax_data_2016.csv with no arguments and view the dataframe's dtypes attribute. Note the data types of zipcode and agi_stub.

# Import panda
import pandas as pd 

# Load csv with no additional arguments
data = pd.read_csv("vt_tax_data_2016.csv")

# Print the data types
print(data.dtypes)

# Create dict specifying data types for agi_stub and zipcode
data_types = {"agi_stub":"category","zipcode":str
			  }

# Load csv using dtype to set correct data types
data = pd.read_csv("vt_tax_data_2016.csv", dtype=data_types)

# Print data types of resulting frame
print(data.dtypes.head())
