import pandas as pd

LOW_MAX = 9
MEDIUM_MIN = 10
MEDIUM_MAX = 14
HIGH_MIN = 15

dataframe = pd.read_csv("student.csv")

def gradeBanding(grade):
    if grade <= LOW_MAX:
        return "Low"
    elif MEDIUM_MIN <= grade <= MEDIUM_MAX:
        return "Medium"
    else:
        return "High"

dataframe["gradeBand"] = dataframe["grade"].apply(gradeBanding)

summaryTable = (
    dataframe
    .groupby("gradeBand")
    .agg(
        numberOfStudents=("grade", "count"),
        averageAbsences=("absences", "mean"),
        percentWithInternet=("internet", lambda x: (x == "yes").mean() * 100) # Neat function formatting trick found using GPT-5.2
    )
    .reset_index()
)

summaryTable.to_csv("student_bands.csv", index=False)