import streamlit as st 
from dotenv import load_dotenv
from data.employee_data import generate_employee_data
import time

if __name__ == "__main__":
    load_dotenv()

    st.set_page_config(page_title="Company onboarding assistant", layout="wide")

    with st.sidebar:  
        st.title("Company onboarding assistant")
        st.write("Employee data")
        with st.spinner("Fetching..."):
            time.sleep(5)
        st.success("Done!")
