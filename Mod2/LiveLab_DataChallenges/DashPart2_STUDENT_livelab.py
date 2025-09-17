'''import pandas as dp
from dash import html, dcc, dash
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
'''
'''# Load and clean data
df = pd.read_csv("/Users/Marcy_Student/Downloads/indian_food.csv").dropna()
# Create app
app = dash.Dash(__name__)
app.title = "My Fisrt app"

app.layout = html.Div([
    html.H1("Indian Food Visual Storytelling"),
    dcc.Dropdown(
        id='region-filter',
        options=[{'label': r, 'value': r} for r in sorted(df["region"].unique())],
        placeholder="Select a region",
        style={'width': '50%'}
    ),
    dcc.Graph(id='flavor-pie')
])

@app.callback(
    Output('flavor-pie', 'figure'),
    Input("region-filter", "value")
)
def update_chart(region):
    filtered = df[df['region'] == region] if region else df
    fig = px.pie(filtered, names="flavor_profile", title="Flavor Profile Distribution")
    return fig

if __name__ == "__main__":
    app.run(debug=True)'''
