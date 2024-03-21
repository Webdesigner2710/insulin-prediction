import streamlit as st
import pandas as pd

# Load data
def load_data():
    return pd.read_excel('insulin information.xlsx')

store_data = load_data()

# Streamlit app
def main():
    # HTML for gradient background
    st.markdown("""
        <style>
        .reportview-container {
            background: linear-gradient(to right, #4ca1af, #c4e0e5);
            color: black;
        }
        table.dataframe {
            width: 100%;
        }
        </style>
        """, unsafe_allow_html=True)

    # Title
    st.title('Store Information by Pincode')

    # Sidebar - Pincode input with default values
    default_pincodes = ['400104', '400064', '400063', '400092', '400067', '400068', '400069', '400047','400019', '400014', '400031', '400056', '400099', '400057', '400058', '400028']  # Example default pincodes
    pincode = st.sidebar.selectbox("Select Store Pincode", default_pincodes)

    # Convert pincode to integer for comparison
    pincode = int(pincode)

    # Filter data based on pincode
    filtered_data = store_data[store_data['Store Pincode'] == pincode]

    # Display filtered data
    if not filtered_data.empty:
        st.subheader(f'Store Information for Pincode {pincode}:')
        # Display selected columns: Store Name, Brand Name, Insulin Name, Insulin Type, Price, and Quantity Available
        st.dataframe(filtered_data[['Store Name', 'Brand Name', 'Insulin Name', 'Insulin Type', 'Price (INR)', 'Quantity available']])
    else:
        st.write(f"No store found for the pincode '{pincode}'.")

if __name__ == '__main__':
    main()