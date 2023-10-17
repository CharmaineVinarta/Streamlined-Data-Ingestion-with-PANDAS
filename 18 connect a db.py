# In order to get data from a database with pandas, first need to be able to connect to one. 
# Practice creating a database engine to manage connections to a database, data.db. 
# To do this, use sqlalchemy's create_engine() function.

# create_engine() needs a string URL to the database. 
# For SQLite databases, that string consists of "sqlite:///", then the database file name.

# Import sqlalchemy's create_engine() function
from sqlalchemy import create_engine

# Create the database engine
engine = create_engine("sqlite:///data.db")

# View the tables in the database
print(engine.table_names())
