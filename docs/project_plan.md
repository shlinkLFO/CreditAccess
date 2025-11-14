# Survey of Consumer Expectations — Project Plan

## 1. Objectives
- Summarize and extract key insights from the FRBNY Survey of Consumer Expectations (SCE).
- Build a structured dataset suitable for exploratory data analysis (EDA).
- Develop a reproducible pipeline for cleaning, weighting, and analyzing the SCE microdata.

## 2. Key Findings from Documentation
- SCE is a rotating monthly panel (~1,300 respondents) capturing inflation, labor-market, housing, and household-finance expectations.
- Uses probabilistic and density-forecast formats to measure expectations and uncertainty.
- Provides point forecasts + density distributions for inflation, earnings, and home prices.
- Panel design minimizes volatility via stable tenure distribution; learning effects stabilize after 1–2 months.
- Representativeness achieved via stratified CCS sampling + ACS-aligned post-stratification weights.
- Monthly and quarterly supplements expand coverage (credit access, labor market, housing, spending).
- Data releases include weighted/unweighted medians, IQRs, and fitted density-statistics.

## 3. Dataset Overview (for EDA Planning)

### 3.1 Core Variables (Monthly)
**Inflation**
- 1-year point forecast
- 1-year density forecast (10 bins → fitted mean, median, IQR)
- 3-year point + density forecast

**Labor Market**
- Job-loss probability
- Probability of leaving job
- Job-finding probability
- Expected earnings change (point + density)

**Housing**
- Home-price change (point)
- Home-price density forecast

**Household Finance**
- Expected income growth
- Expected spending growth
- Credit-access variables

**Macroeconomic Expectations**
- Expected change in unemployment rate
- Expected change in interest rates
- Stock-market expectations
- Item-level price expectations (gas, food, rent, medical, tuition)

### 3.2 Demographics
- Age group
- Gender
- Education
- Income bracket
- Race/ethnicity
- Census division & region
- Household size, presence of young children

### 3.3 Panel Metadata
- Respondent ID
- Wave index
- Invitation batch
- Timestamps
- Survey completion sequence
- Attrition indicators

## 4. EDA Work Plan

### 4.1 Data Ingestion
- Load microdata (monthly release, nine-month lag).
- Standardize field names across monthly files.
- Validate completeness of panel identifiers.

### 4.2 Cleaning
- Handle missing categorical fields.
- Consolidate density-forecast bins into consistent structures.
- Verify density bins sum to 100%.
- Convert all % fields to numeric (float).
- Remove metadata fields not needed for analysis (or archive separately).

### 4.3 Weighting
- Apply ACS-aligned weights (income, education, age, region).
- Validate weight distribution (min/max/median, presence of extreme outliers).
- Create weighted/unweighted analytic samples.

## 5. Initial EDA Tasks

### 5.1 Quality Checks
- Missingness matrix (per variable × wave).
- Learning-phase shifts (wave 1 vs wave 3+).
- Response-time distribution.
- Density forecast consistency checks.

### 5.2 Core Variable Exploration
- Inflation (1-year): distribution + temporal trend
- Inflation uncertainty (IQR): dispersion across respondents
- Earnings expectations: point vs density-mean comparison
- Home-price expectations: region-level differences

### 5.3 Cross-Sectional Slicing
By:
- Age
- Income
- Education
- Race/ethnicity
- Region
- Panel tenure group

Metrics:
- Median expectations
- Uncertainty (IQR)
- Disagreement (cross-sectional IQR)

### 5.4 Panel Dynamics
- Month-to-month change in individual inflation density mean
- Persistence of uncertainty
- Event-response behavior (gas shocks, ACA events, etc.)

## 6. Modeling Roadmap (Optional Expansion)

### 6.1 Reduced-Form Models
- Inflation expectations ~ demographics + prior-month expectations
- Income/spending expectations ~ inflation expectations

### 6.2 Panel Fixed-Effects Models
- Individual responses vs macro events
- Time-varying uncertainty patterns

### 6.3 Structural Expectation-Link Models
- Job-loss probability → expected earnings change
- Inflation expectations → spending intentions

## 7. Deliverables

### 7.1 Core Deliverables
- Cleaned dataset (`sce_panel_clean.parquet`)
- Weighting pipeline (`weights.py`)
- EDA notebook (`01_eda.ipynb`)
- Variable dictionary (`variables.md`)
- Density-estimation module (`density_fit.py`)

### 7.2 Optional Deliverables
- Panel-modeling notebook
- Automated report generator
- Dashboard (Streamlit / Plotly)

## 8. Folder Structure (for Cursor Workspace)

```
sce-project/
│
├── data_raw/
├── data_clean/
├── notebooks/
│   └── 01_eda.ipynb
│
├── src/
│   ├── cleaning.py
│   ├── weights.py
│   ├── density_fit.py
│   └── utils.py
│
├── docs/
│   ├── project_plan.md
│   └── variables.md
│
└── README.md
```
