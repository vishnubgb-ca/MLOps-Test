from data_extraction import get_data
import pandas as pd

def date_preprocessing():
    print("............In  data_preprocessing............")
    data = get_data()
    data.set_index("datetime", inplace=True)
    data.index=pd.to_datetime(data.index)
    data=data.sort_index()
    print(data.shape)
    data=data.resample("10s").max()
    data.dropna(inplace=True)
    print(data.shape)
    data["datetime"]= data.index
    print(data.info())
    return data

date_preprocessing()
