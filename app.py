import streamlit as st
from dotenv import load_dotenv
from data.employee_data_generator import generate_employee_data
import time

if __name__ == "__main__":
    load_dotenv()
    st.set_page_config(page_title="Company onboarding assistant", layout="wide")

    with st.sidebar:
        st.title("Company onboarding assistant")
        st.header("Employee data :")

        # Show spinner for 5 seconds
        with st.spinner("Fetching..."):
            time.sleep(5)
            employees = generate_employee_data(num_records=1)  # generate 1 record

        # Display the generated employee data
        for emp in employees:
            st.write(f"**Name:** {emp['name']}")
            st.write(f"**Employee ID:** {emp['employee_id']}")
            st.write(f"**Designation:** {emp['designation']}")
            st.write(f"**Department:** {emp['department']}")