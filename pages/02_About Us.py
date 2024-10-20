import streamlit as st
from helper_functions.utility import check_password 

# Check if the password is correct.  
if not check_password():  
    st.stop()

# Create an "About this app" section
st.set_page_config(
    layout="centered",
    page_title="About Us"
)

# To clear existing session state
if st.session_state.get("DF_COMBINED") is not None:
    del st.session_state["DF_COMBINED"]

# Set the title of the app
st.title("About Us")

# Self Introduction
st.subheader("Introduction")
st.write("""
         I am an analyst in the Singapore Police Force (SPF), 
         I am passionate about harnessing the power of data and large language models to transform the way we work. 
         My interest is on integrating data and artificial intelligence into practical applications that enhance efficiency and effectiveness in our processes. 
         By leveraging innovative technologies, I aim to save time and improve outcomes, ultimately contributing to a more proactive and informed approach to law enforcement
         """)

st.subheader("Context")
st.write("""
         SPF has dedicated analysts to research upon and keep track of different types of databases relating to different offences.

         Currently, we lack a dedicated database for cases relating to Digital Manipulation (DM).
         DM cases refer to cases where there are alteration/enhancement/modifications from simple digital editing to the use of AI/ML technologies used on photos, videos, and audio. 
         Manual sifting of case reports is plausible but is inefficient with the huge number of cases. 
         Using search terms for identification may lead to inaccuracies and missed narratives. 
         Leveraging LLMs could enhance the accuracy of case filtering for DM-related incidents.
         """)

st.subheader("Objectives")
st.write("""
         The primary objective is to implement a large language model (LLM) that can efficiently identify whether cases are related to Digital Manipulation (DM). 
         This initiative aims to free up analysts' time by streamlining the process of determining DM-related cases, allowing them to enrich these identified cases with information from other system sources or focus on analyzing additional databases.

         Our goal is to achieve a successful proof of concept (POC) during this bootcamp before transitioning to work with real reports in a separate environment. 
         Since actual police reports are classified as confidential, they cannot be hosted online.

         By significantly reducing the time required to sift through reports, the specific solution for DM can be utilized on a weekly or monthly basis to identify new cases for the database.

         If the POC is successful and demonstrates considerable time savings, we envision using the LLM identification approach for emerging and unique crime narratives in the future.
        """)

st.subheader("Data Sources")
st.write("""
         The data is obtained from police reports. 
         Personal identifiable information has been removed to ensure anonymity.
         Any names of individuals or businesses used are completely made-up.
         """)

st.subheader("Contact")
st.write("For any inquiries, please reach out to peng_jian_xing@spf.gov.sg")

