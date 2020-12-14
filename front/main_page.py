import streamlit as st
import pandas as pd
import altair as alt
from stock_data import *
from predictor import *

def set_title():
    st.title('StockMarketML')

def show_sidebar_help():
    st.sidebar.header("How to use")
    st.sidebar.write("""
        1. Pick index. \n
        2. Press 'Predict' button. \n
        3. Enjoy our prediction report.""")

def show_stock_details(stock):
    st.image(stock.get_url(), width = 500)
    st.header(stock.get_name())
    st.subheader('NYSE, ' + stock.get_index())
    st.write(stock.get_description())

def show_report(stock):
    df_predicted = predict_for_index(stock.get_index())
    df_previous_90 = get_last_ndays_data(stock.get_index(), 90)['Open']
    df_previous_14 = get_last_ndays_data(stock.get_index(), 14)['Open']


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



set_title()
show_sidebar_help()

selected_index = st.selectbox("Pick stock", ["Tesla", "Ford", "Apple"])

if st.button("Predict"):
    stock = get_by_name(selected_index)

    show_stock_details(stock)
    show_report(stock)

