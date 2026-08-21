import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Historical World Bank/WDI NPL series used for the forecasting exercise
data = pd.DataFrame({
    "Year": [2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023],
    "NPL_Ratio_Percent": [2.7,3.4,4.0,4.4,5.9,9.2,10.0,9.5,9.2,7.9,6.5,4.8,1.7]
})

# Three-year simple moving average.
# Forecasts are generated recursively so each forecast can use the
# preceding forecast when a future year is not yet observed.
history = data["NPL_Ratio_Percent"].tolist()
forecast = []

for year in [2024, 2025, 2026]:
    prediction = np.mean(history[-3:])
    forecast.append({"Year": year, "Forecast_NPL_Ratio_Percent": prediction})
    history.append(prediction)

forecast_df = pd.DataFrame(forecast)
print(forecast_df)

# One-step rolling backtest
errors = []
for i in range(3, len(data)):
    prediction = data.loc[i-3:i-1, "NPL_Ratio_Percent"].mean()
    actual = data.loc[i, "NPL_Ratio_Percent"]
    errors.append(actual - prediction)

mae = np.mean(np.abs(errors))
rmse = np.sqrt(np.mean(np.square(errors)))
print("Backtest MAE:", round(mae, 2))
print("Backtest RMSE:", round(rmse, 2))

# Visualization
plt.plot(data["Year"], data["NPL_Ratio_Percent"], marker="o", label="Historical")
plt.plot(forecast_df["Year"], forecast_df["Forecast_NPL_Ratio_Percent"],
         marker="o", linestyle="--", label="3-year moving-average forecast")
plt.xlabel("Year")
plt.ylabel("NPL ratio (%)")
plt.title("India Bank NPL Ratio: Historical and Forecast")
plt.legend()
plt.tight_layout()
plt.show()
