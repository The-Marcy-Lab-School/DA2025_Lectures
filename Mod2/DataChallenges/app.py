# Import packages 

import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

# Load and filter the data
df = pd.read_csv('sports.csv')
df = df[["sports", "rev_men", "rev_women"]].dropna()


# Pick 5 sports
top5 = ['Lacrosse', 'Tennis', 'Golf', 'Soccer', 'Swimming and Diving']
#Copying the dataframe to not overwrite the original 
df_5 = df[df["sports"].isin(top5)].copy()


# Create new column called Total_Revenue that adds up the men and women's revenue columns
df_5["Total_Revenue"] = df_5["rev_men"] + df_5["rev_women"]


fig = px.pie(df_5, names='sports', values='Total_Revenue', title='Total Revenue by Sport')


app = dash.Dash(__name__)
app.title = "Top 5 sports"

app.layout = html.Div([
    html.H1("Revenue Analysis for 5 Sports", style={'textAlign': 'center'}),
    dcc.Graph(figure = fig)
])

if __name__ == '__main__':
    app.run(debug=True)