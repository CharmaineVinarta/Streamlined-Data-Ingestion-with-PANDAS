# Create a dictionary, datetime_cols indicating that the new column Part2Start should consist of Part2StartDate and Part2StartTime.
# Load the survey response file, supplying the dictionary to the parse_dates argument to create a new Part2Start column.
# View summary statistics about the new Part2Start column with the describe() method.

# Create a dictionary, datetime_cols indicating that the new column Part2Start should consist of Part2StartDate and Part2StartTime.
# Load the survey response file, supplying the dictionary to the parse_dates argument to create a new Part2Start column.
# View summary statistics about the new Part2Start column with the describe() method.

# Create dict of columns to combine into new datetime column
datetime_cols = {"Part2Start":["Part2StartDate","Part2StartTime"]}

# Load file, supplying the dict to parse_dates
survey_data = pd.read_excel("fcc_survey_dts.xlsx",
parse_dates = datetime_cols)

# View summary statistics about Part2Start
print(survey_data.Part2Start.describe())
