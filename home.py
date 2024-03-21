import streamlit as st
from store import main as store_main
from dropdown import main as features_main
from storelocator import main as locator_main

def main():
    # Add a dropdown menu to select the page
    page = st.sidebar.selectbox("Select Page", ["Home", "Store Locator", "Insulin Stock Prediction","Store Information by Pincode"])

    if page == "Home":
        st.title("Insulin Prediction Website")
        st.image("insulin image.png", caption="Your Logo", use_column_width=True)
        st.write("""
            Welcome to our Insulin Prediction Website!

            Here, you can explore various features related to insulin stocks and locate stores selling specific insulin brands.

            Use the dropdown menu to navigate between different sections of the website.

            Enjoy exploring!
        """)
    elif page == "Store Locator":
        store_main()
    elif page == "Insulin Stock Prediction":
        features_main()
    elif page == "Store Information by Pincode":
        locator_main()

if __name__ == '__main__':
    main()