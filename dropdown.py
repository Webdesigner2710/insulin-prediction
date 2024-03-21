import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the trained Logistic Regression model
with open('log_model.pkl', 'rb') as file:
    lr_model = pickle.load(file)
    
# Function to get pincode based on store name
def get_pincode(store_name):
    pincode_dict = {
        'NEW GALAXY MEDICAL AND GENERAL STORE': '400104',
        'VINAYAK MEDICAL & GENERAL STORES': '400104',
        'ASHISH MEDICAL & GENERAL STORES': '400104',
        'MEDIWELL CHEMIST': '400104',
        'VIPUL CHEMIST': '400104',
        'GANESH DRUG HOUSE': '400104',
        'IDEAL MEDICAL AND GENERAL STORES': '400104',
        'SHREE CHAMUNDA MEDICAL & GENERAL STORES': '400104',
        'CHHAYA SHREE MEDICAL & GENERAL STORES': '400104',
        'CHEMIST HUB': '400064',
        'NEW DOLLY CHEMIST AND GENERAL STORE': '400064',
        'SAHYOG MEDICAL & GENERAL STORES': '400104',
        'GETWELL CHEMIST': '400104',
        'ARADHANA MEDICAL': '400104',
        'SATGURU MEDICAL': '400064',
        'EVERSHINE MEDICAL AND GENERAL STORES': '400064',
        'SAMRAT MEDICAL & GENERAL STORES': '400063',
        'LUCKY MEDICAL & GENERAL STORES': '400063',
        'MAHAVIR CHEMIST': '400092',
        'POOJA CHEMIST': '400067',
        'NEW ARADHANA MEDICAL AND GENERAL STORES': '400068',
        'GENMART PHARMACY': '400069',
        'MUMBAI CHEMIST & GENERAL STORES': '400068',
        'SHIVTIRTH MEDICAL & GENERAL STORE': '400047',
        'OM MEDICO AND GENERAL STORES': '400068',
        'NEW MATUNGA MEDICAL CENTRE': '400019',
        'NOBLE CHEMIST': '400019',
        'SHIV OM PHARMACY': '400014',
        'MANOJ MEDICAL & GENERAL STORES': '400014',
        'GOLDEN CHEMIST': '400014',
        'NITYANAND MEDICAL & GENERAL STORE': '400031',
        'SAHAKAR CHEMISTS': '400014',
        'MAHARASHTRA MEDICAL STORES': '400031',
        'WADALA MEDICAL AND GENERAL STORES': '400031',
        'GREEN LIFE MEDICAL & GENERAL STORES': '400064',
        'MEDLINE CHEMIST': '400092',
        'PHOENIX MEDICO': '400092',
        'KINJAL MEDICAL & GENERAL STORES': '400099',
        'SUNSHINE MEDICAL & GENERAL STORE': '400056',
        'MEENA MEDICAL & GENERAL STORE': '400056',
        'REAL CHEMIST': '400057',
        'METRO MEDICAL': '400057',
        'CRESCENT DRUG STORE': '400056',
        'PRARTHANA MEDICAL & GENERAL STORE': '400057',
        'GREEN KAMAL MEDICAL & GENERAL STORE': '400058',
        'MAMTA MEDICAL': '400014',
        'SHREE SRINIVASA MEDICAL & GENERAL STORE': '400028',
        'DADAR PHARMACY': '400028'
    }
    return pincode_dict.get(store_name, '')



