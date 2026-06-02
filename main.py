import plotly.graph_objects as go
from src import powercurve
from src import load_data

def main():

    data = load_data.load_activity("data/activity.csv")

    df = powercurve.curve_data(data)
    #print(df)
    
    # df = pd.DataFrame({
    # "Time": [1, 5, 10, 30, 60, 120, 300, 600, 1200, 1800, 3600],
    # "Power": [1100, 950, 850, 700, 620, 550, 450, 400, 350, 320, 280]
    # })

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x = df["Time"],
            y = df["max_avg"],
            mode="lines",
            line=dict(color="red"),
            line_shape="spline",
            name= "Powercurve"
            )
        )
    
    fig.update_layout(
        title="Power Curve",
        xaxis_type="log",
        xaxis_title="Duration",
        yaxis_title="Power (W)",
        width=800,
        height=500,
        plot_bgcolor="black",
        paper_bgcolor="black",
        font=dict(color="white")
    )

    fig.update_xaxes(
        tickmode="array",
        tickvals=[1, 5, 10, 30, 60, 120, 300, 600, 1200, 1800, 3600],
        ticktext=[
            "1s", "5s", "10s", "30s",
            "1m", "2m", "5m", "10m",
            "20m", "30m", "1h"
        ]
    )

    fig.show()

if __name__ == "__main__":
    main()