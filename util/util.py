import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None

def load_saved_artifacts():
    print("loading saved assets...start")
    global  __data_columns
    global __locations

    with open("Alpha_converter.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[5:]  # first 4 columns are sqft, bath, balcony,area

    global __model
    if __model is None:
        with open('banglore_home.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved assets...done")

def get_estimated_price(location,sqft,bath,balcony,area_typeEncoded):
    try:
        loc_index = __data_columns.index(location.lower())     ##find position of loc column in Alpha_converter
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = balcony
    x[3] = area_typeEncoded
    if loc_index>=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)  ## round 2  after deci


""" def load_saved_artifacts():                 ## fn can be in either place
    print("loading saved artifacts...start")    
    global  __data_columns
    global __locations

    with open("Alpha_converter.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[5:]  # first 4 columns are sqft, bath, balcony,area

    global __model
    if __model is None:
        with open('banglore_home.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved assets...done") """

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar',1000, 3, 2, 2))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2, 1))
    print(get_estimated_price('Kalhalli', 2000, 2, 2, 2)) # other location
    print(get_estimated_price('Ejipura', 1500, 2, 2, 3))  # other location