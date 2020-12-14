import streamlit as st
import pandas as pd
import altair as alt
from predictor import *

st.title('StockMarketML')

if st.button("Help."):
    "1. Pick index."
    "2. Press 'Predict' button."
    "3. Enjoy our prediction report."

selected_index = st.selectbox("Pick index", ["TSLA", "F"])

if st.button("Predict"):
    
    df_predicted = predict_for_index(selected_index)
    df_previous_90 = get_last_ndays_data(selected_index, 90)['Open']
    df_previous_14 = get_last_ndays_data(selected_index, 14)['Open']



    st.header('Report for stock: ' + selected_index +'\n')

    st.subheader('Values of this index in the last 3 months:')    
    previous_plt = alt.Chart(df_previous_90.reset_index()).mark_line().encode(
        x=alt.X('Date', axis=alt.Axis(title='Date')),
        y=alt.Y('Open', scale=alt.Scale(zero=False))
    )
    st.write(previous_plt)

    st.subheader('and in the last two weeks:')    
    previous_plt = alt.Chart(df_previous_14.reset_index()).mark_line().encode(
        x=alt.X('Date', axis=alt.Axis(title='Date')),
        y=alt.Y('Open', scale=alt.Scale(zero=False))
    )
    st.write(previous_plt)

    st.subheader('Predicted values for the next two weeks:')    
    predicted_plt = alt.Chart(df_predicted.reset_index()).mark_line().encode(
        x=alt.X('index', axis=alt.Axis(title='Date')),
        y=alt.Y('Open', scale=alt.Scale(zero=False))
    )
    st.write(predicted_plt)
