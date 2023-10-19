-- Create a database engine for data.db.
-- Write a SQL query that SELECTs the date, tmax, and tmin columns from the weather table.
-- Make a dataframe by passing the query and engine to read_sql() and assign the resulting dataframe to temperatures.

-- Create database engine for data.db
engine = create_engine("sqlite:///data.db")

-- Write query to get date, tmax, and tmin from weather
query = """
SELECT date, 
       tmax, 
       tmin
  FROM weather;
"""

-- Make a dataframe by passing query and engine to read_sql()
temperatures = pd.read_sql(query, engine)

-- View the resulting dataframe
print(temperatures)
