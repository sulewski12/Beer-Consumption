import pickle
import json
import numpy as np

__data_columns = None
__model = None

def get_estimated_consumption(avg_temp, min_temp, max_temp, precip, weekend, delta_temp):

    x = np.zeros(len(__data_columns))
    x[0] = avg_temp
    x[1] = min_temp
    x[2] = max_temp
    x[3] = precip
    x[4] = weekend
    x[5] = delta_temp

    return round(__model.predict([x])[0], 2)


def load_saved_data():
    print("Loading saved data...")
    global __data_columns

    with open("./artifacts/beer_consumption_columns.json", "r") as f:
        __data_columns = json.load(f)['data columns']

    global __model
    if __model is None:
        with open('./artifacts/beer_consumption_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("Loaded successfully!")


def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_data()