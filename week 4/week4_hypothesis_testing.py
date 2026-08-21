import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df=pd.read_csv("Week4_India_NPL_Hypothesis_Test.csv")
r,p=stats.pearsonr(df["Year"],df["India_NPL_Percent"])
slope,intercept,rvalue,preg,se=stats.linregress(df["Year"],df["India_NPL_Percent"])
print("Pearson r:",round(r,3),"p-value:",round(p,6))
print("Slope:",round(slope,3),"R-squared:",round(rvalue**2,3))

plt.figure(figsize=(8,5))
plt.scatter(df["Year"],df["India_NPL_Percent"],label="Observed")
plt.plot(df["Year"],intercept+slope*df["Year"],label="Linear trend")
plt.xlabel("Year"); plt.ylabel("NPL / Gross Loans (%)")
plt.title("India NPL Ratio and Linear Trend (2011–2023)")
plt.legend(); plt.grid(True,alpha=.3); plt.tight_layout(); plt.show()
