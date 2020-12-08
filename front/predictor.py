from data_fetcher import *

def predict_for_index(index):
    data = get_last_year_data(index)
    # przewiduje i zwraca wyliczone wartości na np. tydzień w przód
    return data