import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

df = pd.read_csv("formatted_sales_data.csv")

df['Date'] = pd.to_datetime(df['Date'])

daily_sales = df.groupby('Date')['Sales'].sum().reset_index()

fig = px.line(
    daily_sales,
    x='Date',
    y='Sales',
    title='Pink Morsel Sales Over Time',
    labels={'Sales': 'Total Sales ($)', 'Date': 'Date'},
)

price_change_date = "2021-01-15"
fig.add_vline(x=price_change_date, line_dash="dash", line_color="red")
fig.add_annotation(
    x=price_change_date,
    y=max(daily_sales['Sales']),
    text="Price Increase",
    showarrow=True,
    arrowhead=1
)

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1("Pink Morsel Sales Visualiser", style={'textAlign': 'center'}),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)

