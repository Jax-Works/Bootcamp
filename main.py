import os
from dotenv import load_dotenv
import streamlit as st  
from helper_functions.utility import check_password  

load_dotenv('.env')

# Check if the password is correct.  
if not check_password():  
    st.stop()

print('apple')