def get_insulin_details(brand_name):
    insulin_details = {
        'Wosulin': {'Insulin Name': 'Biphasic Isophane Insulin Injection IP', 'Insulin Type': 'intermediate-acting', 'Dosage Strength': '40 IU/mL', 'Price (INR)': 175},
        'LEVEMIR': {'Insulin Name': 'Levemir Flexpen Insulin Detemir Injection', 'Insulin Type': 'long-acting', 'Dosage Strength': '100 IU/mL', 'Price (INR)': 1000},
        'Basalog Refil': {'Insulin Name': 'Insulin Glargine Injection', 'Insulin Type': 'fast-acting', 'Dosage Strength': '100 IU/mL', 'Price (INR)': 480},
        'NovoRapid': {'Insulin Name': 'Insulin aspart IP', 'Insulin Type': 'fast-acting', 'Dosage Strength': '100 IU/mL', 'Price (INR)': 600},
        'HUMARAP': {'Insulin Name': 'Insulin injection IP', 'Insulin Type': 'short-acting', 'Dosage Strength': '40 IU/mL', 'Price (INR)': 178},
        'APIDRA': {'Insulin Name': 'Apidra Insulin Glulisine', 'Insulin Type': 'fast-acting', 'Dosage Strength': '100 IU/mL', 'Price (INR)': 1200},
        'Humapen Ergo': {'Insulin Name': 'Humapen Ergo II', 'Insulin Type': 'intermediate-acting', 'Dosage Strength': '100 IU/mL', 'Price (INR)': 450},
        'LANTUS': {'Insulin Name': 'Lantus Insulin Glargine Injection', 'Insulin Type': 'long-acting', 'Dosage Strength': '100 IU/mL', 'Price (INR)': 500},
        'LUPISULIN N': {'Insulin Name': 'Insulin Injection Isophane  IP', 'Insulin Type': 'intermediate-acting', 'Dosage Strength': '40 IU/mL', 'Price (INR)': 198},
        'Ryzodeg': {'Insulin Name': 'Insulin Degludec Insulin Aspart', 'Insulin Type': 'rapid-acting', 'Dosage Strength': '100 IU/mL', 'Price (INR)': 1500},
        'Humstard 30/70': {'Insulin Name': 'Biphasic Isophane Insulin Injection IP', 'Insulin Type': 'intermediate-acting', 'Dosage Strength': '40 IU/mL', 'Price (INR)': None},
        'Human Actrapid': {'Insulin Name': 'Soluble Insulin Injection I.P.', 'Insulin Type': 'short-acting', 'Dosage Strength': '40 IU/mL', 'Price (INR)': 157}
        
    }
    return insulin_details.get(brand_name, {'Insulin Name': '', 'Insulin Type': '', 'Dosage Strength': '', 'Price (INR)': ''})

