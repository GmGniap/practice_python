import dash 
import dash_cytoscape as cyto
#import dash_html_components as html
from dash import html
#import dash_core_components as dcc
from dash import dcc
from dash.dependencies import Output, Input, State
import pandas as pd
from pandas.io import json 
import plotly.express as px
import drc_lib as drc 
from csv import reader

cyto.load_extra_layouts()
app = dash.Dash(__name__, title="Second")

nodes = set()

following_node_dict = {}
following_edge_dict = {}

follower_node_dict = {}
follower_edge_dict = {}

cy_edges = []
cy_nodes = []

# Load data
with open('./sample_network.txt', 'r') as f:
    network_data = f.read().split('\n')

# We select the first 750 edges and associated nodes for an easier visualization
edges = network_data[:750]

# with open("./skill_tree.csv", "r") as f:
#     csv_reader = reader(f)
#     header = next(csv_reader)
#     if header != None:
        # print("Found Header!")
for edge in edges:
    # print(edge)

    # id_no,source,target,track = [edge[i] for i in range(len(edge))]
    # # print(source)
    # cy_edge = {
    #     'data': {
    #         'id': id_no, 'source': source, 'target':target
    #     }
    # }

    # cy_target = {
    #     'data':{
    #         'id': target, 'label': target
    #     }
    # }

    # cy_source = {
    #     'data' : {
    #         'id': source , 'label': source
    #     }
    # }
    if " " not in edge:
        continue
    
    source, target = edge.split(" ")

    cy_edge = {'data': {'id': source+target, 'source': source, 'target': target}}
    cy_target = {"data": {"id": target, "label": "User #" + str(target[-5:])}}
    cy_source = {"data": {"id": source, "label": "User #" + str(source[-5:])}}

    if source not in nodes:
        nodes.add(source)
        cy_nodes.append(cy_source)
    if target not in nodes:
        nodes.add(target)
        cy_nodes.append(cy_target)

    ## Process dictionary for child
    if not following_node_dict.get(source):
        following_node_dict[source] = []
    if not following_edge_dict.get(source):
        following_edge_dict[source] = []

    following_node_dict[source].append(cy_target)
    following_edge_dict[source].append(cy_edge)

    ## Process dict for Parent
    if not follower_node_dict.get(target):
        follower_node_dict[target] = []
    if not follower_edge_dict.get(target):
        follower_edge_dict[target] = []

    follower_node_dict[target].append(cy_source)
    follower_edge_dict[target].append(cy_edge)


genesis_node = cy_nodes[0]
genesis_node['classes'] = "genesis"
default_elements = [genesis_node]

default_stylesheet = [
    {
        "selector": 'node',
        'style': {
            "opacity": 0.65,
            'z-index': 9999
        }
    },
    {
        "selector": 'edge',
        'style': {
            "curve-style": "bezier",
            "opacity": 0.45,
            'z-index': 5000
        }
    },
    {
        'selector': '.followerNode',
        'style': {
            'background-color': '#0074D9'
        }
    },
    {
        'selector': '.followerEdge',
        "style": {
            "mid-target-arrow-color": "blue",
            "mid-target-arrow-shape": "vee",
            "line-color": "#0074D9"
        }
    },
    {
        'selector': '.followingNode',
        'style': {
            'background-color': '#FF4136'
        }
    },
    {
        'selector': '.followingEdge',
        "style": {
            "mid-target-arrow-color": "red",
            "mid-target-arrow-shape": "vee",
            "line-color": "#FF4136",
        }
    },
    {
        "selector": '.genesis',
        "style": {
            'background-color': '#B10DC9',
            "border-width": 2,
            "border-color": "purple",
            "border-opacity": 1,
            "opacity": 1,

            "label": "data(label)",
            "color": "#B10DC9",
            "text-opacity": 1,
            "font-size": 12,
            'z-index': 9999
        }
    },
    {
        'selector': ':selected',
        "style": {
            "border-width": 2,
            "border-color": "black",
            "border-opacity": 1,
            "opacity": 1,
            "label": "data(label)",
            "color": "black",
            "font-size": 12,
            'z-index': 9999
        }
    }
]

