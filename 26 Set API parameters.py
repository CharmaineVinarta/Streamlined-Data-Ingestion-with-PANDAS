api_url = "https://api.yelp.com/v3/businesses/search"

# Create dictionary to query API for cafes in NYC
parameters = {"term":"cafe",
          	  "location":"NYC"}

# Query the Yelp API with headers and params set
response = requests.get(api_url,
                params = parameters,
                headers = headers)

# Extract JSON data from response
data = response.json()

# Load "businesses" values to a dataframe and print head
cafes = pd.DataFrame(data["businesses"])
print(cafes.head())