store_to_brands = {
    'NEW GALAXY MEDICAL AND GENERAL STORE': ['Human Actrapid', 'LUPISULIN N', 'NovoRapid', 'Ryzodeg'],
    'VINAYAK MEDICAL & GENERAL STORES': ['Fiasp', 'Basalog Refil', 'APIDRA'],
    'ASHISH MEDICAL & GENERAL STORES': ['Wosulin', 'HUMARAP', 'Human Actrapid', 'Ryzodeg', 'LUPISULIN N'],
    'MEDIWELL CHEMIST': ['Wosulin', 'APIDRA', 'NovoRapid', 'LANTUS', 'LEVEMIR', 'Humstard 30/70'],
    'VIPUL CHEMIST': ['Ryzodeg', 'Humstard 30/70', 'Human Actrapid'],
    'GANESH DRUG HOUSE': ['Humapen Ergo', 'LUPISULIN N'],
    'IDEAL MEDICAL AND GENERAL STORES': ['Human Actrapid', 'Basalog Refil', 'LANTUS', 'LEVEMIR'],
    'SHREE CHAMUNDA MEDICAL & GENERAL STORES': ['NovoRapid', 'LUPISULIN N', 'Ryzodeg'],
    'CHHAYA SHREE MEDICAL & GENERAL STORES': ['NovoRapid', 'LANTUS', 'APIDRA', 'LEVEMIR', 'Humapen Ergo', 'Human Actrapid'],
    'CHEMIST HUB': ['HUMARAP'],
    'NEW DOLLY CHEMIST AND GENERAL STORE': ['NovoRapid', 'Humapen Ergo', 'APIDRA', 'LEVEMIR', 'LANTUS', 'Basalog Refil'],
    'SAHYOG MEDICAL & GENERAL STORES': ['HUMARAP', 'LUPISULIN N'],
    'GETWELL CHEMIST': ['Human Actrapid', 'Humstard 30/70', 'Wosulin', 'HUMARAP', 'Ryzodeg', 'Basalog Refil', 'LANTUS', 'NovoRapid',             'LEVEMIR', 'Humapen Ergo'],
    'ARADHANA MEDICAL': ['APIDRA'],
    'SATGURU MEDICAL': ['Basalog Refil', 'LUPISULIN N', 'Wosulin', 'NovoRapid'],
    'EVERSHINE MEDICAL AND GENERAL STORES': ['Ryzodeg', 'Basalog Refil', 'LANTUS', 'Fiasp', 'Wosulin'],
    'SAMRAT MEDICAL & GENERAL STORES': ['HUMARAP'],
    'LUCKY MEDICAL & GENERAL STORES': ['Basalog Refil', 'LEVEMIR'],
    'MAHAVIR CHEMIST': ['Wosulin', 'Basalog Refil', 'LANTUS', 'LEVEMIR', 'NovoRapid'],
    'POOJA CHEMIST': ['Basalog Refil'],
    'NEW ARADHANA MEDICAL AND GENERAL STORES': ['APIDRA', 'Humstard 30/70', 'HUMARAP', 'Wosulin'],
    'GENMART PHARMACY': ['Human Actrapid', 'Fiasp', 'LUPISULIN N', 'Ryzodeg', 'Humapen Ergo', 'Wosulin'],
    'MUMBAI CHEMIST & GENERAL STORES': ['Human Actrapid', 'Basalog Refil', 'LANTUS', 'APIDRA', 'Wosulin', 'Humapen Ergo'],
    'SHIVTIRTH MEDICAL & GENERAL STORE': ['APIDRA', 'Basalog Refil', 'LANTUS', 'LEVEMIR', 'Fiasp', 'Wosulin'],
    'OM MEDICO AND GENERAL STORES': ['LUPISULIN N'],
    'NEW MATUNGA MEDICAL CENTRE': ['Ryzodeg', 'LANTUS', 'NovoRapid', 'Wosulin'],
    'NOBLE CHEMIST': ['APIDRA', 'Basalog Refil', 'Humapen Ergo', 'LUPISULIN N', 'HUMARAP'],
    'SHIV OM PHARMACY': ['LEVEMIR', 'Wosulin', 'HUMARAP'],
    'MANOJ MEDICAL & GENERAL STORES': ['HUMARAP', 'Humstard 30/70'],
    'GOLDEN CHEMIST': ['Fiasp', 'Wosulin', 'Ryzodeg'],
    'NITYANAND MEDICAL & GENERAL STORE': ['Wosulin', 'Humapen Ergo', 'LUPISULIN N'],
    'SAHAKAR CHEMISTS': ['LANTUS', 'LEVEMIR', 'Fiasp', 'Basalog Refil', 'NovoRapid'],
    'MAHARASHTRA MEDICAL STORES': ['HUMARAP', 'Humapen Ergo', 'NovoRapid', 'Ryzodeg'],
    'WADALA MEDICAL AND GENERAL STORES': ['LEVEMIR', 'NovoRapid', 'Fiasp'],
    'GREEN LIFE MEDICAL & GENERAL STORES': ['Human Actrapid', 'LUPISULIN N', 'NovoRapid', 'Ryzodeg'],
    'MEDLINE CHEMIST': ['Fiasp', 'Basalog Refil', 'APIDRA'],
    'PHOENIX MEDICO': ['Wosulin', 'Wosulin', 'HUMARAP', 'Human Actrapid', 'Ryzodeg', 'LUPISULIN N'],
    'SUNSHINE MEDICAL & GENERAL STORE': ['Wosulin', 'APIDRA', 'NovoRapid', 'LANTUS', 'LEVEMIR'],
    'KINJAL MEDICAL & GENERAL STORES': ['Humstard 30/70', 'Ryzodeg', 'Humstard 30/70', 'Human Actrapid'],
    'MEENA MEDICAL & GENERAL STORE': ['Humapen Ergo', 'LUPISULIN N'],
    'REAL CHEMIST': ['Human Actrapid', 'Basalog Refil', 'LANTUS', 'LEVEMIR'],
    'CRESCENT DRUG STORE': ['NovoRapid', 'LUPISULIN N', 'Ryzodeg'],
    'PRARTHANA MEDICAL & GENERAL STORE': ['LANTUS', 'APIDRA', 'LEVEMIR', 'Humapen Ergo'],
    'MAMTA MEDICAL': ['Human Actrapid', 'HUMARAP'],
    'METRO MEDICAL': ['NovoRapid', 'Humapen Ergo', 'APIDRA', 'LEVEMIR', 'LANTUS', 'Basalog Refil'],
    'GREEN KAMAL MEDICAL & GENERAL STORE': ['HUMARAP', 'LUPISULIN N'],
    'DADAR PHARMACY': ['Human Actrapid', 'Humstard 30/70', 'Wosulin', 'HUMARAP', 'Ryzodeg', 'Wosulin'],
    'SHREE SRINIVASA MEDICAL & GENERAL STORE': ['NovoRapid', 'LEVEMIR', 'Humapen Ergo', 'APIDRA']
}

