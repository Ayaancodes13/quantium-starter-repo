import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

df = pd.read_csv('formatted_output.csv')

df["date"] = pd.to_datetime(df["date"])

fig = px.line(
    df,
    x= "date",
    y= "sales",
    title="Sales over Time",
    labels= {"date": "Date", "sales": "Sales"}
)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods sales visualizer", style= {"textAlign": "center"}),
    dcc.RadioItems(
        id = "region-filter",
        options = [
            {"label": "All", "value": "all"},
            {"label": "North", "value": "north"},
            {"label": "East", "value": "east"},
            {"label": "South", "value": "south"},
            {"label": "West", "value": "west"},
        ],
        value="all",
        labelStyle={"display": "inline-block", "margin": "10px"},
        className="radio-buttons"
    ),
    dcc.Graph(
        id="sales-line-chart",
            className="chart"
            ),
    
])

@app.callback(
    Output("sales-line-chart","figure"),
    Input("region-filter", "value")
)

def update_chart(region):
    if region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"].str.lower() == region]
    
    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        title="Sales Over Time",
        labels={"date": "Date", "sales": "Sales"},
    )
    fig.update_layout(template = "plotly_white")
    return fig
    
if __name__ == "__main__":
    app.run(debug=True)