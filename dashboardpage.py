# pages/1_📊_Dashboard.py

import streamlit as st
import pandas as pd

df = pd.read_csv("emi_prediction_dataset.csv")

st.title("📊 Executive Dashboard")

col1, col2, col3 = st.columns(3)

col1.metric("Total Customers", len(df))
col2.metric("Avg Salary", int(df['monthly_salary'].mean()))
col3.metric("Avg EMI", int(df['max_monthly_emi'].mean()))

st.bar_chart(df['emi_eligibility'].value_counts())

st.bar_chart(df['max_monthly_emi'].value_counts())

st.bar_chart(df['monthly_salary'].value_counts())

import pandas as pd
import streamlit as st

df = pd.read_csv("emi_prediction_dataset.csv")

# ======================
# CLEAN NUMERIC COLUMNS
# ======================
num_cols = [
    'monthly_salary',
    'credit_score',
    'current_emi_amount',
    'groceries_utilities',
    'other_monthly_expenses'
]

for col in num_cols:
    df[col] = df[col].astype(str)

    # Fix double decimal issue
    df[col] = df[col].str.replace(r'(\d+)\.(\d+)\.(\d+)', r'\1.\2', regex=True)

    # Remove symbols like ₹, commas
    df[col] = df[col].str.replace(r'[^\d.]', '', regex=True)

    df[col] = pd.to_numeric(df[col], errors='coerce')

# ======================
# HANDLE MISSING VALUES
# ======================
df[num_cols] = df[num_cols].fillna(df[num_cols].median())