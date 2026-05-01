import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Unemployment Analysis", layout="wide")

st.title("📊 Unemployment Analysis in India")

# Load data safely
@st.cache_data
def load_data():
    file_path = os.path.join(os.path.dirname(__file__), "Unemployment in India.csv")
    df = pd.read_csv(file_path)

    df.columns = df.columns.str.strip()
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
    df = df.dropna()
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("Filters")

year = st.sidebar.selectbox("Select Year", sorted(df['Year'].unique()))
region = st.sidebar.selectbox("Select Region", sorted(df['Region'].unique()))

filtered = df[(df['Year'] == year) & (df['Region'] == region)]

# Charts
st.subheader("📈 Unemployment Trend Over Time")
st.line_chart(filtered.groupby('Date')['Estimated Unemployment Rate (%)'].mean())

st.subheader("📊 Monthly Trend")
st.bar_chart(filtered.groupby('Month')['Estimated Unemployment Rate (%)'].mean())

st.subheader("🌍 Region-wise Unemployment")
st.bar_chart(df.groupby('Region')['Estimated Unemployment Rate (%)'].mean())

st.subheader("📅 Year-wise Trend")
st.line_chart(df.groupby('Year')['Estimated Unemployment Rate (%)'].mean())

# Raw data
with st.expander("🔍 View Raw Data"):
    st.dataframe(df)
