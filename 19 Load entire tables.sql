-- data.db has two tables. weather has historical weather data for New York City. 
-- hpd311calls is a subset of call records made to the city's 311 help line about housing issues.

-- Load libraries
import pandas as pd
from sqlalchemy import create_engine

-- Create the database engine
engine = create_engine("sqlite:///data.db")

-- Load hpd311calls without any SQL
hpd_calls = pd.read_sql("hpd311calls", engine)

-- View the first few rows of data
print(hpd_calls.head())

-- Create a SQL query to load the entire weather table
query = """
SELECT * FROM hpd311calls;
"""

-- Load weather with the SQL query
weather = pd.read_sql("weather", engine)

-- View the first few rows of data
print(weather.head())
