
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Retail Intelligence Dashboard")

st.write("Upload your sales CSV:")
file = st.file_uploader("Choose a CSV", type="csv")

if file:
    df = pd.read_csv(file)
    fig = px.line(df, x=df.columns[0], y=df.columns[1])
    st.plotly_chart(fig)

st.success("Dashboard Loaded Successfully")
