import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

# Load and clean data
df = pd.read_csv("/Users/Marcy_Student/Downloads/indian_food.csv").dropna()
print(df.columns)

# Create app
app = dash.Dash(__name__)
app.title = "My First App"

app.layout = html.Div([
    html.H1("Indian Food Visual Storytelling"),
    dcc.Dropdown(
        id='prep_time',
        options=[{'label': r, 'value': r} for r in sorted(df["prep_time"].unique())],
        placeholder="Select the preparation time",
        style={'width': '50%'}
    ),
    dcc.Dropdown(
        id='cook_time',
        options=[{'label': r, 'value': r} for r in sorted(df["cook_time"].unique())],
        placeholder="Select the cooking time",
        style={'width': '50%'}
    ),
    dcc.Graph(id='flavor-pie')
])


@app.callback(
    Output('flavor-pie', 'figure'),
    Input("prep_time", "value"),
    Input("cook_time", "value"),
)
def update_chart(prep_time, cook_time):
    filtered = df.copy()
    if prep_time:
        filtered = filtered[filtered['prep_time'] == prep_time]
    if cook_time:
        filtered = filtered[filtered['cook_time'] == cook_time]

    fil = filtered.groupby("course")["prep_time"].mean().reset_index()
    fig = px.bar(fil, x="course", y="prep_time", title="Average Prep Time by Course")
    return fig


if __name__ == "__main__":
    app.run(debug=True)
