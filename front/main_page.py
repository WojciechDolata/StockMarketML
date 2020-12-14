import streamlit as st
import pandas as pd
from predictor import *

st.title('StockMarketML')

if st.button("Help."):
    "1. Pick index."
    "2. Press 'Predict' button."
    "3. Enjoy our prediction report."

selected_index = st.selectbox("Pick index", ["TSLA", "F"])

if st.button("Predict"):
    
    df_predicted = predict_for_index(selected_index)
    # visualize here
    df_previous = get_last_30d_data(selected_index)['Open']

    st.write(df_previous)
    
    st.write(df_predicted)

    # st.line_chart(predicted_data[0])


# df = pd.read_csv("my_data.csv")
# st.line_chart(df)