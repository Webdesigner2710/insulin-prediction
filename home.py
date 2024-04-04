import streamlit as st
from store import main as store_main
from dropdown import main as features_main
from storelocator import main as locator_main

def main():
    # Add a dropdown menu to select the page
    page = st.sidebar.selectbox("Select Page", ["Home", "Store Locator","Store Information by Pincode","Insulin Stock Prediction"])

    if page == "Home":
        st.title("**Insulin Stock Prediction Website**")
        st.image("insulin.png", use_column_width="small")
        st.write("""
            <div>
            <h1><b>OPTIMIZING PERISHABLE INVENTORY TRACKING FOR REAL-TIME DECISION MAKING</b></h1>
     
            <h2><b>Project Overview:</b></h2>
            <b>Our project aims to revolutionize the tracking and availability of perishable pharmaceutical inventory, particularly focusing on insulin, within healthcare management. By leveraging advanced technologies and data-driven insights, we strive to enhance operational efficiency and improve patient care outcomes through real-time inventory management and predictive analytics.</b>

            <h2><b>Objective:</b></h2>
            <b>The primary objective of our project is to optimize perishable pharmaceutical inventory tracking for real-time decision-making, aiming to enhance operational efficiency, minimize stockouts, and ultimately, improve patient care outcomes.</b>

            <h2><b>Why Insulin?</b></h2>
            <b>Insulin was chosen due to its widespread use, perishable nature, and the complexity of its supply chain. By focusing on insulin, we aim to develop methodologies and tools that can be applied to track and manage other perishable pharmaceuticals effectively.</b>

            <h2><b>Methodology:</b></h2>
            <b>Our approach involves the development and implementation of an integrated real-time tracking and analysis system for insulin inventory. This system enables continuous monitoring of inventory levels and expiration dates, leveraging predictive analytics to forecast future availability and facilitate proactive decision-making.</b>
            
            <h2><b>Future Scope:</b></h2>
            <b>The methodology and tools developed for insulin tracking can be extended to other medical equipment, facilitating their efficient tracking and availability within healthcare management.</b>

            </div>
        """, unsafe_allow_html=True)
        st.write("""
         <div>
            <h2><b>About our website:</b></h2>
            <b>Our website is dedicated to optimizing the tracking and availability of insulin, a critical perishable pharmaceutical, within healthcare management.</b>
            <br><br>
            <b>By leveraging advanced technologies and data-driven insights, our platform aims to enhance operational efficiency and improve patient care outcomes through real-time inventory management and predictive analytics.</b>
            <br><br>
            <b>Here, you can explore various features related to insulin stocks and locate stores selling specific insulin brands based on store pincodes.</b>
            <br><br>
            <b>Use the dropdown menu to navigate between different sections of the website.</b>
            <br><br>
            <b>Enjoy exploring!</b>
        </div>
        
        """, unsafe_allow_html=True)
    elif page == "Store Locator":
        store_main()
    elif page == "Store Information by Pincode":
        locator_main()
    elif page == "Insulin Stock Prediction":
        features_main()

if __name__ == '__main__':
    main()