# Streamlit app
def main():
    # HTML for gradient background and styling
    st.markdown("""
    <style>
    .reportview-container {
        background: linear-gradient(to right, #ff99ff 0%, #99ccff 100%);
        color: white;
        font-size: 16px;
    }      
    .widget-dropdown > div[role="button"] {
        background-color: white;
        color: black;
    }
    .widget button[data-baseweb="button"] {
        background-color: #004080;
        color: white;
    }
    .stButton>button {
        background-color: #FF0000;
        color: white;
    }
    .warning-box {
        color: black !important;
        background-color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # Title
    st.title('Insulin Stock Prediction')

    # Input fields
    st.write('Enter the following details:')

    # Dropdown options for each feature
    store_names = [
        'NEW GALAXY MEDICAL AND GENERAL STORE',
        'VINAYAK MEDICAL & GENERAL STORES',
        'ASHISH MEDICAL & GENERAL STORES',
        'MEDIWELL CHEMIST',
        'VIPUL CHEMIST',
        'GANESH DRUG HOUSE',
        'IDEAL MEDICAL AND GENERAL STORES',
        'SHREE CHAMUNDA MEDICAL & GENERAL STORES',
        'CHHAYA SHREE MEDICAL & GENERAL STORES',
        'CHEMIST HUB',
        'NEW DOLLY CHEMIST AND GENERAL STORE',
        'SAHYOG MEDICAL & GENERAL STORES',
        'GETWELL CHEMIST',
        'ARADHANA MEDICAL',
        'SATGURU MEDICAL',
        'EVERSHINE MEDICAL AND GENERAL STORES',
        'SAMRAT MEDICAL & GENERAL STORES',
        'LUCKY MEDICAL & GENERAL STORES',
        'MAHAVIR CHEMIST',
        'POOJA CHEMIST',
        'NEW ARADHANA MEDICAL AND GENERAL STORES',
        'GENMART PHARMACY',
        'MUMBAI CHEMIST & GENERAL STORES',
        'SHIVTIRTH MEDICAL & GENERAL STORE',
        'OM MEDICO AND GENERAL STORES',
        'NEW MATUNGA MEDICAL CENTRE',
        'NOBLE CHEMIST',
        'SHIV OM PHARMACY',
        'MANOJ MEDICAL & GENERAL STORES',
        'GOLDEN CHEMIST',
        'NITYANAND MEDICAL & GENERAL STORE',
        'SAHAKAR CHEMISTS',
        'MAHARASHTRA MEDICAL STORES',
        'WADALA MEDICAL AND GENERAL STORES',
        'GREEN LIFE MEDICAL & GENERAL STORES',
        'MEDLINE CHEMIST',
        'PHOENIX MEDICO',
        'KINJAL MEDICAL & GENERAL STORES',
        'SUNSHINE MEDICAL & GENERAL STORE',
        'MEENA MEDICAL & GENERAL STORE',
        'REAL CHEMIST',
        'METRO MEDICAL',
        'CRESCENT DRUG STORE',
        'PRARTHANA MEDICAL & GENERAL STORE',
        'GREEN KAMAL MEDICAL & GENERAL STORE',
        'MAMTA MEDICAL',
        'SHREE SRINIVASA MEDICAL & GENERAL STORE',
        'DADAR PHARMACY'
    ]

    store_name = st.selectbox('Store Name', store_names)
    pincode = get_pincode(store_name)
    st.write('Store Pincode:', pincode)

    # Dropdown options for brand name
    brand_names = [
        'Wosulin', 'LEVEMIR', 'Basalog Refil', 'NovoRapid', 'HUMARAP', 'APIDRA', 'Humapen Ergo', 'LANTUS',
        'LUPISULIN N', 'Ryzodeg', 'Humstard 30/70', 'Human Actrapid'
    ]
    brand_name = st.selectbox('Brand Name', brand_names)

    if brand_name not in store_to_brands.get(store_name, []):
        st.warning("Selected brand is not available in this store.")
    else:
        st.success("Selected brand is available in this store.")
        
    insulin_details = get_insulin_details(brand_name)  # Retrieve insulin details based on brand name
    insulin_name = insulin_details['Insulin Name']
    insulin_type = insulin_details['Insulin Type']
    dosage_strength = insulin_details['Dosage Strength']
    price = insulin_details['Price (INR)']

    # Display insulin details
    st.write('Insulin Name:', insulin_details.get('Insulin Name', ''))
    st.write('Insulin Type:', insulin_details.get('Insulin Type', ''))

    # Dropdown options for dosage strength
    dosage_strengths = ['100', '40']
    dosage_strength = st.selectbox('Dosage Strength', dosage_strengths)

    # Display price based on selected brand name
    st.write('Price (INR):', insulin_details.get('Price (INR)', ''))
    
    # Make prediction on button click
    if st.button('Predict'):
        # If selected brand is not available in the selected store
        if brand_name not in store_to_brands.get(store_name, []):
            st.warning("Selected brand is not available in this store. Predicted Insulin Stock: 0")
        else:
            # Convert input data to DataFrame
            input_data = pd.DataFrame({
                'Store Name': [store_name],
                'Store Pincode': [pincode],
                'Brand Name': [brand_name],
                'Insulin Name': [insulin_name],
                'Insulin Type': [insulin_type],
                'Dosage Strength': [dosage_strength],
                'Price (INR)': [price]
            })

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