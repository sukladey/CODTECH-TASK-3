import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Load dataset
df = pd.read_csv("sales_data.csv")

# Charts
sales_region = px.bar(
    df,
    x="Region",
    y="Sales",
    color="Region",
    title="Sales by Region"
)

profit_category = px.pie(
    df,
    names="Category",
    values="Profit",
    title="Profit by Category"
)

product_sales = px.bar(
    df,
    x="Product",
    y="Sales",
    color="Category",
    title="Sales by Product"
)

# Create Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Sales Analytics Dashboard", style={"textAlign": "center"}),

    dcc.Graph(figure=sales_region),

    dcc.Graph(figure=profit_category),

    dcc.Graph(figure=product_sales)
])

if __name__ == "__main__":
    app.run(debug=True)
