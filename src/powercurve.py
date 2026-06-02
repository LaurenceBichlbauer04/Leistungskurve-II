import pandas as pd

def curve_data(data):
    
    
    time_list = []
    max_avg_list = []
    #print(time)
    for i in range(1 , len(data)+1):
        max_avg = data["PowerOriginal"].rolling(i).mean().max()
        if not pd.isna(max_avg):
            time_list.append(i)
            max_avg_list.append(max_avg)
    df = pd.DataFrame({
        "Time" : time_list,
        "max_avg" : max_avg_list
    })
    #print(df)
    return df
        






if __name__ == "__main__":
    df = pd.read_csv("data/activity.csv")
    curve_data(df)
    
    