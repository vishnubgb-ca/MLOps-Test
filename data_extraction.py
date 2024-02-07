import pandas as pd

def get_data():
    print("............In  data_extraction............")
    data = pd.read_csv("test_sample.csv")
    # print(data.tail())
    return data

get_data()