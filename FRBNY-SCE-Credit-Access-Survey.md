# FRBNY Survey of Consumer Expectations - Credit Access Module
## Complete Data Documentation

---

## Overview

This document provides complete documentation for the **Federal Reserve Bank of New York Survey of Consumer Expectations – Credit Access Module**, including file structure, variable definitions, and survey methodology.

**Last Updated:** November 2025  
**Survey Period:** October 2013 – October 2017 (YYYYMM format: 201310-201710)

---

## Data Files Structure

### File 1: `FRBNY-SCE-Credit-Access-complete_microdata (4).xlsx`
**Individual-level response data**

| Tab # | Sheet Name | Description | Dimensions |
|-------|------------|-------------|------------|
| 1 | Disclaimer | FRBNY copyright and disclaimer information | N/A |
| 2 | License | Terms of use and attribution requirements | N/A |
| **3** | **Data** | **Individual respondent microdata** | **36,277 observations × 140 variables** |
| **4** | **Codebook** | **Variable definitions and value codes** | **Complete data dictionary** |

**Key Variables in Tab 3 (Data):**
- `userid`: Unique respondent ID (7-digit number)
- `date`: Survey wave (YYYYMM format)
- `weight`: Sampling weight for population estimates
- `N1_1` through `N25_5`: Survey response variables

### File 2: `FRBNY-SCE-Credit-Access-Data (7).xlsx`
**Aggregated time-series data**

| Tab # | Sheet Name | Description | Dimensions |
|-------|------------|-------------|------------|
| 1 | Disclaimer | FRBNY copyright and disclaimer information | N/A |
| 2 | License | Terms of use and attribution requirements | N/A |
| **3** | **overall** | **Time-series aggregate statistics** | **Survey waves × 36 variables** |
| **4** | **demographics** | **Demographic breakdowns over time** | **Survey waves × 26 variables** |

**Tab 3 (overall):** Weighted population estimates for each survey wave  
**Tab 4 (demographics):** Breakdowns by age, income, education, region, numeracy

---

## Complete Variable Codebook
**Source: Microdata File Tab 4 (Codebook)**

### Variable Naming Convention

**Two naming systems are used throughout this documentation:**

1. **Original Technical Names** (`N1_1`, `N2_1`, etc.): As they appear in the raw Excel data
2. **Descriptive Names** (`HasCreditCard`, `CCBalance`, etc.): Human-readable names used in analysis notebooks

**All variable tables below include both naming conventions for easy reference.**

### Quick Reference: Variable Name Mapping

| Category | Original → Descriptive Examples |
|----------|--------------------------------|
| **Debt Types (N1)** | `N1_1` → `HasCreditCard`, `N1_2` → `HasMortgage`, `N1_3` → `HasStudentLoan` |
| **Balances (N2)** | `N2_1` → `CCBalance`, `N2_2` → `MortgageBalance`, `N2_3` → `StudentBalance` |
| **Balance Categories (N2b)** | `N2b_1` → `CCBalanceCat`, `N2b_2` → `MortgageBalanceCat` |
| **Applications (N4)** | `N4_1` → `AppliedCC`, `N4_2` → `AppliedMortgage`, `N4_3` → `AppliedAuto` |
| **No Apply Reasons (N5)** | `N5_1` → `NoNeed`, `N5_2` → `TooTimeConsuming`, `N5_5` → `ExpectedDenial` |
| **Discouraged (N6)** | `N6_1` → `DiscouragedCC`, `N6_2` → `DiscouragedMortgage` |
| **Outcomes (N9)** | `N9_1` → `OutcomeCC`, `N9_2` → `OutcomeMortgage`, `N9_3` → `OutcomeAuto` |
| **Late Payments (N15-N16)** | `N15` → `Late30Days`, `N16` → `Late90Days` |
| **Future Intent Likert (N17a)** | `N17a_1` → `IntentionCC`, `N17a_2` → `IntentionMortgage` |
| **Future Intent Prob (N17b)** | `N17b_1` → `ProbCC`, `N17b_2` → `ProbMortgage` |
| **Approval Prob (N21)** | `N21_1` → `ApprovalProbCC`, `N21_2` → `ApprovalProbMortgage` |
| **Credit Info (N22-N23)** | `N22` → `CreditScore`, `N23` → `LastScoreCheck` |
| **Liquidity (N24-N25)** | `N24` → `Need2000Prob`, `N25` → `Obtain2000Prob` |

