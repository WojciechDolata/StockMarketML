from back.ModelRepository import ModelRepository
import pandas as pd

def get_mock_data():
    return pd.read_csv('data/train.csv').head(7690).tail(60)['Open'].values

model = ModelRepository()

data = get_mock_data()
print(model.predict(data))
