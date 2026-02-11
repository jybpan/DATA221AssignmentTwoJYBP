import pandas as pd 

dataframe = pd.read_csv("student.csv")

print(dataframe)

filteredDataframe = dataframe.query('grade >= 10 and internet == 1 and absences <= 5')
filteredDataframe.to_csv("high_engagement.csv")