---

### Core Identification Variables

| Original | Descriptive Name | Description | Values/Range |
|----------|------------------|-------------|--------------|
| `userid` | `UserID` | Unique Respondent ID | 0000000-9999999 (7-digit identifier) |
| `date` | `SurveyDate` | Survey Administration Month | 201310-201710 (YYYYMM format) |
| `weight` | `Weight` | Sampling Weight | Continuous (for population estimates) |

---

### N1: Types of Debt Currently Held
**Question:** "Which of the following types of debt do you currently have outstanding? Consider credit cards (including store cards), mortgages, home-based loans (such as HELOCs), auto loans, student loans, and other personal loans. (Select all that apply)"

| Original | Descriptive Name | Description | Coding |
|----------|------------------|-------------|--------|
| `N1_1` | `HasCreditCard` | Possess Credit Card | 0 = Don't Possess, 1 = Possess |
| `N1_2` | `HasMortgage` | Possess Mortgage | 0 = Don't Possess, 1 = Possess |
| `N1_3` | `HasStudentLoan` | Possess Student Loan | 0 = Don't Possess, 1 = Possess |
| `N1_4` | `HasHomeLoan` | Possess Home-based Loan (HELOC) | 0 = Don't Possess, 1 = Possess |
| `N1_5` | `HasAutoLoan` | Possess Auto Loan | 0 = Don't Possess, 1 = Possess |
| `N1_6` | `HasOtherLoan` | Possess Other Personal Loan | 0 = Don't Possess, 1 = Possess |
| `N1_7` | `HasNoDebt` | Possess None of the Above | 0 = Has at least one credit product, 1 = No credit products |

---

### N2: Current Debt Balances (Continuous)
**Question:** "What is your best guess of the current balance?"

| Original | Descriptive Name | Description | Values |
|----------|------------------|-------------|--------|
| `N2_1` | `CCBalance` | Current Balance: Credit Cards | 0-9,999,999 USD |
| `N2_2` | `MortgageBalance` | Current Balance: Mortgages | 0-9,999,999 USD |
| `N2_3` | `StudentBalance` | Current Balance: Student Loans | 0-9,999,999 USD |
| `N2_4` | `HomeBalance` | Current Balance: Home-based Loans | 0-9,999,999 USD |
| `N2_5` | `AutoBalance` | Current Balance: Auto Loans | 0-9,999,999 USD |
| `N2_6` | `OtherBalance` | Current Balance: Other Personal Loans | 0-9,999,999 USD |

---

### N2b: Current Debt Balances (Categorical)
**Alternative:** Categorical balance ranges if respondent cannot provide exact amount

**Variable Mapping:**
- `N2b_1` → `CCBalanceCat` (Credit Card Balance Category)
- `N2b_2` → `MortgageBalanceCat` (Mortgage Balance Category)
- `N2b_3` → `StudentBalanceCat` (Student Loan Balance Category)
- `N2b_4` → `HomeBalanceCat` (Home-based Loan Balance Category)
- `N2b_5` → `AutoBalanceCat` (Auto Loan Balance Category)
- `N2b_6` → `OtherBalanceCat` (Other Loan Balance Category)

**Credit Cards, Student Loans, Home-based Loans, Auto Loans, Other Personal Loans:**
- 1 = Less than $500
- 2 = $500 to $999
- 3 = $1,000 to $1,499
- 4 = $1,500 to $1,999
- 5 = $2,000 to $2,499
- 6 = $2,500 to $2,999
- 7 = $3,000 to $3,999
- 8 = $4,000 to $4,999
- 9 = $5,000 to $7,499
- 10 = $7,500 to $9,999
- 11 = $10,000 to $12,499
- 12 = $12,500 to $14,999
- 13 = $15,000 to $19,999
- 14 = $20,000 to $24,999
- 15 = $25,000 or more

