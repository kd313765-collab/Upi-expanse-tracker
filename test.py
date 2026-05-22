import streamlit as st
import pandas as pd

st.title("UPI Expense Tracker")

st.write("To check the total investment")

file = st.file_uploader("test.csv", type="csv")

if file:
    df = pd.read_csv(file)
    st.write("Total Rows:", len(df))
    st.dataframe(df)
    
    if 'Debit' in df.columns:
        st.write("Total Investment: ₹", df['Debit'].sum())
else:
    st.info("I understand it total investment by me ")