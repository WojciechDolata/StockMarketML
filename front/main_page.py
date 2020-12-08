import streamlit as st
import pandas as pd
from predictor import *


st.write("""
# StockMarketML
""")

selected_index = st.selectbox("Pick index", ["TSLA", "F"])

if st.button("Predict"):
    
    predicted_data = predict_for_index(selected_index)
    # visualize here

    st.write(predicted_data)

# df = pd.read_csv("my_data.csv")
# st.line_chart(df)