**Mortgages (`N2b_2`):** Extended categories up to $2.5M+
- Categories 1-15 (same as above)
- 16 = $25,000 to $49,999
- 17 = $50,000 to $74,999
- 18 = $75,000 to $99,999
- 19 = $100,000 to $149,999
- 20 = $150,000 to $199,999
- 21 = $200,000 to $299,999
- 22 = $300,000 to $399,999
- 23 = $400,000 to $499,999
- 24 = $500,000 to $749,999
- 25 = $750,000 to $999,999
- 26 = $1,000,000 to $2,499,999
- 27 = $2,500,000 or more

---

### N3: Credit Card Utilization
**Shown if:** Respondent possesses credit card(s) (N1_1 = 1)

**Question:** "Over the past 12 months, did you borrow up to the limit ('max out') on any of your credit cards?"

| Original | Descriptive Name | Description | Coding |
|----------|------------------|-------------|--------|
| `N3` | `MaxedOutCC` | Maxed Out Credit Card(s) in Past 12 Months | 0 = No, 1 = Yes |

---

### N4: Credit Applications in Past 12 Months
**Question:** "During the last 12 months, did you do any of the following? (Answer Yes/No for each)"

| Original | Descriptive Name | Description | Coding |
|----------|------------------|-------------|--------|
| `N4_1` | `AppliedCC` | Applied for Credit Card | 0 = No, 1 = Yes |
| `N4_2` | `AppliedMortgage` | Applied for Mortgage or Home-based Loan | 0 = No, 1 = Yes |
| `N4_3` | `AppliedAuto` | Applied for Auto Loan | 0 = No, 1 = Yes |
| `N4_4` | `RequestedCCLimit` | Requested Credit Limit Increase (Credit Card) | 0 = No, 1 = Yes |
| `N4_5` | `RequestedLoanLimit` | Requested Loan Limit Increase | 0 = No, 1 = Yes |
| `N4_6` | `RequestedRefi` | Requested Mortgage Refinance | 0 = No, 1 = Yes |
| `N4_7` | `AppliedStudent` | Applied for Student Loan | 0 = No, 1 = Yes |

---

### N5: Reasons for Not Applying
**Shown if:** Respondent answered "No" to **all** items in N4

**Question:** "You just indicated that you did not apply for any new loans or credit cards, nor did you request any increases in limits or refinancing in the past 12 months. What is the reason for that? (Select all that apply)"

| Original | Descriptive Name | Description | Coding |
|----------|------------------|-------------|--------|
| `N5_1` | `NoNeed` | Satisfied with Current Financial Situation | 0 = Not selected, 1 = Selected |
| `N5_2` | `TooTimeConsuming` | Too Time-Consuming | 0 = Not selected, 1 = Selected |
| `N5_3` | `RatesTooHigh` | Borrowing Rates Too High | 0 = Not selected, 1 = Selected |
| `N5_4` | `DontKnowHow` | Don't Know How to Apply | 0 = Not selected, 1 = Selected |
| `N5_5` | `ExpectedDenial` | Expected to Be Denied | 0 = Not selected, 1 = Selected |

---

### N6: Discouraged Borrowers (Aggregate)
**Shown if:** Respondent selected "Did not think you would get approved" in N5

**Question:** "During the last 12 months, which of the following did you need but not apply for because you thought you would not be approved? (Select all that apply)"

| Original | Descriptive Name | Description | Coding |
|----------|------------------|-------------|--------|
| `N6_1` | `DiscouragedCC` | Needed but Didn't Apply: Credit Card | 0 = No, 1 = Yes |
| `N6_2` | `DiscouragedMortgage` | Needed but Didn't Apply: Mortgage/Home-based Loan | 0 = No, 1 = Yes |
| `N6_3` | `DiscouragedAuto` | Needed but Didn't Apply: Auto Loan | 0 = No, 1 = Yes |
| `N6_4` | `DiscouragedCCLimit` | Needed but Didn't Apply: Credit Limit Increase | 0 = No, 1 = Yes |
| `N6_5` | `DiscouragedLoanLimit` | Needed but Didn't Apply: Loan Limit Increase | 0 = No, 1 = Yes |
| `N6_6` | `DiscouragedRefi` | Needed but Didn't Apply: Mortgage Refinance | 0 = No, 1 = Yes |
| `N6_7` | `DiscouragedStudent` | Needed but Didn't Apply: Student Loan | 0 = No, 1 = Yes |
| `N6_8` | `NotDiscouraged` | None of the Above | 0 = No, 1 = Yes |

