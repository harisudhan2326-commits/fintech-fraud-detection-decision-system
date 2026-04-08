import pandas as pd

def load_data():
    df = pd.read_csv('../data/raw_data.csv')
    # print(df.head())
    # print("--------------------------")
    # print(df.shape)
    # print("--------------------------")
    # print(df.columns)
    # print("--------------------------")
    # print(df.describe())
    # print("--------------------------")
    # print(df.info())
    # print("--------------------------")
    # print (df['Class'].value_counts(normalize=True))
    return df
df = load_data()



