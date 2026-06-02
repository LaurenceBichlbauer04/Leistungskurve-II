import pandas as pd

def load_activity(text):
    with open(text, "r") as file:
        return pd.read_csv(file)



    

   
