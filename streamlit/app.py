import streamlit as st, pandas as pd, os
st.title('Customer 360 — Churn Scoring Demo')
if os.path.exists('../ml/scores.csv'):
    df = pd.read_csv('../ml/scores.csv')
    st.dataframe(df.head())
else:
    st.write('No scores found. Run ML scoring to generate ml/scores.csv')
