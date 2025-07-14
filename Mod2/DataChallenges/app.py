from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

# Load and clean data
df = pd.read_csv("indian_food.csv").dropna(subset=["prep_time", "cook_time", "flavor_profile", "region"])

# Create app
app = Dash(__name__)
app.title = "Prep vs Cook Time Comparison"

app.layout = html.Div([
    html.H1("Indian Food: Prep vs Cook Time by Flavor"),
#html.p example:
    html.P("Welcome! Explore how prep time compares to cook time in Indian recipes.", style={'fontSize': '18px', 'color': '#c51b8a'}),


    dcc.Dropdown(
        id='region-filter',
        options=[{'label': r, 'value': r} for r in sorted(df['region'].unique())],
        placeholder="Select a region",
        style={'width': '50%'}
    ),

    dcc.Graph(id='prep-cook-scatter')
])

@app.callback(
    Output('prep-cook-scatter', 'figure'),
    Input('region-filter', 'value')
)
def update_chart(region):
    filtered = df[df['region'] == region] if region else df
    fig = px.scatter(
        filtered,
        x="prep_time",
        y="cook_time",
        color="flavor_profile",
        title="Prep Time vs Cook Time by Flavor Profile",
        labels={"prep_time": "Prep Time (min)", "cook_time": "Cook Time (min)"},
        hover_data=["name"]  
    )
    return fig

if __name__ == "__main__":
    app.run(debug=True)

'''
1. What insight does your dashboard reveal about Indian food preparation?
My dashboard reveals how preparation time and cooking time vary across Indian recipes and how these factors differ by flavor profile. 
By filtering recipes by region, users can dive deeper and analyze whether certain regions tend to favor quicker meals or more time-intensive 
dishes. This regional breakdown allows for more meaningful comparisons and insights into traditional cooking practices.

2. What chart decisions did your group make and why?
I chose a scatter plot because it clearly shows the relationship between prep time and cook time. 
It also makes it easy to identify patterns, clusters, or outliers—for example, dishes that take a long time to prepare but 
cook quickly, or vice versa. Using color to represent flavor profiles adds an extra layer of insight without cluttering the chart.

3. What limitations exist in the data or what did you wish you could add?
Some limitations include missing or inconsistent data in certain columns, such as missing prep or cook times. 
I also wish the dataset had more details like spice level, cooking techniques, or ingredients, 
which could lead to even richer analysis. 

4. What part of Dash was most challenging? What was easier than expected?
The most challenging part was getting the callback functions to work correctly, especially managing IDs and making sure 
the inputs and outputs were aligned with the layout. On the other hand, creating clean layouts and 
using Plotly Express for charts was easier than expected. Dash’s components and structure felt intuitive once I got the hang of it.

5. How does your app reflect clarity, accessibility, or ethics in design?
The app uses simple, readable fonts, clear headings, and a dropdown for easy filtering, 
making it user-friendly and accessible to a wide audience. It avoids overwhelming the user with too 
many visuals and presents data in a clean and interpretable way. It shows the diversity of Indian cuisine 
by allowing users to explore regional differences without making generalized assumptions.

'''