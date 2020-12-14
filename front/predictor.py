from data_fetcher import *
import tensorflow as tf
import pandas as pd
import numpy as np
from datetime import timedelta
import sys
sys.path.append('../')
from back.ModelRepository import ModelRepository

def get_week_ahead(beg_date):
    arr = []
    curr_date = beg_date + timedelta(1)
    for i in range(7): 
        if curr_date.weekday() == 6:
            curr_date = curr_date + timedelta(1)
        elif curr_date.weekday() == 5:
            curr_date = curr_date + timedelta(2)
        
        arr.append(curr_date)
        curr_date = curr_date + timedelta(1)
    return arr
    
def predict_for_index(index):
    orig_data = get_last_60d_data(index)

    open_data = orig_data['Open'].values

    model = ModelRepository()
    predicted_data = model.predict(open_data)

    last_day = orig_data.index[orig_data['Open'].values.size - 1]

    df = pd.DataFrame(columns=['Open'], data=np.transpose(predicted_data), index=pd.DatetimeIndex( get_week_ahead(last_day)))

    return df
