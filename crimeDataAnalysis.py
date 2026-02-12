import pandas as pd

crimeStats = pd.read_csv("crime.csv")

def crimeAssessment(capitaViolentCrimes):
    if capitaViolentCrimes >= 0.50:
        return "High-Crime"
    else:
        return "LowCrime"

crimeStats["risk"] = crimeStats["ViolentCrimesPerPop"].apply(crimeAssessment)

unemploymentRateByCrime = crimeStats.groupby("risk")["PctUnemployed"].mean()

for riskLevel in unemploymentRateByCrime.index:
    riskPercentage = unemploymentRateByCrime[riskLevel]*100
    print(f"{riskLevel}: {riskPercentage:.2f}%")