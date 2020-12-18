import streamlit as st
import pandas as pd
import altair as alt
from stock_data import *
from predictor import *

def set_title():
    st.title('StockMarketML')

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

    # left align table values, css-y37zgl is the class of table div
    st.markdown(
        """<style>
            .css-y37zgl {text-align: left !important}
        </style>
        """, unsafe_allow_html=True)


    today_value = df_previous_14.values[df_previous_14.size - 1]
    df_percentage_predicted = df_predicted.apply(lambda x: (x - today_value) / today_value * 100)

    st.subheader('Predicted gain/loss (in %) compared to current stock value')
    df_percentage_predicted = df_percentage_predicted.style.applymap(lambda x: 'color: red' if x <= 0 else 'color: green')
    st.table(df_percentage_predicted)


set_title()
# show_sidebar_help()

st.sidebar.header("How to use")
st.sidebar.write("""
        1. Pick index. \n
        2. Press 'Predict' button. \n
        3. Enjoy our prediction report.""")
st.sidebar.header("Pick stock")
selected_index = st.sidebar.selectbox("", ["Tesla", "Ford", "Apple"])

if st.sidebar.button("Predict"):
    stock = get_by_name(selected_index)

    show_stock_details(stock)
    show_report(stock)

