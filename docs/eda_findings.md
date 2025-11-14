# Exploratory Data Analysis - Key Findings
## FRBNY Survey of Consumer Expectations - Credit Access Data

**Analysis Date:** November 14, 2025  
**Data Source:** Federal Reserve Bank of New York Survey of Consumer Expectations

---

## 1. Dataset Overview

### 1.1 Overall Sheet
- **Dimensions:** 36 rows × 36 columns
- **Time Coverage:** October 2013 (201310) to June 2025 (202506)
- **Frequency:** Semi-annual observations over 12-year period
- **Numeric Variables:** 33 credit access metrics

### 1.2 Demographics Sheet
- **Dimensions:** 213 rows × 26 columns
- **Demographic Breakdowns:**
  - Age groups: 3 categories (≤40, 40-59, ≥60)
  - Credit score groups: 3 categories (<680, 680-760, >760)
- **Numeric Variables:** 23 credit access metrics

---

## 2. Key Variables Identified

### 2.1 Application Metrics
- **Applied_Accepted**: Percentage who applied and were accepted
- **Applied_Rejected**: Percentage who applied and were rejected
- **Discouraged**: Percentage discouraged from applying
- **AppliedforCreditCard**: Credit card application rate
- **AppliedforMortage_Home-BasedLoan**: Mortgage application rate
- **AppliedforAutoLoan**: Auto loan application rate
- **RequestedIncreaseinCreditCardLimit**: Credit limit increase requests
- **RequestedMortgageRefi**: Mortgage refinancing requests

### 2.2 Rejection Metrics
- **CCRejected**: Credit card rejection rate (conditional on application)
- **HomeLoanRejected**: Home loan rejection rate
- **AutoLoanRejected**: Auto loan rejection rate
- **CCLimitRejected**: Credit limit increase rejection rate
- **RefiRejected**: Refinancing rejection rate
- **Rejectedfromoneormoresourcesofcredit_givenapplied**: Overall rejection rate

### 2.3 Expectation Metrics
- **ChanceCCApplicationWillBeRejected**: Expected probability of CC rejection
- **ChanceMortgageApplicationWillBeRejected**: Expected probability of mortgage rejection
- **ChanceAutoLoanApplicationWillBeRejected**: Expected probability of auto loan rejection
- **ChanceCCLimitInc.RequestWillBeRejected**: Expected probability of limit increase rejection
- **ChanceRefiWillBeRejected**: Expected probability of refinancing rejection

### 2.4 Account Status
- **Closedatleastoneacctvoluntarily**: Voluntary account closures
- **Lenderclosedatleastoneacct**: Involuntary account closures by lender

### 2.5 Forward-Looking Metrics
- **LikelyApplyforCreditCard_Categ_Contin**: Likelihood of future CC application
- **LikelyApplyforMortage_Home-BasedLoan_Categ_Contin**: Likelihood of future mortgage application
- **LikelyApplyforAutoLoan_Categ_Contin**: Likelihood of future auto loan application
- **ChanceNeed**: Chance of needing credit
- **ChanceComeUp**: Chance of credit opportunity arising

---

## 3. Summary Statistics

### 3.1 Application Rates (Overall Sample)
- **Any Credit Application:** 25-50% of respondents
- **Credit Card Applications:** 15-30% of respondents
- **Mortgage Applications:** 2-9% of respondents
- **Auto Loan Applications:** 8-17% of respondents
- **Credit Limit Increases:** 8-18% of respondents
- **Refinancing Requests:** Up to 27% of respondents (varies significantly)

### 3.2 Rejection Rates (Conditional on Application)
- **Credit Card:** 8-26% rejection rate
- **Mortgage/Home Loan:** 7-24% rejection rate
- **Auto Loan:** 5-19% rejection rate
- **Credit Limit Increase:** 10-45% rejection rate
- **Refinancing:** 13-42% rejection rate

### 3.3 Expected Rejection Probabilities
- **Credit Card:** Mean ~24-35%
- **Mortgage:** Mean ~30-48%
- **Auto Loan:** Mean ~22-34%
- **Credit Limit Increase:** Mean ~27-42%
- **Refinancing:** Mean ~26-37%

### 3.4 Discouragement
- **Discouraged from Applying:** 2-9% of respondents

---

## 4. Demographic Patterns

