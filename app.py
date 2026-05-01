import streamlit as st
import pandas as pd

st.set_page_config(page_title="Unemployment Analysis", layout="wide")

st.title("📊 Unemployment Analysis in India")

@st.cache_data
def load_data():
    df = pd.read_csv("Unemployment in India.csv")
    df.columns = df.columns.str.strip()
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
    df = df.dropna()
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    return df

df = load_data()

st.sidebar.header("Filters")

year = st.sidebar.selectbox("Select Year", sorted(df['Year'].unique()))
region = st.sidebar.selectbox("Select Region", sorted(df['Region'].unique()))

filtered_df = df[(df['Year'] == year) & (df['Region'] == region)]

st.subheader("📈 Unemployment Trend Over Time")
st.line_chart(filtered_df.groupby('Date')['Estimated Unemployment Rate (%)'].mean())

st.subheader("📊 Monthly Trend")
st.bar_chart(filtered_df.groupby('Month')['Estimated Unemployment Rate (%)'].mean())

st.subheader("🌍 Region-wise Unemployment")
st.bar_chart(df.groupby('Region')['Estimated Unemployment Rate (%)'].mean())

st.subheader("📅 Year-wise Trend")
st.line_chart(df.groupby('Year')['Estimated Unemployment Rate (%)'].mean())

with st.expander("🔍 Raw Data"):
    st.dataframe(df)
