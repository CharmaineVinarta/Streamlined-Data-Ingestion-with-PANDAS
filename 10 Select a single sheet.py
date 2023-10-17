# An Excel workbook may contain multiple sheets of related data. 
# The New Developer Survey response workbook has sheets for different years. 
# Because read_excel() loads only the first sheet by default, earlier we've gotten survey responses for 2016. 
# Now, create a dataframe of 2017 responses using read_excel()'s sheet_name argument in a couple different ways.

import pandas as pd

# Create df from second worksheet by referencing its position
responses_2017 = pd.read_excel("fcc_survey.xlsx",
                               sheet_name = 1)

# Graph where people would like to get a developer job
job_prefs = responses_2017.groupby("JobPref").JobPref.count()
job_prefs.plot.barh()
plt.show()


# Create a dataframe from the 2017 sheet by providing the sheet's name to read_excel().

# Create df from second worksheet by referencing its name
responses_2017 = pd.read_excel("fcc_survey.xlsx",
                               sheet_name = '2017')

# Graph where people would like to get a developer job
job_prefs = responses_2017.groupby("JobPref").JobPref.count()
job_prefs.plot.barh()
plt.show()
