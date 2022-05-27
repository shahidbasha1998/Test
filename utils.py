import pickle
import json
import numpy as np

__gender = None
__test_name = None
__sample_storage = None
__traffic_conditions = None

__data_columns = None
__model = None

def get_predict(age,gender,test_name,sample_storage,traffic_conditions,time_taken_for_sample_collection,lab_location,time_taken_to_reach_lab):

    gender_index =__data_columns.index(gender.lower())
    test_name_index = __data_columns.index(test_name.lower())
    sample_storage_index = __data_columns.index(sample_storage.lower())
    traffic_conditions_index = __data_columns.index(traffic_conditions.lower())

    x = np.zeros(len(__data_columns))
    x[0] = age
    x[1] = time_taken_for_sample_collection
    x[2] = lab_location
    x[3] = time_taken_to_reach_lab

    if gender_index >= 0:
        x[gender_index] = 1
    if test_name_index >= 0:
        x[test_name_index] = 1
    if sample_storage_index >= 0:
        x[sample_storage_index] = 1
    if traffic_conditions_index >= 0:
        x[traffic_conditions_index] = 1

    return __model.predict([x])[0]



def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __gender
    global __test_name
    global __sample_storage
    global __traffic_conditions

    global  __data_columns

    with open("columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']

        __gender = __data_columns[4:6]# first 3 columns are sqft, bath, bhk
        __test_name = __data_columns[6:16]
        __sample_storage = __data_columns[16:18]
        __traffic_conditions = __data_columns[20:]

    global __model

    if __model is None:
        with open('Medical_sample.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")
#
# def get_gender():
#     return __gender
# def get_test_name():
#     return __test_name
# def get_sample_storage():
#     return __sample_storage
# def get_traffic_conditions():
#     return __traffic_conditions
#
# def get_data_columns():
#     return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_predict(34,'Male','Acute kidney profile','Advanced','High Traffic',100,23,26))