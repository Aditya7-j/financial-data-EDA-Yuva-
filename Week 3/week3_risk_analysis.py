import pandas as pd
import matplotlib.pyplot as plt

# Week 3 — Risk Analysis
# Risk register based on Week 1 indicators and Week 2 India NPL forecast.

risks = pd.DataFrame([
    ["R1","Asset-quality deterioration","Medium","High",6],
    ["R2","Forecast/model uncertainty","High","Medium",6],
    ["R3","Data comparability / timing risk","High","Medium",6],
    ["R4","Credit-cycle / concentration risk","Medium","High",6],
    ["R5","Capital adequacy pressure","Medium","High",6],
    ["R6","Over-reliance on aggregate indicators","Medium","Medium",4],
], columns=["Risk ID","Risk","Likelihood","Impact","Score"])

risks.to_csv("Week3_Risk_Register.csv", index=False)

likelihood = {"Low":1, "Medium":2, "High":3}
impact = {"Low":1, "Medium":2, "High":3}

fig, ax = plt.subplots(figsize=(7,6))
ax.set_xlim(0.5,3.5)
ax.set_ylim(0.5,3.5)
ax.set_xticks([1,2,3], ["Low","Medium","High"])
ax.set_yticks([1,2,3], ["Low","Medium","High"])
ax.set_xlabel("Likelihood")
ax.set_ylabel("Impact")
ax.set_title("Week 3 — Financial Risk Matrix")
ax.grid(True, alpha=0.3)

for _, r in risks.iterrows():
    x = likelihood[r["Likelihood"]]
    y = impact[r["Impact"]]
    ax.scatter(x, y, s=170)
    ax.annotate(r["Risk ID"], (x,y), xytext=(6,6), textcoords="offset points")

plt.tight_layout()
plt.savefig("Week3_Risk_Matrix.png", dpi=180, bbox_inches="tight")
plt.show()