# ################################# APP LAYOUT ################################
styles = {
    'json-output': {
        'overflow-y': 'scroll',
        'height': 'calc(50% - 25px)',
        'border': 'thin lightgrey solid'
    },
    'tab': {'height': 'calc(98vh - 80px)'}
}

app.layout = html.Div([
    html.Div(className='eight columns', children=[
        cyto.Cytoscape(
            id='cytoscape',
            elements=default_elements,
            stylesheet=default_stylesheet,
            style={
                'height': '95vh',
                'width': '100%'
            }
        )
    ]),

    html.Div(className='four columns', children=[
        dcc.Tabs(id='tabs', children=[
            dcc.Tab(label='Control Panel', children=[
                drc.NamedDropdown(
                    name='Layout',
                    id='dropdown-layout',
                    options=drc.DropdownOptionsList(
                        'random',
                        'grid',
                        'circle',
                        'concentric',
                        'breadthfirst',
                        'cose',
                        'cose-bilkent',
                        'dagre',
                        'cola',
                        'klay',
                        'spread',
                        'euler'
                    ),
                    value='grid',
                    clearable=False
                ),
                drc.NamedRadioItems(
                    name='Expand',
                    id='radio-expand',
                    options=drc.DropdownOptionsList(
                        'followers',
                        'following'
                    ),
                    value='followers'
                )
            ]),

            dcc.Tab(label='JSON', children=[
                html.Div(style=styles['tab'], children=[
                    html.P('Node Object JSON:'),
                    html.Pre(
                        id='tap-node-json-output',
                        style=styles['json-output']
                    ),
                    html.P('Edge Object JSON:'),
                    html.Pre(
                        id='tap-edge-json-output',
                        style=styles['json-output']
                    )
                ])
            ])
        ]),

    ])
])


# ############################## CALLBACKS ####################################
@app.callback(Output('tap-node-json-output', 'children'),
              [Input('cytoscape', 'tapNode')])
def display_tap_node(data):
    return json.dumps(data, indent=2)


@app.callback(Output('tap-edge-json-output', 'children'),
              [Input('cytoscape', 'tapEdge')])
def display_tap_edge(data):
    return json.dumps(data, indent=2)


@app.callback(Output('cytoscape', 'layout'),
              [Input('dropdown-layout', 'value')])
def update_cytoscape_layout(layout):
    return {'name': layout}


@app.callback(Output('cytoscape', 'elements'),
              [Input('cytoscape', 'tapNodeData')],
              [State('cytoscape', 'elements'),
               State('radio-expand', 'value')])
def generate_elements(nodeData, elements, expansion_mode):
    if not nodeData:
        return default_elements

    # If the node has already been expanded, we don't expand it again
    if nodeData.get('expanded'):
        return elements

    # This retrieves the currently selected element, and tag it as expanded
    for element in elements:
        if nodeData['id'] == element.get('data').get('id'):
            element['data']['expanded'] = True
            break

    if expansion_mode == 'followers':

        followers_nodes = follower_node_dict.get(nodeData['id'])
        followers_edges = follower_edge_dict.get(nodeData['id'])

        if followers_nodes:
            for node in followers_nodes:
                node['classes'] = 'followerNode'
            elements.extend(followers_nodes)

        if followers_edges:
            for follower_edge in followers_edges:
                follower_edge['classes'] = 'followerEdge'
            elements.extend(followers_edges)

    elif expansion_mode == 'following':

        following_nodes = following_node_dict.get(nodeData['id'])
        following_edges = following_edge_dict.get(nodeData['id'])

        if following_nodes:
            for node in following_nodes:
                if node['data']['id'] != genesis_node['data']['id']:
                    node['classes'] = 'followingNode'
                    elements.append(node)

        if following_edges:
            for follower_edge in following_edges:
                follower_edge['classes'] = 'followingEdge'
            elements.extend(following_edges)

    return elements


if __name__ == '__main__':
    app.run_server(debug=True)