import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from data_fetcher import fetch_climate_data
from data_processor import process_data

def create_dashboard(server):
    app = dash.Dash(__name__, server=server, url_base_pathname='/dash/')

    app.layout = html.Div([
        dcc.Input(id='city-input', type='text', placeholder='Enter city name', style={'width': '400px', 'height': '40px', 'font-size': '20px'}),
        html.Button(id='submit-button', n_clicks=0, children='Submit', style={'background-color': '#007BFF', 'color': 'white', 'width': '120px', 'height': '50px', 'font-size': '20px'}),
        html.Div(style={'margin-top': '50px'}, children=[
        html.Div(id='climate-output',  style={'font-size': '24px'}),
        dcc.Graph(id='climate-graph')
    ])
    ])

    @app.callback(
        [Output('climate-output', 'children'),
         Output('climate-graph', 'figure')],
        [Input('submit-button', 'n_clicks')],
        [Input('city-input', 'value')]
    )
    def update_output(n_clicks, value):
        if n_clicks > 0:
            data = fetch_climate_data(value)
            processed_data = process_data(data)

            if processed_data:
                output = f"Temperature: {processed_data['temperature']} K, Pressure: {processed_data['pressure']} hPa, Humidity: {processed_data['humidity']}%, Wind Speed: {processed_data['wind_speed']} m/s, Description: {processed_data['description']}"

                fig = go.Figure(data=[
                    go.Bar(name='Temperature', x=['Temperature'], y=[processed_data['temperature']]),
                    go.Bar(name='Pressure', x=['Pressure'], y=[processed_data['pressure']]),
                    go.Bar(name='Humidity', x=['Humidity'], y=[processed_data['humidity']]),
                    go.Bar(name='Wind Speed', x=['Wind Speed'], y=[processed_data['wind_speed']]),
                ])

                fig.update_layout(barmode='group')

                return output, fig
            else:
                return "City not found", {}
        return "", {}

    return app