---

### N7: Item-Level Discouraged Borrowers
**Shown for each:** Specific items answered "No" in N4

**Question:** "During the last 12 months, did you need any of the following but **did not** apply because you thought you would not get approved? (For each applicable item: Yes/No)"

| Original | Descriptive Name | Description | Coding |
|----------|------------------|-------------|--------|
| `N7_1` | `NeededCC` | Credit Card: Needed but Expected Denial | 0 = No, 1 = Yes |
| `N7_2` | `NeededMortgage` | Mortgage/Home Loan: Needed but Expected Denial | 0 = No, 1 = Yes |
| `N7_3` | `NeededAuto` | Auto Loan: Needed but Expected Denial | 0 = No, 1 = Yes |
| `N7_4` | `NeededCCLimit` | Credit Limit Increase: Needed but Expected Denial | 0 = No, 1 = Yes |
| `N7_5` | `NeededLoanLimit` | Loan Limit Increase: Needed but Expected Denial | 0 = No, 1 = Yes |
| `N7_6` | `NeededRefi` | Mortgage Refinance: Needed but Expected Denial | 0 = No, 1 = Yes |
| `N7_7` | `NeededStudent` | Student Loan: Needed but Expected Denial | 0 = No, 1 = Yes |

---

### N8: Requested Credit Amounts
**Shown for each:** N4 item answered "Yes"

**Question:** "You stated that you applied for [X] in the past 12 months. What was the amount or limit you requested?"

**Response:** Open numeric field (dollars) or "Don't remember / Don't know"

| Original | Descriptive Name | Description | Values |
|----------|------------------|-------------|--------|
| `N8_1` | `RequestedCCAmt` | Credit Limit Requested: Credit Card | 0-9,999,999 USD |
| `N8_1_dk` | `RequestedCCUnknown` | Don't Remember Amount | 0 = Provided amount, 1 = Don't know |
| `N8_2` | `RequestedMortgageAmt` | Amount Requested: Mortgage/Home Loan | 0-9,999,999 USD |
| `N8_2_dk` | `RequestedMortgageUnknown` | Don't Remember Amount | 0 = Provided amount, 1 = Don't know |
| `N8_3` | `RequestedAutoAmt` | Amount Requested: Auto Loan | 0-9,999,999 USD |
| `N8_3_dk` | `RequestedAutoUnknown` | Don't Remember Amount | 0 = Provided amount, 1 = Don't know |
| `N8_4` | `RequestedCCLimitAmt` | Credit Limit Increase Requested | 0-9,999,999 USD |
| `N8_4_dk` | `RequestedCCLimitUnknown` | Don't Remember Amount | 0 = Provided amount, 1 = Don't know |
| `N8_5` | `RequestedLoanLimitAmt` | Loan Limit Increase Requested | 0-9,999,999 USD |
| `N8_5_dk` | `RequestedLoanLimitUnknown` | Don't Remember Amount | 0 = Provided amount, 1 = Don't know |
| `N8_6` | `RequestedRefiAmt` | Mortgage Refinance Amount Requested | 0-9,999,999 USD |
| `N8_6_dk` | `RequestedRefiUnknown` | Don't Remember Amount | 0 = Provided amount, 1 = Don't know |
| `N8_7` | `RequestedStudentAmt` | Student Loan Amount Requested | 0-9,999,999 USD |
| `N8_7_dk` | `RequestedStudentUnknown` | Don't Remember Amount | 0 = Provided amount, 1 = Don't know |

---

### N9: Application Outcomes
**Shown for each:** N4 item answered "Yes" (except refinance, which is covered by N11)

**Question:** "Was your request for [X] granted?"

**Response options:**
- Yes, fully granted (1)
- Yes, but only partly granted (2)
- No, request was rejected (3)

