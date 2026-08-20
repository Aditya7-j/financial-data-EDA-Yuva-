# Week 1 — Understanding Financial Data

## 📊 Project Overview

This project explores publicly available banking and financial-system data from the **World Bank World Development Indicators (WDI)**. The goal was to practice a complete financial-data workflow: **data acquisition, data cleaning, exploratory data analysis (EDA), visualization, and reporting**.

The analysis uses a 15-country sample covering developed and emerging economies.

## 🎯 Objectives

- Acquire publicly available financial data from the World Bank
- Understand and clean financial indicators
- Perform descriptive and exploratory analysis
- Compare banking-system conditions across countries
- Examine relationships between financial indicators
- Communicate findings through charts and a written report

## 📁 Dataset

The analysis uses three World Bank indicators:

| Indicator | World Bank Code | Description |
|---|---|---|
| Bank capital to assets | `FB.BNK.CAPA.ZS` | Bank capital and reserves relative to total assets (%) |
| Non-performing loans | `FB.AST.NPER.ZS` | Nonperforming loans relative to total gross loans (%) |
| Private-sector credit | `FD.AST.PRVT.GD.ZS` | Domestic credit to the private sector provided by banks (% of GDP) |

The observation year is retained for each indicator because the latest available year differs across countries and indicators.

## 🛠️ Tools & Technologies

- **Python**
- **Pandas** — data preparation and analysis
- **NumPy** — numerical analysis
- **Matplotlib** — data visualization
- **Jupyter Notebook** — exploratory analysis
- **World Bank API / WDI** — public financial data source
- **GitHub** — project versioning and documentation

## 🔍 Analysis Workflow

```text
Public World Bank Data
        ↓
Data Acquisition
        ↓
Data Cleaning & Validation
        ↓
Descriptive Statistics
        ↓
Exploratory Data Analysis
        ↓
Visualizations & Correlations
        ↓
Financial Insights
        ↓
Final Report
