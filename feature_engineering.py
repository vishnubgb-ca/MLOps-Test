# from data_visualization import data_visualizations
from data_preprocessing import date_preprocessing
import pandas as pd
import numpy as np

def feature_engineering():
    print("............In  feature_engineering............")
    data = date_preprocessing()
    #renaming ther columns
    data.rename(columns={"datetime":"ds", "Temperature":"y"}, inplace=True)

    # data preprocess
    # finding the last recorded date
    last_date = data['ds'].max()
    # Calculating 10 seconds before the start of the next day
    next_date_start = pd.Timestamp(last_date.date()) + pd.DateOffset(days=1)  # Start of the next day
    next_timeline = next_date_start - pd.Timedelta(seconds=10)

    # Checking if the next timeline already exists
    if not any(data['ds'] == next_timeline):
        # Adding the next timeline 10 seconds before the start of the next day
        new_row = pd.DataFrame({'ds': [next_timeline]})
        data = pd.concat([data, new_row], ignore_index=True)
    data = data.ffill()  # Forward fill NaN values
    data.drop("Current", axis=1, inplace=True)
    cols = list(data.columns)
    cols.remove('ds')
    cols.insert(0, 'ds')
    data = data[cols]
    print(data.tail())
    data.to_csv("test_data_cleansed.csv", index=False)
    print(".......pipeline successful.....")
    return data

feature_engineering()
