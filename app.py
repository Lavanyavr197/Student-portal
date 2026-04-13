import streamlit as st
import pandas as pd

st.title("📊 Student Performance Dashboard")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Data")
    st.write(df)

    st.subheader("📈 Average")
    st.write(df.mean(numeric_only=True))

    st.subheader("🏆 Topper")
    top = df.loc[df['Total'].idxmax()]
    st.write(top)

    st.subheader("📉 Weak Students")
    st.write(df[df['Total'] < 50])

    st.bar_chart(df.set_index('Name')['Total'])
