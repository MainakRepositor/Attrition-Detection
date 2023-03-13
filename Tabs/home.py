"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Company Attrition Prediction")

    # Add image to the home page
    st.image("./images/home.png")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
            The azttrition rate is calculated as the percent of employees who have left the organization by the average number of employees. Ideally, the average attrition rate should be less than 10%, and an attrition rate greater than 20%' is alarming for any company.
        </p>
    """, unsafe_allow_html=True)