| Original | Descriptive Name | Credit Type |
|----------|------------------|-------------|
| `N9_1` | `OutcomeCC` | Credit Card Application Outcome |
| `N9_2` | `OutcomeMortgage` | Mortgage/Home Loan Application Outcome |
| `N9_3` | `OutcomeAuto` | Auto Loan Application Outcome |
| `N9_4` | `OutcomeCCLimit` | Credit Limit Increase Outcome |
| `N9_5` | `OutcomeLoanLimit` | Loan Limit Increase Outcome |
| `N9_6` | `OutcomeRefi` | Mortgage Refinance Outcome |
| `N9_7` | `OutcomeStudent` | Student Loan Application Outcome |

**Note:** N9_6 (Refinance Outcome) appears in early survey waves; later waves use N11 (binary Yes/No) instead.

---

### N10: Partial Grant Amounts
**Shown if:** N9 = 2 (Partially Granted) **and** N8 provided a numeric requested amount

**Question:** "You mentioned that your request for [X] was partly granted, and that your original request was for $Y. What was the dollar amount that was actually granted by your lender?"

**Response:** Open numeric field (dollars)

| Original | Descriptive Name | Description | Values |
|----------|------------------|-------------|--------|
| `N10_1` | `GrantedCCAmt` | Credit Limit Actually Granted: Credit Card | 0-9,999,999 USD |
| `N10_2` | `GrantedMortgageAmt` | Amount Actually Granted: Mortgage/Home Loan | 0-9,999,999 USD |
| `N10_3` | `GrantedAutoAmt` | Amount Actually Granted: Auto Loan | 0-9,999,999 USD |
| `N10_4` | `GrantedCCLimitAmt` | Credit Limit Actually Granted | 0-9,999,999 USD |
| `N10_5` | `GrantedLoanLimitAmt` | Loan Limit Increase Actually Granted | 0-9,999,999 USD |
| `N10_7` | `GrantedStudentAmt` | Student Loan Amount Actually Granted | 0-9,999,999 USD |

---

### N11: Mortgage Refinance Outcome
**Shown if:** N4_6 = "Yes" (Applied for mortgage refinance)

**Question:** "Was your request to refinance your mortgage granted?"

| Original | Descriptive Name | Description | Coding |
|----------|------------------|-------------|--------|
| `N11` | `RefiApproved` | Mortgage Refinance Approved | 0 = No, 1 = Yes |

---

### N12: Reasons Refinance Was Not Granted
**Shown if:** N11 = "No" (Applied for refinance but was denied)

**Question:** "What reason(s) did your lender give for not granting your request to refinance your mortgage? (Select all that apply)"

**Note:** This question was present in early survey waves but removed from later survey administration.

| Original | Descriptive Name | Description | Coding |
|----------|------------------|-------------|--------|
| `N12_1` | `RefiDeniedBadCredit` | Denied: Credit Record Not Good Enough | 0 = Not selected, 1 = Selected |
| `N12_2` | `RefiDeniedIncome` | Denied: Income Not Sufficient | 0 = Not selected, 1 = Selected |
| `N12_3` | `RefiDeniedDocumentation` | Denied: Insufficient Documentation of Income/Assets | 0 = Not selected, 1 = Selected |
| `N12_4` | `RefiDeniedOther` | Denied: Other Reason (Open Text) | 0 = Not selected, 1 = Selected |

---

### N13: Changes in Mortgage Terms After Refinance
**Shown if:** N11 = "Yes" (Refinance was approved)

**Question:** "As a result of refinancing your mortgage, how did the terms of your mortgage change? (Select all that apply)"

**Note:** This question was present in early survey waves but removed from later survey administration.

