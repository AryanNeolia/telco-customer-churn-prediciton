import streamlit as st
import pandas as pd 
import pickle

st.title("Telecom Customer Churn Predictor")
st.write("Input a customer's details below to check their risk of leaving")

@st.cache_resource

def load_model():
    with open('balanced_model.pkl' ,'rb')as file:
        return pickle.load(file)

model =load_model()

st.subheader("Customer Demographics & Plan Details")

contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])

monthly_charges = st.number_input("Monthly Charges ($)", min_value=0.0, max_value=200.0, value=50.0)
total_charges = st.number_input("Total Charges ($)", min_value=0.0, max_value=10000.0, value=500.0)
tenure = st.slider("Tenure (Months with company)", min_value=0, max_value=72, value=12)


if st.button("Predict Churn Risk"):
    
    
    input_data = {
        'tenure': [tenure],
        'MonthlyCharges': [monthly_charges],
        'TotalCharges': [total_charges],
        'Contract_One year': [1 if contract == "One year" else 0],
        'Contract_Two year': [1 if contract == "Two year" else 0]
    }
    
    
    feature_names = model.feature_names_in_
    
    
    input_df = pd.DataFrame(0, index=[0], columns=feature_names)
    
    
    for key, val in input_data.items():
        if key in input_df.columns:
            input_df[key] = val

    
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1] 

    st.markdown("---")
    if prediction == 1:
        st.error(f"🚨 **High Risk Alert!** This customer is highly likely to churn. (Probability: {probability*100:.1f}%)")
    else:
        st.success(f"✅ **Safe!** This customer is likely to stay loyal. (Probability of churn: {probability*100:.1f}%)")