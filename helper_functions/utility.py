import streamlit as st  
import random  
import hmac  

# """  
# This file contains the common components used in the Streamlit App.  
# This includes the sidebar, the title, the footer, and the password check.  
# """  

# Password check function
def check_password():
    """Returns `True` if the user entered the correct password."""
    def password_entered():
        """Checks whether the entered password is correct."""
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Remove the password for security
        else:
            st.session_state["password_correct"] = False

    # If the password is already validated, return True
    if st.session_state.get("password_correct", False):
        return True

    # Otherwise, show the password input
    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )
    
    if "password_correct" in st.session_state and not st.session_state["password_correct"]:
        st.error("😕 Password incorrect")
    
    return False
