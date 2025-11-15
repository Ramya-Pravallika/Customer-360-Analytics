# 📊 Enterprise Customer 360 Analytics Platform  
**SQL | Python | Snowflake | dbt | Power BI | Streamlit | Machine Learning**

A complete **end-to-end Customer 360 Analytics & Churn Prediction Platform**, powered by modern data stack tools.  
This project demonstrates how an enterprise SaaS company can unify CRM, product usage, billing, support, and NPS data into a single analytical layer — then apply machine learning to predict churn and drive retention.

---

# 🚀 Project Overview

This repository contains an **end-to-end enterprise analytics project** that includes:

### ✔️ Data Engineering  
- Synthetic datasets representing CRM, product usage, support, NPS, and revenue  
- Snowflake warehouse setup  
- dbt transformations (staging + marts)  
- Dimensional modeling (Kimball)  
- Daily account metrics & feature engineering  

### ✔️ Machine Learning  
- Python churn prediction model (XGBoost)  
- Account-level churn probability  
- SHAP explainability  
- Score outputs for dashboards & CSM consumption  

### ✔️ Analytics & BI  
- Power BI dashboards (DAX samples + report guidance)  
- Customer Health view  
- Churn Trend Analyzer  
- Revenue & Upsell predictions  
- Executive overview dashboards  

### ✔️ App Layer  
- Streamlit demo app for interactively exploring churn risk and account insights  

### ✔️ Production-Ready Engineering  
- Clear repo structure  
- Reproducible synthetic data generator  
- GitHub Actions CI pipeline (sample)

---

# 🏗️ Architecture

    ┌──────────────────────┐
    │   Operational Data    │
    │ CRM • Usage • Support │
    │ NPS • Billing         │
    └───────────┬──────────┘
                │ Raw Data
                ▼
    ┌──────────────────────┐
    │   Snowflake RAW      │
    └───────────┬──────────┘
                │ dbt staging
                ▼
    ┌──────────────────────┐
    │   dbt MODELS         │
    │ staging → marts      │
    └───────────┬──────────┘
                │ Analytics tables
                ▼
    ┌──────────────────────┐
    │   ML Features        │
    │ XGBoost Churn Model  │
    │ SHAP Explainability  │
    └───────────┬──────────┘
                │ Scores
                ▼
    ┌──────────────────────┐
    │ Power BI Dashboards  │
    │ Streamlit App        │
    └──────────────────────┘
