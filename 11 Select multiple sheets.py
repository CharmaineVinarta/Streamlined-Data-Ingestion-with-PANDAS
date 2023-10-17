import pandas as pd

# 1 Load both the 2016 and 2017 sheets by name with a list and one call to read_excel().
# Create df from second worksheet by referencing its name
responses_2017 = pd.read_excel("fcc_survey.xlsx",
                               sheet_name = '2017')

# Graph where people would like to get a developer job
job_prefs = responses_2017.groupby("JobPref").JobPref.count()
job_prefs.plot.barh()
plt.show()

# 2 Load the 2016 sheet by its position (0) and 2017 by name. Note the sheet names in the result.
# Load all sheets in the Excel file
all_survey_data = pd.read_excel("fcc_survey.xlsx",
                                sheet_name = [0,'2017'])

# View the sheet names in all_survey_data
print(all_survey_data.keys())


# 3 Load all sheets in the Excel file without listing them all.
# Load all sheets in the Excel file
all_survey_data = pd.read_excel("fcc_survey.xlsx",
                                sheet_name = None)

# View the sheet names in all_survey_data
print(all_survey_data.keys())
