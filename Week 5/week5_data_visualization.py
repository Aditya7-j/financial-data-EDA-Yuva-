import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Week5_Financial_Visualization_Data.csv")

# Ranked bar charts
for col, title, xlabel, filename in [
    ("Bank_Capital_to_Assets_pct","Bank Capital-to-Assets Ratio by Country","Bank capital / assets (%)","Week5_01_Bank_Capital.png"),
    ("NPL_to_Gross_Loans_pct","Non-Performing Loans as % of Gross Loans","NPL / gross loans (%)","Week5_02_NPL_Ratio.png"),
    ("Private_Credit_to_GDP_pct","Private-Sector Credit Provided by Banks","Private credit / GDP (%)","Week5_03_Private_Credit.png"),
]:
    s = df.sort_values(col)
    plt.figure(figsize=(10,6))
    plt.barh(s["Country"], s[col])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.grid(axis="x", alpha=.25)
    plt.tight_layout()
    plt.savefig(filename, dpi=180, bbox_inches="tight")
    plt.close()

# Relationship charts
plt.figure(figsize=(8,6))
plt.scatter(df["Bank_Capital_to_Assets_pct"], df["NPL_to_Gross_Loans_pct"])
plt.xlabel("Bank capital / assets (%)")
plt.ylabel("NPL / gross loans (%)")
plt.title("Bank Capital vs. Non-Performing Loans")
plt.grid(alpha=.25)
plt.tight_layout()
plt.savefig("Week5_04_Capital_vs_NPL.png", dpi=180, bbox_inches="tight")
plt.close()

plt.figure(figsize=(8,6))
plt.scatter(df["Private_Credit_to_GDP_pct"], df["NPL_to_Gross_Loans_pct"])
plt.xlabel("Private credit / GDP (%)")
plt.ylabel("NPL / gross loans (%)")
plt.title("Private Credit Depth vs. NPL Ratio")
plt.grid(alpha=.25)
plt.tight_layout()
plt.savefig("Week5_05_Credit_vs_NPL.png", dpi=180, bbox_inches="tight")
plt.close()

print(df.corr(numeric_only=True))
