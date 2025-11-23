# Survey of Consumer Expectations — Credit Access Analysis

Comprehensive exploratory data analysis of the Federal Reserve Bank of New York's Survey of Consumer Expectations (SCE) Credit Access data (2013-2025).

---

## 📊 Quick Start

### Run the Analysis
```bash
# Install dependencies
pip install -r requirements.txt

# Launch Jupyter Notebook
jupyter notebook notebooks/01_eda_complete.ipynb
```

### View Results
- **Main Analysis:** `notebooks/01_eda_complete.ipynb`
- **Detailed Findings:** `docs/eda_findings.md`
- **Visualizations:** `data_clean/*.png`

---

## 📁 Project Structure

```
Final Project/
│
├── data_raw/                           # Original data
│   └── FRBNY-SCE-Credit-Access-Data 2.xlsx
│
├── data_clean/                         # Processed data & outputs
│   ├── overall_cleaned.csv            # Time series (36 periods)
│   ├── demographics_cleaned.csv       # By age & credit score
│   ├── time_series_plots.png         # Temporal trends
│   ├── correlation_heatmap.png       # Variable relationships
│   ├── distribution_plots.png        # Distributions
│   └── demographic_comparison.png    # Group comparisons
│
├── notebooks/
│   └── 01_eda_complete.ipynb         # ⭐ MAIN ANALYSIS NOTEBOOK
│
├── src/                               # Reusable Python modules
│   ├── cleaning.py                   # Data cleaning functions
│   ├── weights.py                    # Survey weighting
│   └── utils.py                      # Utility functions
│
├── docs/                              # Documentation
│   ├── eda_findings.md               # 📄 Comprehensive report
│   ├── project_plan.md               # Methodology
│   ├── variables_summary_overall.csv # Data dictionary
│   └── variables_summary_demographics.csv
│
├── requirements.txt                   # Python dependencies
└── README.md                          # This file
```

---

## 🔍 Dataset Overview

**Source:** Federal Reserve Bank of New York Survey of Consumer Expectations  
**Period:** October 2013 - June 2025 (36 semi-annual observations)  
**Sample:** ~1,300 respondents per wave  
**Focus:** Credit access patterns, application behavior, rejection rates, expectations

### Key Variables
- **Application Metrics:** Credit cards, auto loans, mortgages, refinancing
- **Rejection Rates:** Conditional on application by credit type
- **Expectations:** Perceived probability of rejection
- **Demographics:** Age groups (≤40, 40-59, ≥60) & Credit score (<680, 680-760, >760)

---

## 📈 Key Findings

### 1️⃣ Application Patterns
- **Credit Cards:** 28% application rate (most common)
- **Auto Loans:** 14% application rate
- **Mortgages:** 7% application rate (infrequent)

### 2️⃣ Rejection Patterns
- **Credit Limit Increases:** ~28% rejection (HIGHEST)
- **Auto Loans:** ~10% rejection (LOWEST)
- **Credit Cards:** ~18% rejection

### 3️⃣ Systematic Pessimism
- Consumers overestimate rejection rates by **+5-15 percentage points**
- Consistent across all credit types
- May contribute to discouragement effect

### 4️⃣ Demographic Disparities
- Credit score <680: **~20% rejection**
- Credit score >760: **~5% rejection**
- Clear gradient in credit access

### 5️⃣ Discouragement Effect
- **7% of respondents** deterred from applying
- Represents significant barrier to credit access

---

## 🛠️ Technical Details

### Dependencies
```
pandas >= 1.5.0
numpy >= 1.23.0
matplotlib >= 3.6.0
seaborn >= 0.12.0
openpyxl >= 3.0.0
scipy >= 1.9.0
```

### Data Processing
1. Load raw Excel file with multiple sheets
2. Clean headers and convert data types
3. Handle missing values (<2% total)
4. Export to CSV format
5. Generate visualizations

### Analysis Coverage
- ✓ Descriptive statistics
- ✓ Time series analysis (12 years)
- ✓ Demographic stratification
- ✓ Correlation analysis
- ✓ Expectation vs reality comparison
- ✓ Distribution analysis

---

## 📚 Documentation

### Main Documents
1. **`notebooks/01_eda_complete.ipynb`** - Full interactive analysis with code and visualizations
2. **`docs/eda_findings.md`** - Comprehensive written report (10 sections)
3. **`docs/project_plan.md`** - Methodology and project roadmap

### Variable Dictionaries
- `docs/variables_summary_overall.csv` - 36 credit access metrics
- `docs/variables_summary_demographics.csv` - 26 demographic metrics

---

## 🎯 Policy Implications

1. **Information Asymmetry:** Consumer education could reduce pessimistic bias
2. **Credit Access Equity:** Targeted interventions for subprime borrowers
3. **Discouragement Effect:** Pre-screening tools may increase access
4. **Economic Monitoring:** Early warning indicators for financial stress

---

## 🚀 Next Steps

### Recommended Further Analysis
1. **Time Series Modeling:** Decompose trends, seasonality, COVID-19 impact
2. **Expectation Formation:** Model drivers of systematic bias
3. **Discouragement Determinants:** Who is deterred and why?
4. **Cross-Sectional Studies:** Interaction effects, regional patterns

---

## 📞 Data Source & License

**Federal Reserve Bank of New York**  
Survey of Consumer Expectations (SCE)  
https://www.newyorkfed.org/microeconomics/sce

**License:** Data available under FRBNY terms (see `data_raw/` file License sheet)

---

## 📊 Analysis Status

✅ **EDA Complete** - November 14, 2025  
✅ Cleaned datasets generated  
✅ Visualizations created  
✅ Comprehensive documentation  
✅ Reusable code modules  

**Project:** MSBA Business Intelligence - Final Project