| Original | Descriptive Name | Description | Coding |
|----------|------------------|-------------|--------|
| `N13_1` | `RefiLowerRate` | Refinance: Interest Rate Was Reduced | 0 = Not selected, 1 = Selected |
| `N13_2` | `RefiHigherBalance` | Refinance: Mortgage Balance Increased (Cashed Out Equity) | 0 = Not selected, 1 = Selected |
| `N13_3` | `RefiLongerTerm` | Refinance: Term of Mortgage Increased (e.g., 15→30 years) | 0 = Not selected, 1 = Selected |
| `N13_4` | `RefiShorterTerm` | Refinance: Term of Mortgage Decreased | 0 = Not selected, 1 = Selected |
| `N13_5` | `RefiAdjToFixed` | Refinance: Changed from Adjustable to Fixed Rate | 0 = Not selected, 1 = Selected |
| `N13_6` | `RefiFixedToAdj` | Refinance: Changed from Fixed to Adjustable Rate | 0 = Not selected, 1 = Selected |
| `N13_7` | `RefiChangedServicer` | Refinance: Changed Mortgage Servicer | 0 = Not selected, 1 = Selected |
| `N13_8` | `RefiOtherChange` | Refinance: Other Change (Open Text) | 0 = Not selected, 1 = Selected |

---

### N14: Changes to Existing Credit
**Note:** Respondent should consider all types of credit: cards, mortgages, home-based loans, auto loans, student loans, and other personal loans

**Question:** "In the past 12 months, did any of the following happen? (Select all that apply)"

| Original | Descriptive Name | Description | Coding |
|----------|------------------|-------------|--------|
| `N14_1` | `ClosedVoluntary` | Voluntarily Closed an Account | 0 = No, 1 = Yes |
| `N14_2` | `ClosedByLender` | Lender Closed an Account | 0 = No, 1 = Yes |
| `N14_3` | `LimitReduced` | Lender Reduced a Credit Limit | 0 = No, 1 = Yes |
| `N14_4` | `NoChanges` | None of the Above | 0 = No, 1 = Yes |

---

### N15-N16: Late Payments

**N15 shown if:** Respondent has at least one type of debt in N1

**N15 Question:** "Over the past 12 months, were you late on any of your loan payments by more than 30 days?"

**N16 shown if:** N15 = "Yes"

**N16 Question:** "Over the past 12 months, were you late on any of your loan payments by more than 90 days?"

| Original | Descriptive Name | Description | Coding |
|----------|------------------|-------------|--------|
| `N15` | `Late30Days` | Any Payments >30 Days Late (Past 12 Months) | 0 = No, 1 = Yes |
| `N16` | `Late90Days` | Any Payments >90 Days Late (Past 12 Months) | 0 = No, 1 = Yes |

---

### N17random: Assignment to Intention Question Format
**Internal routing variable** (not respondent-facing)

This variable determines whether respondents see N17a (Likert scale) or N17b (Probability scale). Respondents are randomly assigned to one of two question formats for measuring future credit intentions.

---

### N17a: Future Credit Intentions (Likert Scale)
**Question format:** One of two possible formats; respondents see **either** N17a **or** N17b

**Question:** "Over the next 12 months, how likely is it that you will do any of the following?"

**Scale:** 1 = Very Unlikely, 2 = Somewhat Unlikely, 3 = Neither Likely nor Unlikely (Neutral), 4 = Somewhat Likely, 5 = Very Likely

| Original | Descriptive Name | Credit Type |
|----------|------------------|-------------|
| `N17a_1` | `IntentionCC` | Apply for Credit Card |
| `N17a_2` | `IntentionMortgage` | Apply for Mortgage/Home-based Loan |
| `N17a_3` | `IntentionAuto` | Apply for Auto Loan |
| `N17a_4` | `IntentionCCLimit` | Request Credit Limit Increase |
| `N17a_5` | `IntentionLoanLimit` | Request Loan Limit Increase |
| `N17a_6` | `IntentionRefi` | Request Mortgage Refinance |
| `N17a_7` | `IntentionStudent` | Apply for Student Loan |

---

### N17b: Future Credit Intentions (Probability)
**Question format:** Alternative to N17a; respondents see **either** N17a **or** N17b

**Question:** "Over the next 12 months, what do you think is the percent chance that you will do any of the following?"

**Response format:** Respondents enter a value from **0 to 100** for each item

