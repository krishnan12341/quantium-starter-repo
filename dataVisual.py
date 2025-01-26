import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as plotly

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
        dcc.Graph(
            id = 'sales-line-chart',

            style = {'width': '80%', 'margin': 'auto'}
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
    Input('sales-line-chart', 'id')
)

def update_chart(_):
    image = plotly.line(
        pinkMorsel,
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

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)