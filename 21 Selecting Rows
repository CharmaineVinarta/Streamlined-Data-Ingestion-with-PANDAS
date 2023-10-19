# Create a query that selects all columns of records in hpd311calls that have 'SAFETY' as their complaint_type.
# Use read_sql() to query the database and assign the result to the variable safety_calls.
# Run the last section of code to create a graph of safety call counts in each borough.

# Create query to get hpd311calls records about safety
query = """
Select *
from hpd311calls
where complaint_type = 'SAFETY';
"""

# Query the database and assign result to safety_calls
safety_calls = pd.read_sql(query, engine)

# Graph the number of safety calls by borough
call_counts = safety_calls.groupby('borough').unique_key.count()
call_counts.plot.barh()
plt.show()


# filtering on multiple condition

# Create query for records with max temps <= 32 or snow >= 1
query = """
SELECT *
  FROM weather
  where tmax <= 32 
  or snow >= 1;
"""

# Query database and assign result to wintry_days
wintry_days = pd.read_sql(query, engine)

# View summary stats about the temperatures
print(wintry_days.describe())
