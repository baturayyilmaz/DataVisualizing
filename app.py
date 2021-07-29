# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from plotly import graph_objs as go
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#################################################
df_joined = pd.read_csv("NYC-LOC.csv")  # Taking the dataset, prepared in Download_Filter.py program
#################################################
mapbox_access_token = "pk.eyJ1IjoicGxvdGx5bWFwYm94IiwiYSI6ImNqdnBvNDMyaTAxYzkzeW5ubWdpZ2VjbmMifQ.TXcBE-xg9BFdV2ocecc_7g"

app.layout = html.Div(children=[
    html.Div(children=[dcc.Input(id='state', type='number')], style={'display': 'none'}), # the invisible div. Used for passing state between callbacks
    html.H1(children=['CS405 - Data Visualization Project'], style={'text-align': 'center'}),
    html.Div(children='Baturay Yılmaz - 239333', style={'text-align': 'center', 'color': 'red'}),

    html.Div( # plotting the map
        dcc.Graph(
                id='map',
                figure=go.Figure(
                    data=[
                        go.Scattermapbox(
                            lat=df_joined[df_joined['Pickup_Hour'] == i]['latitude'],
                            lon=df_joined[df_joined['Pickup_Hour'] == i]['longitude'],
                            mode='markers',
                            name=str(i) + ":00",
                            hovertemplate='<b>Lat</b>: %{lat}<br><b>Lon</b>: %{lon}',
                            marker=go.scattermapbox.Marker(
                                size=12
                            ),
                            text=df_joined[df_joined['Pickup_Hour'] == i]['Pickup_Hour']
                        )for i in df_joined.Pickup_Hour.unique()
                    ],
                    layout=go.Layout(
                        title="Pickup Locations Of Passengers on 01/01/2019",
                        hovermode='closest',
                        height=600,
                        mapbox=go.layout.Mapbox(
                            style="dark",
                            accesstoken=mapbox_access_token,
                            bearing=0,
                            center=go.layout.mapbox.Center(
                                lat=40.7185670947,
                                lon=-73.882191923
                            ),
                            pitch=0,
                            zoom=10,
                        )
                    )
                )
        )
    ),
    html.Div([ # Dropdown menu for filtering the pie chart.
            html.Div([
                dcc.Dropdown(
                    id='pie-chart-filter',
                    placeholder="Select a passenger count to filter the pie chart..."

                )
            ], style={'width': '40%', 'float': 'right', 'display': 'inline-block', 'margin-right': '175px'})
    ]),

    html.Div(children=[
        html.Div(children=[
            dcc.Graph( # plotting bar chart.
                id='bar-chart',
                figure={
                    'data': [
                        {'x': ["0:00-1:00"], 'y': [(df_joined.Pickup_Hour == 0).sum()], 'type': 'bar', 'name': '0:00'},
                        {'x': ["1:00-2:00"], 'y': [(df_joined.Pickup_Hour == 1).sum()], 'type': 'bar', 'name': '1:00'},
                        {'x': ["2:00-3:00"], 'y': [(df_joined.Pickup_Hour == 2).sum()], 'type': 'bar', 'name': '2:00'},
                        {'x': ["3:00-4:00"], 'y': [(df_joined.Pickup_Hour == 3).sum()], 'type': 'bar', 'name': '3:00'},
                        {'x': ["4:00-5:00"], 'y': [(df_joined.Pickup_Hour == 4).sum()], 'type': 'bar', 'name': '4:00'},
                        {'x': ["5:00-6:00"], 'y': [(df_joined.Pickup_Hour == 5).sum()], 'type': 'bar', 'name': '5:00'},
                        {'x': ["6:00-7:00"], 'y': [(df_joined.Pickup_Hour == 6).sum()], 'type': 'bar', 'name': '6:00'},
                        {'x': ["7:00-8:00"], 'y': [(df_joined.Pickup_Hour == 7).sum()], 'type': 'bar', 'name': '7:00'},
                        {'x': ["8:00-9:00"], 'y': [(df_joined.Pickup_Hour == 8).sum()], 'type': 'bar', 'name': '8:00'},
                        {'x': ["9:00-10:00"], 'y': [(df_joined.Pickup_Hour == 9).sum()], 'type': 'bar', 'name': '9:00'},
                        {'x': ["10:00-11:00"], 'y': [(df_joined.Pickup_Hour == 10).sum()], 'type': 'bar', 'name': '10:00'},
                        {'x': ["11:00-12:00"], 'y': [(df_joined.Pickup_Hour == 11).sum()], 'type': 'bar', 'name': '11:00'},
                        {'x': ["12:00-13:00"], 'y': [(df_joined.Pickup_Hour == 12).sum()], 'type': 'bar', 'name': '12:00'},
                        {'x': ["13:00-14:00"], 'y': [(df_joined.Pickup_Hour == 13).sum()], 'type': 'bar', 'name': '13:00'},
                        {'x': ["14:00-15:00"], 'y': [(df_joined.Pickup_Hour == 14).sum()], 'type': 'bar', 'name': '14:00'},
                        {'x': ["15:00-16:00"], 'y': [(df_joined.Pickup_Hour == 15).sum()], 'type': 'bar', 'name': '15:00'},
                        {'x': ["16:00-17:00"], 'y': [(df_joined.Pickup_Hour == 16).sum()], 'type': 'bar', 'name': '16:00'},
                        {'x': ["17:00-18:00"], 'y': [(df_joined.Pickup_Hour == 17).sum()], 'type': 'bar', 'name': '17:00'},
                        {'x': ["18:00-19:00"], 'y': [(df_joined.Pickup_Hour == 18).sum()], 'type': 'bar', 'name': '18:00'},
                        {'x': ["19:00-20:00"], 'y': [(df_joined.Pickup_Hour == 19).sum()], 'type': 'bar', 'name': '19:00'},
                        {'x': ["20:00-21:00"], 'y': [(df_joined.Pickup_Hour == 20).sum()], 'type': 'bar', 'name': '20:00'},
                        {'x': ["21:00-22:00"], 'y': [(df_joined.Pickup_Hour == 21).sum()], 'type': 'bar', 'name': '21:00'},
                        {'x': ["22:00-23:00"], 'y': [(df_joined.Pickup_Hour == 22).sum()], 'type': 'bar', 'name': '22:00'},
                        {'x': ["23:00-0:00"], 'y': [(df_joined.Pickup_Hour == 23).sum()], 'type': 'bar', 'name': '23:00'},
                    ],
                    'layout': {
                        'title': 'Number Of Taxi PickUps With Respect to Hours',
                        'clickmode': 'event+select'
                    }
                }
            )], style={'display': 'inline-block'}
        ),
        html.Div(children=[
            dcc.Graph( # pie-chart will be plotted in callbacks
                id='interactive-pie-chart',
            )], style={'display': 'inline-block'}
        ),
    ], style={'display': 'inline-block'}),
])


