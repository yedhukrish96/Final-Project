import streamlit as st
import pandas as pd
import pickle




def ml():
    data = pd.read_csv("final_df_forml.csv")
    with open("scaler.pkl", "rb") as f:
        transformer = pickle.load(f)
    with open("encoder.pkl", "rb") as f:
        encoder = pickle.load(f)
    with open("knn_model.pkl", "rb") as f:
        knn = pickle.load(f)



    
 # Ask for user input
    loan_amount = st.number_input("Select the loan amount you wish to borrow", max_value=150000,value=0)
    country = st.selectbox("Select your country", ['0'] + data["country"].unique().tolist(), index=0)     #Select your country", data["country"].unique(),index=1)
    sector = st.selectbox("Select the sector you plan to invest in",['0'] + data["sector"].unique().tolist(),index=0)
    curr = st.selectbox("Select your local currency",['0']+ data["currency"].unique().tolist(),index=0)
    term = st.selectbox("Select the repayment term in months",['0']+ data["term_in_months"].unique().tolist(),index=0)
    lender_count = st.slider("How many lenders should contribute to the loan?", min_value=1, max_value=100)
    repay_interval = st.selectbox("Select the repayment interval which suits you",['0']+ data["repayment_interval"].unique().tolist(),index=0)
    posted_year = st.selectbox("Select the year in which you posted the request",['0']+ data["posted_year"].unique().tolist(),index=0)
    posted_month = st.selectbox("Select the month in which the loan was posted",['0']+ data["posted_month"].unique().tolist(),index=0)
    disbursed_year = st.selectbox("Select the year in which you wish the loan to be disbursed",['0']+ data["disbursed_year"].unique().tolist(),index=0)
    disbursed_month = st.selectbox("Select the month in which the loan is to be disbursed",['0']+ data["disbursed_month"].unique().tolist(),index=0)
    num_male_borrowers = st.slider("How many male borrowers are there?", min_value=0, max_value=50)
    num_female_borrowers = st.slider("How many female borrowers are there?", min_value=0, max_value=50)
    mode_gender_of_borrower = st.selectbox("Select the gender of the main borrower",['0']+ data["mode_gender_of_borrower"].unique().tolist(),index=0)

# Preprocess the user input
    user_input = pd.DataFrame({
    "loan_amount": [loan_amount],    
    "country": [country],
    "sector": [sector],
    "currency": [curr],
    "term_in_months": [term],
    "lender_count": [lender_count],
    "repayment_interval": [repay_interval],
    "posted_year": [posted_year],
    "posted_month": [posted_month],
    "disbursed_year": [disbursed_year],
    "disbursed_month": [disbursed_month],
    "num_male_borrowers": [num_male_borrowers],
    "num_female_borrowers": [num_female_borrowers],
    "mode_gender_of_borrower": [mode_gender_of_borrower]
})


    categorical_cols = user_input[['sector', 'country', 'currency', 'repayment_interval', 'posted_year',
       'posted_month', 'disbursed_year', 'disbursed_month',
       'mode_gender_of_borrower']].astype('str')
    cols = encoder.get_feature_names_out(categorical_cols.columns)
    categorical_encoded = pd.DataFrame(encoder.transform(categorical_cols).toarray(),columns=cols)
    
   
    numerical_cols = user_input[['term_in_months', 'lender_count', 'num_male_borrowers',
       'num_female_borrowers']]
    numericals_scaled = transformer.transform(numerical_cols)
    numericals_scaled = pd.DataFrame(numericals_scaled,columns=numerical_cols.columns)
    user_input1 = pd.concat([numericals_scaled,categorical_encoded],axis=1)

# Make a prediction with the KNN model
    predicted_loan_amount = knn.predict(user_input1)[0]
   
    # Display the prediction
    predicted_loan_amount = int(predicted_loan_amount) # converting to integer
    #st.write(predicted_loan_amount)

# Check if loan is granted or not
    loan_amount_input = int(loan_amount)
    if loan_amount_input <= predicted_loan_amount:
         st.write("Congratulations! Your loan has been granted.")
    else:
        st.write("Loan cannot be granted. You can ask for a loan up to", predicted_loan_amount, "amount.")


# Display the prediction
    #st.write(str(predicted_loan_amount))

