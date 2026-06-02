from src import powercurve
from src import load_data


def main():

    data = load_data.load_activity("data/activity.csv")
    #print(data)
    powercurve.curve_data(data)










if __name__ == "__main__":
    main()
