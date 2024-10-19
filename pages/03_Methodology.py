import streamlit as st
from helper_functions.utility import check_password 

# Check if the password is correct.  
if not check_password():  
    st.stop()

# Create an "Methodology" section
st.set_page_config(
    layout="centered",
    page_title="Methodology"
)


# Set the title of the app
st.title("Methodology")
st.write("This app has two main features..")


# Insert flowchart
