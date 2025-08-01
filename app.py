import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px
from dash.dependencies import Input, Output

# Load processed data
df = pd.read_csv("formatted_sales_data.csv")
df['Date'] = pd.to_datetime(df['Date'])

# Create the app
app = dash.Dash(__name__)
app.title = "Pink Morsel Sales Visualizer"

# Layout with region filter
app.layout = html.Div(children=[
    html.H1("Pink Morsel Sales Visualiser", style={'textAlign': 'center'}),

    html.Div([
        html.Label("Select Region:", style={'fontWeight': 'bold'}),
        dcc.RadioItems(
            id='region-selector',
            options=[
                {'label': 'North', 'value': 'north'},
                {'label': 'South', 'value': 'south'},
                {'label': 'East', 'value': 'east'},
                {'label': 'West', 'value': 'west'},
                {'label': 'All', 'value': 'all'}
            ],
            value='all',
            labelStyle={'display': 'inline-block', 'margin-right': '10px'}
        )
    ], className='radio-box'),

    dcc.Graph(id='sales-line-chart')
])

# Callback to update the chart
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-selector', 'value')
)
def update_chart(selected_region):
    if selected_region == 'all':
        filtered_df = df.copy()
    else:
        filtered_df = df[df['Region'].str.lower() == selected_region]

    daily_sales = filtered_df.groupby('Date')['Sales'].sum().reset_index()

    fig = px.line(
        daily_sales,
        x='Date',
        y='Sales',
        title=f"Pink Morsel Sales Over Time - {selected_region.capitalize()} Region" if selected_region != 'all' else "Pink Morsel Sales Over Time (All Regions)",
        labels={'Sales': 'Total Sales ($)', 'Date': 'Date'},
    )

    fig.add_vline(x="2021-01-15", line_dash="dash", line_color="red")
    fig.add_annotation(
        x="2021-01-15",
        y=max(daily_sales['Sales']),
        text="Price Increase",
        showarrow=True,
        arrowhead=1
    )
    return fig

if __name__ == '__main__':
    app.run(debug=True)
