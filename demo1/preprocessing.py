import pandas as pd
import numpy as np

def create_interval_dataset(dataset, look_back):

    dataX, dataY = [], []
    for i in range(len(dataset) - look_back):
        dataX.append(dataset[i:i+look_back])
        dataY.append(dataset[i+look_back])
    return np.asarray(dataX), np.asarray(dataY)


df = pd.read_csv('./record.csv')
dataset_init = np.asarray(df)
dataX, dataY = create_interval_dataset(dataset_init, look_back=3)
print(dataX)
print(dataY)
