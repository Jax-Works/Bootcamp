import streamlit as st
from helper_functions.utility import check_password 

# Check if the password is correct.  
if not check_password():  
    st.stop()

# Create an "About this app" section
st.set_page_config(
    layout="centered",
    page_title="Guide"
)

# To clear existing session state
if st.session_state.get("DF_COMBINED") is not None:
    del st.session_state["DF_COMBINED"]

# Set the title of the app
st.title("Guide")

# Steps and instructions
st.subheader("Step 1")
st.write("""
         Prepare your file with the facts of cases to be uploaded.
         Ensure that the column of the facts of cases are labelled "FACTS".
         """)
st.image("image/Step 1.png")

st.subheader("Step 2")
st.write("""
         Upload your file with the facts of the police report in the "Main" page as seen below.
         """)
st.image("image/Step 2.png")

st.subheader("Step 3")
st.write("""
         Once the file is uploaded, a table will be displayed.
         Check whether the correct file is uploaded. 
         """)
st.image("image/Step 3.png")

st.subheader("Step 4")
st.write("""
         Click "Run LLM!" to send the table to the LLM for evaluation. 
         Please wait for the results, which will determine if the cases involve digital manipulation, along with a summary report.

         Check the 'Presence_of_DM' column to see whether the reports have been identified as related to digital manipulation. 
         """)
st.image("image/Step 4.png")

st.subheader("Step 5")
st.write("""
         Once the app has finished running, a download button will appear at the bottom of the page.
         If you would like the results of the generated table, click the "Download Data as CSV" button.
         """)
st.image("image/Step 5.png")