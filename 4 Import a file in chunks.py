# The first 500 rows have been loaded as vt_data_first500
# To get the next 500 rows, employ several keyword arguments: nrows and skiprows to get the correct records, header to tell pandas the data does not have column names, and names to supply the missing column names.
# Also want to use the list() function to get column names from vt_data_first500 to reuse.
# pandas has been imported as pd.

# Use nrows and skiprows to make a dataframe, vt_data_next500, with the next 500 rows.
# Set the header argument so that pandas knows there is no header row.
# Name the columns in vt_data_next500 by supplying a list of vt_data_first500's columns to the names argument.

# Create dataframe of next 500 rows with labeled columns
vt_data_next500 = pd.read_csv("vt_tax_data_2016.csv", 
                       		  nrows = 500,
                       		  skiprows = 500,
                       		  header = None,
                       		  names = list(vt_data_first500))

# View the Vermont dataframes to confirm they're different
print(vt_data_first500.head())
print(vt_data_next500.head())
