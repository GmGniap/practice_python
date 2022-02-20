import dash 
import dash_cytoscape as cyto
#import dash_html_components as html
from dash import html
#import dash_core_components as dcc
from dash import dcc
from dash.dependencies import Output, Input 
import pandas as pd
from pandas.io import json 
import plotly.express as px
import json 

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, title="First Testing")


# df = pd.DataFrame(
#     {
#         "Fruit" : ["A","B","C"],
#         "Amount" : [4,1,3],
#         "City": ["Ygn","Monywa","Mdy"]
#     }
# )
# fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")


# app.layout = html.Div(
#     children=[
#         html.H1(children="Hello Dash"),
#         html.Div(children='''
#             Dash : Web Application
#         '''),
#     dcc.Graph(
#         id='example',
#         figure = fig 
#     )
#     ]
# )

df = pd.read_csv("./skill_tree.csv")
with open("./test.json", "r") as f:
    data = json.load(f)
app.layout = html.Div([ 
    html.Div([ 
        dcc.Dropdown(
            id = 'dropdown_update',
            value = 'grid',
            clearable = False,
            options = [
                {'label': name.capitalize(), 'value': name}
                for name in df.Parent.unique()
            ]
        ),
        cyto.Cytoscape(
            id = 'skill-tree',
            layout = {'name': 'breadthfirst'},
            style={'width': '100%', 'height':'500px'},
            elements= data
        )
    ], className = 'test'),

    html.Div([ 
        dcc.Graph(id='my-graph')
    ], className = 'test'),
], className = 'row')

@app.callback(
    Output('skill-tree', 'elements'),
    [Input('skill-tree', 'tapNodeData')],
    State('skill-tree', 'elements'),
)
def generate_elements(nodeData, elements):
    if not nodeData:
        return defau
@app.callback(
    Output('my-graph', 'figure'),
    Input('skill-tree', 'tapNodeData'),
)
def update_nodes(data):
    if data is None:
        dff = df.copy()
        dff.loc[dff.Child == 'Nextjs', 'color'] = 'yellow'
        fig = px.bar(dff,x='Child',y='Track')
        fig.update_traces(marker={'color':dff['color']})
        return fig 
    else:
        print(data)
        dff = df.copy()
        dff.loc[dff.Child == data['label'], 'color'] = "yellow"
        fig = px.bar(dff,x='Child',y='Track')
        fig.update_traces(marker={'color':dff['color']})
        return fig


if __name__ == '__main__':
    app.run_server(debug=True)