from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
from plotly.offline import plot
import plotly.express as px
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('SimpleExample', external_stylesheets=external_stylesheets)

def scatter():
		x1 = [1,2,3,4]
		y1 = [38, 35, 25, 45]

		trace = go.Scatter(
			x = x1,
			y = y1
		)
		layout = dict(
			title = 'Simple Graph',
			xaxis = dict(range=[min(x1),max(x1)]),
			yaxis = dict(range=[min(y1),max(y1)])
		)
		fig = go.Figure(data=[trace], layout=layout)
		plot_div = plot(fig, output_type='div', include_plotlyjs=False)
		return plot_div


app.layout = html.Div([
    html.Div([
        html.H1('Square Root Slider Graph'),
        dcc.Graph(id='slider-graph', animate=True, style={"backgroundColor": "#1a2d46", 'color': '#ffffff'}),
        dcc.Slider(
            id='slider-updatemode',
            marks={i: '{}'.format(i) for i in range(20)},
            max=20,
            value=2,
            step=1,
            updatemode='drag',
        ),
    ]),
])
@app.callback(
               Output('slider-graph', 'figure'),
              [Input('slider-updatemode', 'value')])
def display_value(value):


    x = []
    for i in range(value):
        x.append(i)

    y = []
    for i in range(value):
        y.append(i*i)

    graph = go.Scatter(
        x=x,
        y=y,
        name='Manipulate Graph'
    )
    layout = go.Layout(
        paper_bgcolor='#27293d',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(range=[min(x), max(x)]),
        yaxis=dict(range=[min(y), max(y)]),
        font=dict(color='white'),

    )
    return {'data': [graph], 'layout': layout}


