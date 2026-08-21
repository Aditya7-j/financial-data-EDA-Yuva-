# Week 1 — Understanding Financial Data

This project analyzes three World Bank World Development Indicators:
- `FB.BNK.CAPA.ZS` — Bank capital to assets ratio (%)
- `FB.AST.NPER.ZS` — Bank nonperforming loans to total gross loans (%)
- `FD.AST.PRVT.GD.ZS` — Domestic credit to private sector by banks (% of GDP)

The supplied CSV is a 15-country analytical sample used for the report. Observation years are retained because the latest available year differs across country/indicator combinations.

## Run
```bash
pip install -r requirements.txt
python financial_eda.py
```

The script retrieves the indicators from the public World Bank API, cleans the response, keeps the latest available observation per selected country/indicator, and creates EDA outputs.

Primary source: World Bank WDI.
