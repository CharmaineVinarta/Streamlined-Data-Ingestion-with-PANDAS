# task here is to compile them in one dataframe for analysis. pandas has been imported as pd. 
# All sheets have been read into the ordered dictionary responses, where sheet names are keys and dataframes are values, get dataframes with the values() method.

# pandas has been imported as pd. All sheets have been read into the ordered dictionary responses, where sheet names are keys and dataframes are values
# get dataframes with the values() method.

# Create an empty dataframe
all_responses = pd.DataFrame()

# Set up for loop to iterate through values in responses
for df in responses.values():
  # Print the number of rows being added
  print("Adding {} rows".format(df.shape[0]))
  # Append df to all_responses, assign result
  all_responses = all_responses.append(df)

# Graph employment statuses in sample
counts = all_responses.groupby("EmploymentStatus").EmploymentStatus.count()
counts.plot.barh()
plt.show()
