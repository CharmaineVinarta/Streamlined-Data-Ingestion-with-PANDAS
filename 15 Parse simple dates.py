# Load fcc_survey.xlsx, making sure that the Part1StartTime column is parsed as datetime data.
# View the first few values of the survey_data.Part1StartTime to make sure it contains datetimes.
# pandas has been loaded as pd

# Load file, with Part1StartTime parsed as datetime data
survey_data = pd.read_excel("fcc_survey.xlsx",
parse_dates=["Part1StartTime"])

# Print first few values of Part1StartTime
print(survey_data.Part1StartTime.head())
