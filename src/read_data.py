import os
import pandas as pd
import numpy as np

data_path = "./data"

__all__ = ["get_df"]


def get_df():
    
    df = pd.read_csv(os.path.join(data_path, "Dane_zadanie1.csv"), sep=";")
    df["ProcessDate"] = pd.to_datetime(df["ProcessDate"], format="%Y-%m-%d")

    return df

def get_atm_df():

    df = get_df()
    ts = df.set_index('ProcessDate')
    atm_df = pd.DataFrame(index=pd.date_range(start=ts.index.min(), end=ts.index.max(), freq='D'))
    for name, gr in ts.groupby('Atm'):
        atm_df[name] = gr['Withdrawal']

    atm_df = atm_df.replace(np.nan, 0)
    atm_df = atm_df.astype(int)
    return atm_df