| Original | Descriptive Name | Credit Type | Values |
|----------|------------------|-------------|--------|
| `N17b_1` | `ProbCC` | Probability: Apply for Credit Card | 0-100% |
| `N17b_2` | `ProbMortgage` | Probability: Apply for Mortgage/Home Loan | 0-100% |
| `N17b_3` | `ProbAuto` | Probability: Apply for Auto Loan | 0-100% |
| `N17b_4` | `ProbCCLimit` | Probability: Request Credit Limit Increase | 0-100% |
| `N17b_5` | `ProbLoanLimit` | Probability: Request Loan Limit Increase | 0-100% |
| `N17b_6` | `ProbRefi` | Probability: Request Mortgage Refinance | 0-100% |
| `N17b_7` | `ProbStudent` | Probability: Apply for Student Loan | 0-100% |

---

### N18: Reasons for No Future Applications (All Items Low/Zero)
**Shown if:** Respondent indicates very unlikely or low probability for **all** credit items in N17a/N17b

**Question:** "You just said that it is very unlikely that you will apply for any new loans or credit cards, or request any credit limit increases or a refinance in the next 12 months. What is the reason for that? (Select all that apply)"

**Variables:** `N18_1` through `N18_5` (binary indicators, multiple selection allowed)

| Original | Descriptive Name | Description | Coding |
|----------|------------------|-------------|--------|
| `N18_1` | `NoIntentionNoNeed` | No Intention: Satisfied with Current Financial Situation | 0 = Not selected, 1 = Selected |
| `N18_2` | `NoIntentionTimeConsuming` | No Intention: Too Time-Consuming to Apply | 0 = Not selected, 1 = Selected |
| `N18_3` | `NoIntentionDontKnowHow` | No Intention: Don't Know How to Apply | 0 = Not selected, 1 = Selected |
| `N18_4` | `NoIntentionRatesTooHigh` | No Intention: Rates Are Too High | 0 = Not selected, 1 = Selected |
| `N18_5` | `NoIntentionExpectedDenial` | No Intention: Don't Think Would Get Approved | 0 = Not selected, 1 = Selected |

---

### N19: Item-Level Reasons for Low Likelihood (Specific Products)
**Shown for each:** N17a = "Very Unlikely" or N17b < 10% for **specific** credit types

**Question:** For each low-likelihood item: "You indicated it is very unlikely you will [apply for X]. What is the reason for that? (Select all that apply)"

**Variables:** `N19_1` through `N19_5` (binary indicators, multiple selection allowed)

**Note:** These variables apply to each specific credit product where the respondent indicated low likelihood in N17a/N17b.

| Original | Descriptive Name | Description | Coding |
|----------|------------------|-------------|--------|
| `N19_1` | `LowLikelihoodNoNeed` | Low Likelihood: Satisfied with Current Financial Situation | 0 = Not selected, 1 = Selected |
| `N19_2` | `LowLikelihoodTimeConsuming` | Low Likelihood: Too Time-Consuming to Apply | 0 = Not selected, 1 = Selected |
| `N19_3` | `LowLikelihoodDontKnowHow` | Low Likelihood: Don't Know How to Apply | 0 = Not selected, 1 = Selected |
| `N19_4` | `LowLikelihoodRatesTooHigh` | Low Likelihood: Rates Are Too High | 0 = Not selected, 1 = Selected |
| `N19_5` | `LowLikelihoodExpectedDenial` | Low Likelihood: Don't Think Would Get Approved | 0 = Not selected, 1 = Selected |

---

### N20: Expected Future Denial
**Question:** "In the next 12 months, select all types of credit you might need but won't apply for because you think you'll be denied"

| Original | Descriptive Name | Description | Coding |
|----------|------------------|-------------|--------|
| `N20_1` | `ExpectDenialCC` | Expected Denial: Credit Card | 0 = No, 1 = Yes |
| `N20_2` | `ExpectDenialMortgage` | Expected Denial: Mortgage/Home Loan | 0 = No, 1 = Yes |
| `N20_3` | `ExpectDenialAuto` | Expected Denial: Auto Loan | 0 = No, 1 = Yes |
| `N20_4` | `ExpectDenialCCLimit` | Expected Denial: Credit Limit Increase | 0 = No, 1 = Yes |
| `N20_5` | `ExpectDenialLoanLimit` | Expected Denial: Loan Limit Increase | 0 = No, 1 = Yes |
| `N20_6` | `ExpectDenialRefi` | Expected Denial: Mortgage Refinance | 0 = No, 1 = Yes |
| `N20_7` | `ExpectDenialStudent` | Expected Denial: Student Loan | 0 = No, 1 = Yes |
| `N20_8` | `NoExpectedDenial` | None of the Above | 0 = No, 1 = Yes |

