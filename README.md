This project is an end-to-end Machine Learning and Data Analytics application that predicts loan EMI eligibility and estimates the maximum EMI amount a customer can afford based on financial and demographic data.

The system combines data preprocessing, feature engineering, exploratory data analysis (EDA), machine learning models, and interactive dashboards to deliver real-time insights and predictions.

A multi-page web application is built using Streamlit, allowing users to explore data, evaluate model performance, and make live predictions.

🚀 Key Features
📊 Exploratory Data Analysis (EDA)
Distribution analysis of EMI eligibility
Correlation between financial variables
Demographic and risk pattern insights
⚙️ Feature Engineering
Debt-to-Income ratio
Expense-to-Income ratio
Financial risk indicators

🤖 Machine Learning Models
Classification (EMI Eligibility)

Logistic Regression
Random Forest Classifier
XGBoost Classifier

Regression (EMI Amount Prediction)

Linear Regression
Random Forest Regressor
XGBoost Regressor
📈 Model Evaluation Metrics
Accuracy, Precision, Recall, F1-score
RMSE, MAE, R² Score
🧠 Experiment Tracking
Integrated with MLflow
Tracks model parameters, metrics, and performance
🌐 Interactive Dashboard
Multi-page app using Streamlit
Real-time prediction interface
Data visualization & model insights
🛠️ Tech Stack
Python
Pandas, NumPy
Scikit-learn
XGBoost
Matplotlib, Seaborn
Streamlit
MLflow
Git & GitHub
📂 Project Structure
emi-project/
│
├── app.py
├── pages/
├── model.pkl
├── emi_prediction_dataset.csv
├── requirements.txt
└── README.md