### 4.1 By Age Group
- **Less than or equal to 40:** Higher application rates, younger borrowers more active
- **Between 40-59:** Moderate application rates, peak earning years
- **Over 60:** Lower application rates, likely established credit profiles

### 4.2 By Credit Score
- **Less than 680:** Higher rejection rates, more discouraged borrowers
- **Between 680-760:** Moderate rejection rates
- **Over 760:** Lower rejection rates, better credit access

---

## 5. Temporal Trends

### 5.1 Time Period
- Data spans from October 2013 to June 2025 (36 semi-annual observations)
- Captures multiple economic periods:
  - Post-financial crisis recovery (2013-2019)
  - COVID-19 pandemic period (2020-2021)
  - Post-pandemic recovery (2022-2025)

### 5.2 Notable Patterns
- Semi-annual measurement allows tracking of medium-term trends
- Sufficient time coverage to analyze cyclical patterns
- Recent data allows for contemporary policy relevance

---

## 6. Data Quality Assessment

### 6.1 Missing Data
- **Overall Sheet:** 1.65% missing (minimal)
- **Demographics Sheet:** 1.46% missing (minimal)
- Missing data concentrated in recent metrics (ChanceNeed, ChanceComeUp)

### 6.2 Sample Sizes
- **Overall Sample:** ~1,300 observations per wave
- **Demographic Subgroups:** 163-592 observations per category
- Adequate sample sizes for statistical analysis

---

## 7. Key Insights

### 7.1 Credit Access Barriers
1. Rejection rates vary significantly by credit type (credit limit increases face highest rejection)
2. Expected rejection probabilities exceed actual rejection rates (pessimistic expectations)
3. Non-trivial discouragement effect (2-9% deterred from applying)

### 7.2 Credit Type Differences
1. **Credit Cards:** Most common application type, moderate rejection rates
2. **Auto Loans:** Moderate application rates, lower rejection rates
3. **Mortgages:** Lowest application rates (expected for infrequent transaction)
4. **Refinancing:** High variability, likely driven by interest rate environment

### 7.3 Demographic Disparities
1. Clear credit score gradient in rejection rates
2. Age-related patterns in application behavior
3. Different credit needs across demographic segments

---

## 8. Data Files Generated

### 8.1 Cleaned Data
- `data_clean/overall_cleaned.csv` - Time series data
- `data_clean/overall_cleaned.parquet` - Optimized format
- `data_clean/demographics_cleaned.csv` - Demographic breakdowns
- `data_clean/demographics_cleaned.parquet` - Optimized format

### 8.2 Visualizations
- `data_clean/time_series_plots.png` - Temporal trends
- `data_clean/distribution_plots.png` - Variable distributions
- `data_clean/correlation_heatmap.png` - Inter-variable relationships
- `data_clean/demographic_comparison.png` - Group comparisons

### 8.3 Documentation
- `docs/variables_summary_overall.csv` - Overall variable dictionary
- `docs/variables_summary_demographics.csv` - Demographics variable dictionary

---

## 9. Recommendations for Further Analysis

### 9.1 Time Series Analysis
- Decompose trends, seasonality, and cyclical components
- Event studies (COVID-19 impact, policy changes)
- Forecasting future credit access patterns

### 9.2 Cross-Sectional Analysis
- Deeper demographic segmentation
- Credit score gradient analysis
- Age cohort effects

### 9.3 Panel Analysis
- If microdata available: individual-level dynamics
- Expectation accuracy analysis (expected vs. actual rejections)
- Discouragement determinants

### 9.4 Policy Implications
- Credit access equity across demographics
- Impact of economic shocks on credit availability
- Consumer expectations and financial decision-making

---

## 10. Limitations

1. **Aggregated Data:** Pre-aggregated statistics, not microdata
2. **Semi-Annual Frequency:** Cannot capture high-frequency dynamics
3. **Survey-Based:** Subject to self-reporting biases
4. **Sample Composition:** Rotating panel may have tenure effects

---

## Contact & References

**Data Source:**  
Federal Reserve Bank of New York  
Survey of Consumer Expectations (SCE)  
https://www.newyorkfed.org/microeconomics/sce

**License:**  
Data subject to FRBNY license terms  
See: docs/License (from original Excel file)

**Analysis conducted for:**  
MSBA Business Intelligence - Final Project  
November 2025

