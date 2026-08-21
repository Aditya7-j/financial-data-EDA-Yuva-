import requests
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

COUNTRIES = {
    "IND":"India","USA":"United States","CHN":"China","GBR":"United Kingdom",
    "DEU":"Germany","JPN":"Japan","AUS":"Australia","CAN":"Canada","FRA":"France",
    "BRA":"Brazil","IDN":"Indonesia","ARE":"United Arab Emirates","SAU":"Saudi Arabia",
    "MEX":"Mexico","ZAF":"South Africa"
}
INDICATORS = {
    "Bank_Capital_Assets_pct":"FB.BNK.CAPA.ZS",
    "NPL_pct":"FB.AST.NPER.ZS",
    "Private_Credit_GDP_pct":"FD.AST.PRVT.GD.ZS"
}
OUT=Path("outputs"); OUT.mkdir(exist_ok=True)

def fetch_indicator(code, name):
    url=f"https://api.worldbank.org/v2/country/{';'.join(COUNTRIES)}/indicator/{code}?format=json&per_page=1000"
    r=requests.get(url,timeout=30); r.raise_for_status()
    rows=r.json()[1]
    return pd.DataFrame([{
        "Country":x["country"]["value"],"Code":x["countryiso3code"],
        "Year":int(x["date"]),"Value":float(x["value"])
    } for x in rows if x.get("value") is not None]).assign(Indicator=name)

frames=[fetch_indicator(code,name) for name,code in INDICATORS.items()]
long=pd.concat(frames,ignore_index=True)
long["Year"]=pd.to_numeric(long["Year"],errors="coerce")
long["Value"]=pd.to_numeric(long["Value"],errors="coerce")
long=long.dropna(subset=["Code","Year","Value"]).drop_duplicates()
long=long.sort_values(["Code","Indicator","Year"])
latest=long.groupby(["Code","Indicator"],as_index=False).tail(1)
wide=latest.pivot(index="Code",columns="Indicator",values="Value").reset_index()
wide["Country"]=wide["Code"].map(COUNTRIES)
wide=wide[["Country","Code"]+list(INDICATORS)]
wide.to_csv(OUT/"world_bank_latest_selected.csv",index=False)
print(wide)
print("\nDescriptive statistics:\n",wide[list(INDICATORS)].describe().T)
print("\nCorrelations:\n",wide[list(INDICATORS)].corr())

c=wide.sort_values("Bank_Capital_Assets_pct")
plt.figure(figsize=(9,6)); plt.barh(c["Country"],c["Bank_Capital_Assets_pct"])
plt.xlabel("Bank capital to assets ratio (%)"); plt.title("Bank Capital Adequacy — Selected Countries")
plt.tight_layout(); plt.savefig(OUT/"bank_capital_ratio.png",dpi=160); plt.close()

c=wide.sort_values("NPL_pct")
plt.figure(figsize=(9,6)); plt.barh(c["Country"],c["NPL_pct"])
plt.xlabel("Non-performing loans / gross loans (%)"); plt.title("Non-Performing Loan Ratios — Selected Countries")
plt.tight_layout(); plt.savefig(OUT/"npl_ratio.png",dpi=160); plt.close()

plt.figure(figsize=(8,6))
plt.scatter(wide["Private_Credit_GDP_pct"],wide["Bank_Capital_Assets_pct"])
x=wide["Private_Credit_GDP_pct"]; y=wide["Bank_Capital_Assets_pct"]
coef=np.polyfit(x,y,1); xx=np.linspace(x.min(),x.max(),100); plt.plot(xx,coef[0]*xx+coef[1])
plt.xlabel("Domestic credit to private sector by banks (% of GDP)")
plt.ylabel("Bank capital to assets ratio (%)"); plt.title("Bank Capital vs. Private-Sector Credit")
plt.tight_layout(); plt.savefig(OUT/"capital_vs_credit.png",dpi=160); plt.close()
