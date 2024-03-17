import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the trained Logistic Regression model
with open('log_model.pkl', 'rb') as file:
    lr_model = pickle.load(file)

# Streamlit app
def main():
    # HTML for gradient background
    st.markdown("""
    <style>
    .reportview-container {
        background: linear-gradient(to right, #FF512F, #DD2476);
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

    # Title
    st.title('Insulin Stock Prediction')

    # Input fields
    st.write('Enter the following details:')

    # Example: assuming you have 8 features
    feature_names = ['Store Name', 'Store Pincode', 'Brand Name', 'Insulin Name',
                     'Insulin Type', 'Dosage Strength', 'Price (INR)']

    features = {}
    for name in feature_names:
        # For categorical text features, use text input
        if name in ['Store Name', 'Brand Name', 'Insulin Name', 'Insulin Type']:
            features[name] = st.text_input(label=name)
        # For numerical features, parse the float values from the input string
        else:
            value = st.text_input(label=name)
            try:
                features[name] = float(value) if value else None
            except ValueError:
                st.error(f'Invalid input for {name}. Please enter a numeric value.')

    # Make prediction on button click
    if st.button('Predict'):
        # Convert input data to DataFrame
        input_data = pd.DataFrame([features])

        # Perform label encoding for categorical text features
        categorical_features = ['Store Name', 'Brand Name', 'Insulin Name', 'Insulin Type']
        label_encoders = {}  # Dictionary to store label encoders for each categorical feature
        for feature in categorical_features:
            # Initialize label encoder for the feature
            label_encoders[feature] = LabelEncoder()
            # Fit label encoder and transform the feature
            input_data[feature] = label_encoders[feature].fit_transform(input_data[feature])

        # Make prediction
        prediction = lr_model.predict(input_data)
        # Display prediction
        st.write('Predicted Insulin Stock:', prediction[0])

if __name__ == '__main__':
    main()
