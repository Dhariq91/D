
import pandas as pd
import streamlit as st

def suggest_components(user_type):
    # Load the Excel file
    file_path = "PC_Components.xlsx"
    try:
        df = pd.read_excel(file_path)
    except FileNotFoundError:
        st.error("The components file is missing. Please make sure 'PC_Components.xlsx' is in the same directory.")
        return

    # Filter the components based on user type
    suggestions = df[df['User Type'] == user_type]

    if suggestions.empty:
        st.warning(f"No suggestions found for user type: {user_type}.")
    else:
        st.success(f"Here are some suggested components for a {user_type}:")
        st.dataframe(suggestions.head())

# Streamlit UI
st.title("PC Component Suggester")
st.write("Welcome! Please select your user type to get component suggestions.")

# User input
user_type = st.selectbox("Select your user type:", ["Gamer", "Editor", "Developer", "Streamer", "General User"])

if st.button("Suggest Components"):
    suggest_components(user_type)
