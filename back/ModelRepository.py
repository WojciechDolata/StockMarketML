from tensorflow import keras
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from back.metadata import model_path

class ModelRepository(object):
    def __init__(self):
        self.model = keras.models.load_model(model_path)
        self.n_steps = 60
        self.allowed_inputs = [list, tuple, np.ndarray]
        self.scaler = MinMaxScaler(feature_range=(0,1))

    def predict(self, data):
        """ 
        The function makes 7-day stock price prediction based on prices from 60 previous days.
  
        Parameters: 
            data (list | tuple | numpy.ndarray) - array-like 1D input of 60 daily values on which to base prediction upon
          
        Returns: 
            numpy.ndarray - vector of shape (1, 7) containing predicted values - one per day
        """

        if type(data) not in self.allowed_inputs:
            raise TypeError(f'Data input must be one of the {self.allowed_inputs}. Received type: {type(data)}')

        if len(data) != self.n_steps:
            raise ValueError(f'Data needs to be 1D input of length {self.n_steps}, Received length: {len(data)}')

        data = np.array(data).reshape((60, 1))
        scaled_data = self.scaler.fit_transform(data)
        reshaped_data = scaled_data.reshape((1, 60, 1))

        result = self.model.predict(reshaped_data)
        scaled_result = self.scaler.inverse_transform(result)

        return scaled_result