@app.callback(
    [dash.dependencies.Output('pie-chart-filter', 'options'),
     dash.dependencies.Output('pie-chart-filter', 'value'),
     dash.dependencies.Output('state', 'value')],
    [dash.dependencies.Input('bar-chart', 'clickData')]
)
def update_figure(clickData):
    if clickData is not None:  # if something is clicked.
        time_interval = clickData["points"][0]["x"]  # click data is a dictionary, which has a list in its "points" key and that list has another dictionary in its 0th index
        time = time_interval.partition(":")[0]  # time_interval is string. If it was "1:00-2:00", now time is "1"
        time = int(time)

        temp_pd_series2 = df_joined[df_joined["Pickup_Hour"] == time]["passenger_count"].value_counts()
        indices = list(temp_pd_series2.index.values)
        indices.sort()
        options = [{'label': i, 'value': i} for i in indices] # this will the options of dropdown.
        return options, None, time

    else:  # if something is not clicked. Then we are goint to display it for 0:00
        temp_pd_series2 = df_joined[df_joined["Pickup_Hour"] == 1]["passenger_count"].value_counts()
        indices = list(temp_pd_series2.index.values)
        indices.sort()
        options = [{'label': i, 'value': i} for i in indices]
        return options, None, 0


@app.callback(
    dash.dependencies.Output('interactive-pie-chart', 'figure'),
    [
        dash.dependencies.Input('pie-chart-filter', 'value'), # value from dropdown menu
        dash.dependencies.Input('state', 'value') # takes the state from invisible div
    ]
)
def filter_pie_chart(filter_value, state):
    if filter_value is None:
        time = state

        temp_pd_series = df_joined[df_joined["Pickup_Hour"] == time]["borough"].value_counts()
        labels = list(temp_pd_series.index.values)
        values = list(temp_pd_series.values)
        title = "Percentage of Pickups with Respect to Boroughs at " + str(time) + ":00"

        return go.Figure(
                    data=[go.Pie(
                        labels=labels,
                        values=values,
                    )],
                    layout=go.Layout(
                        title=title
                    )
                )

    else: # a value is being set in dropdown. So, we should filter it.
        time = state

        df_temp = df_joined[df_joined["Pickup_Hour"] == time]
        df_temp = df_temp[df_temp["passenger_count"] == filter_value] # filtering according to value of the dropdown
        temp_pd_series = df_temp["borough"].value_counts()
        labels = list(temp_pd_series.index.values)
        values = list(temp_pd_series.values)
        title = "Percentage of Pickups with Respect to Boroughs at " + str(time) + ":00 where Passenger Count is " + str(filter_value)

        return go.Figure(
                    data=[go.Pie(
                        labels=labels,
                        values=values,
                    )],
                    layout=go.Layout(
                        title=title,
                        titlefont={'size': 15}
                    )
                )


if __name__ == '__main__':
    app.run_server(debug=True)
