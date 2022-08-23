from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
from plotly.offline import plot
import plotly.express as px
import pandas as pd
from home.models import HR

mylist = []
for i in HR.objects.all():
    mylist.append(list(i.get_data()))
df = pd.DataFrame(mylist, columns = ['Name', 'Department','Salary','Age'])
dep_options = []
for dep in df['Department'].unique():
    dep_options.append({'label': dep, 'value': dep})



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

colors = {
    'background': 'white',
    'text': '#7FDBFF'
}


app = DjangoDash('HRDashboard', external_stylesheets=external_stylesheets)

# *******************************************************************************************************

# Structure the layout for the Dashboard
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[

    html.H1(
        children='Django & Plotly Dash Integration',
        style={
            'textAlign': 'center',
            'color': 'red'
        }
    ),

    html.Br(),


    html.Div([

        html.Div([

            html.Div([
                html.H1(
                children='Age Distribution in Each Department',
                style={
                    'color': 'blue',
                    'font-size': 30,
                    
                }
            ),
                dcc.Graph(id='age_distribution' )
            ],style = {'width': '80%',"border":"2px black solid"}),

            html.Div([
                html.Label(['Select the Department ID']),
                dcc.Dropdown(
                    id='dep-picker',
                    options=dep_options,
                    value= 1,
                    placeholder="Select the Department",
                    # multi=False,

                    style = {'width': '50%',  'align-items': 'center', 'justify-content': 'center'}
                ),
            ]),

        ],  className='six columns'),

        html.Div([

            html.Div([
                html.H1(
                children='Salary Distribution in Each Department',
                style={
                    'color': 'blue',
                    'font-size': 30,
                    
                }
            ),
                dcc.Graph(id='salary_distribution' )
            ],style = {'width': '80%',"border":"2px black solid"}),

            html.Div([
                html.Label(['Select the Department ID']),
                dcc.Dropdown(
                    id='dep-picker1',
                    options=dep_options,
                    value= 1,
                    placeholder="Select the Department",
                    # multi=False,

                    style = {'width': '50%',  'align-items': 'center', 'justify-content': 'center'}
                ),
            ]),

        ],  className='six columns'),

    ], className='row'),
  

       
])

# *******************************************************************************************************

# Generate the interactive Plots


##Call backs for the Plotly Plots

# @app.callback(
#     Output(component_id='age_distribution', component_property='figure'),
#     Output(component_id='salary_distribution', component_property='figure'),
    
#     [Input(component_id='dep-picker', component_property='value'),
#     Input(component_id='dep-picker1', component_property='value'),
#     ]  
    
# )
# *******************************************************************************************************

##Updating the plots

# Plot to show Age Distribution wrt each Department
@app.callback(
    Output(component_id='age_distribution', component_property='figure'),
    [Input(component_id='dep-picker', component_property='value')]   
)
def update_age_histogram(selected_dep):

    filtered_df = df[df['Department'] == selected_dep]
    hist_data = [go.Histogram(x=filtered_df['Age'],
                              marker=dict(color='yellow'))]
    layout = go.Layout(paper_bgcolor='#000080')
    return {'data': hist_data, 'layout': layout}

# Plot to show Salary Distribution wrt each Department

@app.callback(
    Output(component_id='salary_distribution', component_property='figure'),
    [Input(component_id='dep-picker1', component_property='value')]   
)
def update_salary_histogram(selected_dep):

    filtered_df = df[df['Department'] == selected_dep]
    hist_data = [go.Histogram(x=filtered_df['Salary'],
                              marker=dict(color='yellow'))]
    layout = go.Layout(paper_bgcolor='#000080')
    return {'data': hist_data, 'layout': layout}

# *******************************************************************************************************


# Run the Server
if __name__ == '__main__':
    app.run_server(debug=True)