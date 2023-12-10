import streamlit as st
import openai
import pandas as pd

def main():
    st.title("ChatGPT Downgraded version.")

    # Sidebar for API key input
    api_key = st.sidebar.text_input("Enter OpenAI API Key", type="password")

    # User input
    user_input = st.text_area("Enter your prompt:")

    # Get OpenAI ChatGPT response
    if st.button("Generate Response"):
        if api_key:
            openai.api_key = api_key
            response = generate_response(user_input)
            st.success("Response Generated Successfully!")
            st.write("Answer Output:")
            st.write(response)
            st.write("Formatted Output as DataFrame:")
            display_results_as_dataframe(response)
        else:
            st.error("Please enter your OpenAI API key in the sidebar.")

    # File upload for CSV or Excel
    uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])
    if uploaded_file is not None:
        st.write("File Uploaded Successfully!")
        df = pd.read_csv(uploaded_file) if uploaded_file.type == "application/vnd.ms-excel" else pd.read_excel(
            uploaded_file
        )
        st.write("Data from the Uploaded File:")
        st.write(df)

        # Process data using OpenAI ChatGPT if needed

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use appropriate engine
        prompt=prompt,
        max_tokens=2000,  # Adjust as needed
    )
    return response.choices[0].text.strip()

def display_results_as_dataframe(response):
    # Split the response into lines and then split each line into columns
    rows = [line.split(",") for line in response.split("\n")]

    # Create a DataFrame from the rows
    df = pd.DataFrame(rows)

    # Display the DataFrame
    st.dataframe(df)

if __name__ == "__main__":
    main()