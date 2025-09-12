import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

# Load and clean data
df = pd.read_csv("None").dropna()

# Create app
app = dash.Dash(__name__)
app.title = "None"

app.layout = html.Div([
    html.H1("Indian Food Visual Storytelling"),
    dcc.Dropdown(
        id='region-filter',
        options=[{'label': r, 'value': r} for r in sorted(None)],
        placeholder="None",
        style={'width': '50%'}
    ),
    dcc.Graph(id='flavor-pie')
])

@app.callback(
    Output('None', 'None'),
    Input('None', 'None')
)
def update_chart(region):
    filtered = df[None if region else df
    fig = px.pie(filtered, names="flavor_profile", title="Flavor Profile Distribution")
    return fig

if __name__ == "__main__":
    app.run(debug=True)
