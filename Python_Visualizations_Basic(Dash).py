import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Load Datasets
recipes = pd.read_csv("recipes.csv")
interactions = pd.read_csv("interactions.csv")

# Initialize Dash App
app = dash.Dash(__name__)

# Preprocess Data
cuisine_counts = recipes["cuisine"].value_counts().reset_index()
cuisine_counts.columns = ["Cuisine", "Count"]

# Layout
app.layout = html.Div([
    html.H1("Personalized Recipe Recommendation System"),

    html.Div([
        html.Label("Filter by Cuisine:"),
        dcc.Dropdown(
            id="cuisine-filter",
            options=[{"label": cuisine, "value": cuisine} for cuisine in recipes["cuisine"].unique()],
            multi=True,
            placeholder="Select Cuisines",
        )
    ]),

    html.Div([
        html.Label("Filter by Cooking Time (minutes):"),
        dcc.Slider(
            id="time-filter",
            min=recipes["minutes"].min(),
            max=recipes["minutes"].max(),
            step=5,
            value=30,
            marks={i: str(i) for i in range(0, recipes["minutes"].max(), 30)},
        )
    ]),

    html.Div([
        html.H3("Top Recommended Recipes:"),
        html.Div(id="recommendation-output")
    ]),

    html.Div([
        dcc.Graph(id="cuisine-distribution")
    ])
])

# Callbacks
@app.callback(
    [Output("recommendation-output", "children"),
     Output("cuisine-distribution", "figure")],
    [Input("cuisine-filter", "value"),
     Input("time-filter", "value")]
)
def update_dashboard(selected_cuisines, cooking_time):
    # Filter recipes
    filtered_recipes = recipes
    if selected_cuisines:
        filtered_recipes = filtered_recipes[filtered_recipes["cuisine"].isin(selected_cuisines)]
    filtered_recipes = filtered_recipes[filtered_recipes["minutes"] <= cooking_time]

    # Recommendations
    recommendations = filtered_recipes.head(5)[["name", "minutes", "cuisine"]]
    recommendation_list = [
        html.Div(f"{row['name']} ({row['cuisine']} - {row['minutes']} minutes)") for _, row in recommendations.iterrows()
    ]

    # Cuisine Distribution Chart
    cuisine_fig = px.bar(cuisine_counts, x="Cuisine", y="Count", title="Cuisine Distribution")

    return recommendation_list, cuisine_fig

# Run Server
if __name__ == "__main__":
    app.run_server(debug=True)
