import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt

st.title("📊 Model Performance Dashboard")

# ==============================
# 📁 PATH SETUP (VERY IMPORTANT)
# ==============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "model.pkl")



# ==============================
# 📂 LOAD DATA
# ==============================
try:
    df = pd.read_csv("emi_prediction_dataset.csv")
    st.success("Dataset Loaded ✅")
except Exception as e:
    st.error(f"Dataset not found ❌ {e}")
    st.stop()

# ==============================
# 🤖 LOAD MODEL
# ==============================
try:
    model = pickle.load(open(model_path, "rb"))
    st.success("Model Loaded ✅")
except Exception as e:
    st.error(f"Model not found ❌ {e}")
    st.stop()

# ==============================
# 🧹 DATA CLEANING (FIX YOUR ERRORS)
# ==============================
num_cols = ['monthly_salary', 'credit_score', 'current_emi_amount']

for col in num_cols:
    df[col] = df[col].astype(str).str.extract(r'(\d+\.?\d*)')[0]
    df[col] = pd.to_numeric(df[col], errors='coerce')

df = df.dropna()

# ==============================
# 🎯 FEATURES & TARGET
# ==============================
X = df[['monthly_salary', 'credit_score', 'current_emi_amount']]
y = df['emi_eligibility']

# Convert target if needed
if y.dtype == 'object':
    y = y.map({'Yes': 1, 'No': 0})

# ==============================
# 🔮 PREDICTIONS
# ==============================
y_pred = model.predict(X)

# ==============================
# 📊 METRICS
# ==============================
st.subheader("📈 Model Metrics")

acc = accuracy_score(y, y_pred)
prec = precision_score(y, y_pred)
rec = recall_score(y, y_pred)
f1 = f1_score(y, y_pred)

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
    st.metric("Accuracy", f"{acc:.2f}")

with col2:
    st.metric("Precision", f"{prec:.2f}")

with col3:
    st.metric("Recall", f"{rec:.2f}")

with col4:
    st.metric("F1 Score", f"{f1:.2f}")

# ==============================
# 📉 VISUALIZATION
# ==============================
st.subheader("📊 Prediction Distribution")

fig, ax = plt.subplots()
ax.hist(y_pred)
ax.set_title("Prediction Output Distribution")
st.pyplot(fig)

# ==============================
# 📊 DATA PREVIEW
# ==============================
st.subheader("📄 Sample Data")
st.dataframe(df.head())