---

### N21: Expected Approval Probabilities
**Shown for each:** N17a/N17b indicates positive likelihood of applying  
**Question:** "If you were to apply, what is the percent chance (0-100%) your application would be approved?"

| Original | Descriptive Name | Credit Type | Values |
|----------|------------------|-------------|--------|
| `N21_1` | `ApprovalProbCC` | Expected Approval: Credit Card | 0-100% |
| `N21_2` | `ApprovalProbMortgage` | Expected Approval: Mortgage/Home Loan | 0-100% |
| `N21_3` | `ApprovalProbAuto` | Expected Approval: Auto Loan | 0-100% |
| `N21_4` | `ApprovalProbCCLimit` | Expected Approval: Credit Limit Increase | 0-100% |
| `N21_5` | `ApprovalProbLoanLimit` | Expected Approval: Loan Limit Increase | 0-100% |
| `N21_6` | `ApprovalProbRefi` | Expected Approval: Mortgage Refinance | 0-100% |
| `N21_7` | `ApprovalProbStudent` | Expected Approval: Student Loan | 0-100% |

---

### N22: Self-Reported Credit Score

| Original | Descriptive Name | Description | Coding |
|----------|------------------|-------------|--------|
| `N22` | `CreditScore` | Credit Score Category | 1 = Below 620, 2 = 620-679, 3 = 680-719, 4 = 720-760, 5 = Above 760, 6 = Don't Know |

---

### N23: Last Credit Score Check

| Original | Descriptive Name | Description | Coding |
|----------|------------------|-------------|--------|
| `N23` | `LastScoreCheck` | When Last Checked Credit Score | 1 = Less than 1 month ago, 2 = 1-6 months ago, 3 = 6-12 months ago, 4 = 1-2 years ago, 5 = More than 2 years ago, 6 = Never checked |

---

### N24-N25: Emergency Liquidity Needs

| Original | Descriptive Name | Description | Values |
|----------|------------------|-------------|--------|
| `N24` | `Need2000Prob` | Probability of Needing $2,000 Unexpectedly Next Month | 0-100% |
| `N25` | `Obtain2000Prob` | Probability of Obtaining $2,000 Within Month if Needed | 0-100% |

---

## Data Usage Guidelines

### How to Use This Documentation:

1. **For Individual-Level Analysis:**
   - Use **Microdata File Tab 3 (Data)**
   - 36,277 individual responses
   - All N1-N25 variables available
   - Apply `weight` variable for population estimates

2. **For Time-Series Analysis:**
   - Use **Access-Data File Tab 3 (overall)**
   - Aggregate statistics by survey wave
   - Already weighted for population

3. **For Demographic Analysis:**
   - Use **Access-Data File Tab 4 (demographics)**
   - Breakdowns by age, income, education, etc.

4. **For Variable Definitions:**
   - Reference **Microdata File Tab 4 (Codebook)**
   - Complete value codes and descriptions

### Key Analytic Opportunities:

- **Debt Holding:** N1 variables (binary indicators of possession)
- **Credit Constraints:** N6, N7, N20 (discouraged borrowers)
- **Credit Applications:** N4 (past behavior), N17a/N17b (future intentions)
- **Financial Health:** N22 (credit score), N24/N25 (liquidity)
- **Application Outcomes:** N9 (approval/denial/partial)
- **Balances:** N2 (continuous), N2b (categorical ranges)

---

## Data Attribution

**Source:** Survey of Consumer Expectations, © 2013-2025 Federal Reserve Bank of New York (FRBNY)

The SCE data are available without charge at www.newyorkfed.org and may be used subject to license terms posted there. FRBNY disclaims any responsibility or legal liability for this analysis and interpretation of Survey of Consumer Expectations data.

---

**Document Version:** 2.0  
**Last Updated:** November 2025  
**Total Variables Documented:** 126+
