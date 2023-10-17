# Import pandas
import pandas as pd

# Create dict specifying that 0s in zipcode are NA values
null_values = {"zipcode": 0}

# Load csv using na_values keyword argument
data = pd.read_csv("vt_tax_data_2016.csv", 
                   na_values={"zipcode": 0})

# View rows with NA ZIP codes
print(data[data.zipcode.isna()])
