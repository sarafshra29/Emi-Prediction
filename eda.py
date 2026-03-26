import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.title("📊 Exploratory Data Analysis (EDA)")

# ======================
# PATH FIX
# ======================
BASE_DIR = os.path.dirname(os.path.abspath("emi_prediction_dataset.csv"))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, ".."))

csv_path = os.path.join(PROJECT_ROOT, "emi_prediction_dataset.csv")

st.write("Reading file from:", csv_path)  # DEBUG

# ======================
# LOAD DATA
# ======================
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
    st.success("Dataset Loaded ✅")
else:
    st.error("Dataset NOT found ❌")
    st.stop()

# ======================
# SHOW DATA
# ======================
st.subheader("📄 Dataset Preview")
st.dataframe(df.head())

st.write("Shape:", df.shape)

# ======================
# CLEAN DATA (IMPORTANT)
# ======================
num_cols = ['monthly_salary', 'credit_score', 'current_emi_amount']

for col in num_cols:
    df[col] = df[col].astype(str).str.extract(r'(\d+\.?\d*)')[0]
    df[col] = pd.to_numeric(df[col], errors='coerce')

# ⚠️ Don't drop all data blindly
df = df.dropna(subset=num_cols)

st.write("After cleaning shape:", df.shape)

# ======================
# PLOT 1: EMI ELIGIBILITY
# ======================
st.subheader("📊 EMI Eligibility Distribution")

fig1, ax1 = plt.subplots()
sns.countplot(x='emi_eligibility', data=df, ax=ax1)
st.pyplot(fig1)

# ======================
# PLOT 2: SALARY DISTRIBUTION
# ======================
st.subheader("💰 Salary Distribution")

fig2, ax2 = plt.subplots()
sns.histplot(df['monthly_salary'], kde=True, ax=ax2)
st.pyplot(fig2)

# ======================
# PLOT 3: CORRELATION
# ======================
st.subheader("🔗 Correlation Matrix")

fig3, ax3 = plt.subplots()

corr = df[num_cols].corr()
sns.heatmap(corr, annot=True, ax=ax3)

st.pyplot(fig3)