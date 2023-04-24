import streamlit as st
import pandas as pd
import pickle




def ml():
    data = pd.read_csv("data_fr_streamlit.csv")
    with open("transformer.pkl", "rb") as f:
        transformer = pickle.load(f)
    with open("encoder.pkl", "rb") as f:
        encoder = pickle.load(f)
    with open("knn_model.pkl", "rb") as f:
        knn = pickle.load(f)



    
    
# Ask for user input
    country = st.selectbox("Select your country", data["country"].unique())
    sector = st.selectbox("Select the sector you plan to invest in", data["sector"].unique())
    gender = st.selectbox("Select the gender of the borrower", ["female", "male"])
    num_borrowers = st.slider("How many borrowers are there?", min_value=1, max_value=50)
    repay_interval = st.selectbox("Select the repayment interval which suits you", data["repayment_interval"].unique()) 
    curr = st.selectbox("Select your local currency", data["currency"].unique())
    loan_amount = st.number_input("Enter the loan amount you wish to borrow", min_value=0)

# Preprocess the user input
    user_input = pd.DataFrame({
    "country": [country],
    "sector": [sector],
    "gender_of_borrower": [gender],
    "num_male_borrowers": [num_borrowers] if gender == "male" else [0],
    "num_female_borrowers": [num_borrowers] if gender == "female" else [0],
    "repayment interval" : [repay_interval],
    "local currency" : [curr],
    "loan_amount": [loan_amount]
     })

    user_input_encoded = encoder.transform(user_input).toarray()
    user_input = pd.DataFrame(user_input_encoded, columns=encoder.get_feature_names())
    numerical_cols = data.select_dtypes(include=[int, float]).columns
    user_input[numerical_cols] = transformer.transform(user_input[numerical_cols])

# Make a prediction with the KNN model
    prediction = knn.predict(user_input)[0]
    predicted_loan_amount = transformer.inverse_transform([[prediction]])[0][0]

# Display the prediction
    if predicted_loan_amount <= loan_amount:
        st.write("Your loan application has been **approved**!")
    else:
        st.write(f"Sorry, we cannot approve a loan for the requested amount of {loan_amount:.2f} {curr}. We can approve up to {predicted_loan_amount:.2f} {curr}.")

