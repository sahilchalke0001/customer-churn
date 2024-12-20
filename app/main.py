import streamlit as st

# Set page config at the very beginning
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="chart_with_upwards_trend",
)

# Main Page Title
st.subheader(".....")

# Description
st.write("""
Welcome to the Customer Insights Application! 
Here you can:
- Predict customer churn to identify at-risk customers and reduce attrition.
- Analyze customer reviews to gain valuable insights into customer sentiment and feedback.

Select a function below to get started.
""")

# Add Navigation Buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("Predict Customer Churn"):
        st.session_state.page = "predict_customer_churn"  # Use session state to manage page
        st.write("Customer Churn Prediction page...")

with col2:
    if st.button("Analyze Customer Reviews"):
        st.session_state.page = "analyze_customer_reviews"  # Use session state to manage page
        st.write("Customer Review Analysis page...")

# Read page parameter from session_state or set to "home" if not defined
page = st.session_state.get("page", "home")  # Default to 'home' if no page set

if page == "predict_customer_churn":
    import predict_customer_churn
    predict_customer_churn.run()  # Call a function in the file to display its content
# elif page == "analyze_customer_reviews":
#     import analyze_customer_reviews
#     analyze_customer_reviews.run()  # Call a function in the file to display its content
else:
    st.write("Welcome to the Customer Insights Application!")
    st.write("Select a feature from the buttons above.")

# Footer
st.markdown("---")
st.write("For assistance or feedback, contact our support team.")

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

