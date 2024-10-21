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

# To clear existing session state
if st.session_state.get("DF_COMBINED") is not None:
    del st.session_state["DF_COMBINED"]

# Set the title of the app
st.title("Methodology")

st.subheader("Features")
st.write("""
         This app offers two key features:

Automated Digital Manipulation (DM) Detection: The app automatically identifies whether police reports are related to digital manipulation (DM) cases. 
         It leverages advanced prompting techniques, such as chain-of-thought prompting, to enhance the accuracy of its evaluations.

Case Summary Generation: The app generates concise yet informative summaries of uploaded DM cases. 
         It provides an overview of the incidents and highlights potential patterns and trends observed.

Designed for scalability, the app efficiently processes uploads, delivering streamlined insights for researchers and professionals handling large volumes of DM data.""")

# Insert flowchart
st.image("image/Flowchart.png", caption="Illustration of Methodology as a Flowchart")