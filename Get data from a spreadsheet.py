# Load the pandas library as pd.
# Read in fcc_survey.xlsx and assign it to the variable survey_responses.
# Print the first few records of survey_responses.

# Load pandas as pd
import pandas as pd

# Read spreadsheet and assign it to survey_responses
survey_responses = pd.read_excel("fcc_survey.xlsx")

# View the head of the dataframe
print(survey_responses.head())

