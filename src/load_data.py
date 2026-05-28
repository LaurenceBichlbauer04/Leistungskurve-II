import pandas as pd

def load_activity(data):
    df = pd.read_csv(data)
    df["Time"] = range(len(df))
    return df



    

   
