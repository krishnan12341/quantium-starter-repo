import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as p

formattedData = './outputFiles/formatted_sales_output_file.csv'
df = pd.read_csv(formattedData)

df['Date'] = pd.to_datetime(df['Date'])
pinkMorsel = df.sort_values(by = 'Date')

compareDate = pd.to_datetime('2021-01-15')
beforePrice = pinkMorsel[pinkMorsel['Date'] < compareDate]
afterPrice = pinkMorsel[pinkMorsel['Date'] >= compareDate]
app = dash.Dash(__name__)

app.layout = html.Div(
    style={
        'backgroundColor': '#0ECAE9',
        'fontFamily': 'Arial',
        'color': '#E90EDE',
        'padding': '13px',
        'width': '100%',
        'height': '100%',
        'margin': '0',
        'display': 'flex',
        'flexDirection': 'column',
        'alignItems': 'center',
        'justifyContent': 'center',
    },
    children=[
        html.Link(
            href = "https://fonts.googleapis.com/css2?family=Sixtyfour+Convergence&display=swap",
            rel = "stylesheet"
        ),
        html.H1(
            "Soul Foods Sales Visualiser",
            style = {'textAlign': 'center', 'fontSize': '36px'}
        ),
        html.H2(
            "Pink Morsel Sales",
            style = {'textAlign': 'center', 'fontSize': '28px'}
        ),
        html.Div(
            style = {'marginBottom': '20px', 'textAlign': 'center'},
            children =[
                html.Label(
                    "Filter by Region:",
                    style = {'fontSize': '18px', 'color': '#FFFFFF', 
                    'marginRight': '10px'
                    }
                ),
                dcc.RadioItems(
                    id = 'region-filter',
                    options = [
                        {'label': 'North', 'value': 'north'},
                        {'label': 'East', 'value': 'east'},
                        {'label': 'South', 'value': 'south'},
                        {'label': 'West', 'value': 'west'},
                        {'label': 'All', 'value': 'all'}
                    ],
                    value = 'all',
                    labelStyle = {'display': 'inline-block', 'marginRight': '10px', 
                    'color': '#FFFFFF'},
                    style = {'fontSize': '16px'}
                )
            ]
        ),
        dcc.Graph(
            id = 'sales-line-chart',
            style = {'width': '80%', 'margin': 'auto', 'backgroundColor': '#FFFFFF', 'padding': '10px', 'borderRadius': '10px'}
        ),
        html.Label(
            "Comparison Date: January 15, 2021",
            style ={
                'textAlign': 'center',

                'display': 'block',
                'marginTop': '20px',
                'fontSize': '18px'
            }
        )
    ]
)

@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter', 'value')
)

def update_chart(selected_region):
    if selected_region == 'all':
        filter = pinkMorsel
    else:
        filter = pinkMorsel[pinkMorsel['Region'] == selected_region]

    image = p.line(
        filter,
        x = 'Date',
        y = 'Sales',
        color = 'Region',
        title = 'Pink Morsel Sales by Region',
        labels = {'Sales': 'Total Sales ($)', 'Date': 'Date'}
    )
    image.add_vline(x=compareDate, line_width=3, line_dash="dash", line_color="red")
    image.update_layout(
        title_font_size = 20,
        xaxis_title = "Date",
        yaxis_title = "Sales (USD)",
        legend_title = "Region"
    )
    return image

# Runs the app
if __name__ == '__main__':
    app.run_server(debug=True)