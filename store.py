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
    st.title('Store Locator')

    # Sidebar - Brand Name input
    brand_name = st.sidebar.text_input("Enter Brand Name")

    # Filter data based on brand name
    filtered_data = store_data[store_data['Brand Name'] == brand_name]
    # Convert 'Store Pincode' column to string type
    store_data['Store Pincode'] = store_data['Store Pincode'].astype(str)

    # Remove commas from the 'Store Pincode' column
    store_data['Store Pincode'] = store_data['Store Pincode'].str.replace(',', '')
    # Display filtered data
    if not filtered_data.empty:
        st.subheader(f'Stores selling {brand_name}:')
        # Display Store Name, Pincode, Address, Insulin Type, Price, and Quantity Available
        st.dataframe(filtered_data[['Store Name', 'Address', 'Store Pincode', 'Insulin Type', 'Price (INR)', 'Quantity available']])
    else:
        st.write(f"No store found for the brand name '{brand_name}'.")

if __name__ == '__main__':
    main()
