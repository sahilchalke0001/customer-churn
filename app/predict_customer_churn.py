import streamlit as st
import pandas as pd
import pickle
import io

# Load model, encoders, and scaler
with open('model/best_model.pkl', 'rb') as model_file:
    loaded_model = pickle.load(model_file)
with open('model/encoder.pkl', 'rb') as encoders_file:
    encoders = pickle.load(encoders_file)
with open('model/scaler.pkl', 'rb') as scaler_file:
    scaler_data = pickle.load(scaler_file)

def run():
    # Your function logic here for predicting customer churn
    st.title("Customer Churn Prediction")
    
    # Function to make a prediction
    def make_prediction(input_data):
        input_df = pd.DataFrame([input_data])  # Indented correctly

        # Apply transformations to the input data
        for col, encoder in encoders.items():
            input_df[col] = encoder.transform(input_df[col])

        # Scaling numerical columns
        numerical_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
        input_df[numerical_cols] = scaler_data.transform(input_df[numerical_cols])

        # Prediction
        prediction = loaded_model.predict(input_df)[0]
        probability = loaded_model.predict_proba(input_df)[0, 1]
        
        # Return result
        return "Churn" if prediction == 1 else "No Churn", probability

    # Create input form with three columns
    col1, col2, col3 = st.columns(3)

    with col1:
        gender = st.selectbox('Gender', ['Male', 'Female'])
        SeniorCitizen = st.selectbox('Senior Citizen', [0, 1])
        Partner = st.selectbox('Partner', ['Yes', 'No'])
        Dependents = st.selectbox('Dependents', ['Yes', 'No'])
        tenure = st.number_input('Tenure (months)', min_value=0, max_value=72)
        PaperlessBilling = st.selectbox('Paperless Billing', ['Yes', 'No'])

    with col2:
        PhoneService = st.selectbox('Phone Service', ['Yes', 'No'])
        MultipleLines = st.selectbox('Multiple Lines', ['Yes', 'No', 'No phone service'])
        InternetService = st.selectbox('Internet Service', ['DSL', 'Fiber optic', 'No'])
        OnlineSecurity = st.selectbox('Online Security', ['Yes', 'No', 'No internet service'])
        OnlineBackup = st.selectbox('Online Backup', ['Yes', 'No', 'No internet service'])
        PaymentMethod = st.selectbox('Payment Method', ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])
        TotalCharges = st.number_input('Total Charges', min_value=0.0, step=0.1)

    with col3:
        DeviceProtection = st.selectbox('Device Protection', ['Yes', 'No', 'No internet service'])
        TechSupport = st.selectbox('Tech Support', ['Yes', 'No', 'No internet service'])
        StreamingTV = st.selectbox('Streaming TV', ['Yes', 'No', 'No internet service'])
        StreamingMovies = st.selectbox('Streaming Movies', ['Yes', 'No', 'No internet service'])
        Contract = st.selectbox('Contract', ['Month-to-month', 'One year', 'Two year'])
        MonthlyCharges = st.number_input('Monthly Charges', min_value=0.0, step=0.1)

    st.markdown(
        f"""
        <style>
            .stApp {{
                background-image: url('https://miro.medium.com/v2/resize:fit:2000/1*uScC9YN6GIXG1agVI0XFpA.png');
                background-size: cover;
            }}
            p {{
                background-color: #E0115F;
                color: black;
                font-weight: bold;
                text-align: center;
                display: block;
            }}
            h3,li,h1 {{
            color: #E52B50;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Create the dictionary with input data
    input_data = {
        'gender': gender,
        'SeniorCitizen': SeniorCitizen,
        'Partner': Partner,
        'Dependents': Dependents,
        'tenure': tenure,
        'PhoneService': PhoneService,
        'MultipleLines': MultipleLines,
        'InternetService': InternetService,
        'OnlineSecurity': OnlineSecurity,
        'OnlineBackup': OnlineBackup,
        'DeviceProtection': DeviceProtection,
        'TechSupport': TechSupport,
        'StreamingTV': StreamingTV,
        'StreamingMovies': StreamingMovies,
        'Contract': Contract,
        'PaperlessBilling': PaperlessBilling,
        'PaymentMethod': PaymentMethod,
        'MonthlyCharges': MonthlyCharges,
        'TotalCharges': TotalCharges,
    }

    # Create a button for prediction
    col1, col2, col3 = st.columns(3)

    with col2:
        if st.button("Predict Churn"):
            prediction, probability = make_prediction(input_data)

            # Display results
            st.subheader("Prediction")
            st.write(f"**{prediction}**")
            st.write(f"Probability of churn: **{probability:.2f}**")

            # Prepare a report for download
            report = f"""
            Customer Data:
            Gender: {gender}
            Senior Citizen: {SeniorCitizen}
            Partner: {Partner}
            Dependents: {Dependents}
            Tenure (months): {tenure}
            Phone Service: {PhoneService}
            Multiple Lines: {MultipleLines}
            Internet Service: {InternetService}
            Online Security: {OnlineSecurity}
            Online Backup: {OnlineBackup}
            Device Protection: {DeviceProtection}
            Tech Support: {TechSupport}
            Streaming TV: {StreamingTV}
            Streaming Movies: {StreamingMovies}
            Contract: {Contract}
            Paperless Billing: {PaperlessBilling}
            Payment Method: {PaymentMethod}
            Monthly Charges: {MonthlyCharges}
            Total Charges: {TotalCharges}

            Prediction: {prediction}
            Churn Probability: {probability:.2f}
            """

            report_txt = io.StringIO(report)

            # Add a download button
            st.download_button(
                label="Download Report",
                data=report_txt.getvalue(),
                file_name="churn_prediction_report.txt",
                mime="text/plain"
            )
