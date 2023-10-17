# The Vermont tax data contains 147 columns describing household composition, income sources, and taxes paid by ZIP code and income group. Most analyses don't need all these columns. 
# Ccreate a dataframe with fewer variables using read_csv()s usecols argument.
# pandas has already been imported as pd in workspace.

# Create a list of columns to use: zipcode, agi_stub (income group), mars1 (number of single households), MARS2 (number of households filing as married), and NUMDEP (number of dependents).
# Create a dataframe from vt_tax_data_2016.csv that uses only the selected columns.

# Create list of columns to use
cols = ["zipcode", "agi_stub", "mars1", "MARS2", "NUMDEP"]

# Create dataframe from csv using only selected columns
data = pd.read_csv("vt_tax_data_2016.csv", usecols = cols)

# View counts of dependents and tax returns by income level
print(data.groupby("agi_stub").sum())
