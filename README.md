# 📱 Telco Customer Churn Prediction & Streamlit App

An end-to-end Machine Learning project that identifies at-risk telecom customers and provides an interactive dashboard for real-time churn risk assessment.

## 🚀 Live Demo
https://telco-customer-churn-prediction-emhwsp6sxvdi4eajtetwvu.streamlit.app/

---

## 📊 Project Overview
* **The Problem:** Customer churn is costing telecom companies millions annually. The goal of this project is to predict which customers are highly likely to cancel their service so proactive retention strategies can be applied.
* **The Data:** IBM Telco Customer Churn dataset, analyzing customer demographics, account details, and subscribed services.
* **Key Insight:** Customers on **Month-to-month contracts** with high monthly charges are the most significant drivers of churn.

---

## 🛠️ Machine Learning Pipeline & Challenges

### 1. Data Processing & Feature Engineering
* Handled missing/blank values in the `TotalCharges` column and cast them to numeric.
* Converted categorical variables into numerical values using **One-Hot Encoding** (`pd.get_dummies()`).

### 2. The Class Imbalance Challenge
The dataset suffered from a heavy class imbalance with a **3:1 ratio** of loyal customers (`False`) to churned customers (`True`). 
* **Baseline Logistic Regression:** Achieved 79% overall accuracy, but a poor **Recall of 51%** for churners—meaning it missed half the customers who actually left.
* **The Optimization:** Implemented a **Balanced Logistic Regression** model (`class_weight='balanced'`). This successfully boosted **Recall to 80%**, allowing the business to catch the vast majority of at-risk users while maintaining a balanced precision-recall trade-off.

### 📊 Model Performance Comparison

| Model Configuration | Overall Accuracy | Churn Recall (True) | Churn Precision (True) |
| :--- | :---: | :---: | :---: |
| Baseline Logistic Regression | 79% | 51% | 62% |
| **Balanced Logistic Regression (Final)** | **73%** | **80%** | **50%** |
| Random Forest (Balanced) | 78% | 45% | 63% |

*Decision Strategy:* Random Forest proved too conservative for this business use-case (missing 55% of churners). Logistic Regression with balanced class weights was chosen for deployment because the cost of an automated retention offer (False Positive) is significantly lower than losing a customer entirely (False Negative).

---

## 💻 How to Run the App Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/AryanNeolia/telco-customer-churn-prediction.git](https://github.com/AryanNeolia/telco-customer-churn-prediction.git)
   cd telco-customer-churn-prediction
