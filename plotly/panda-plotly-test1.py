# imports
import errno
import pprint
import sys
import textwrap

import pandas as pd
import plotly


def custom_wrap(s, width=15):
    return "<br>".join(textwrap.wrap(s, width=width))


# import plotly.graph_objs as go
my_domain = plotly.graph_objs.sankey.Domain()
my_domain.x = (1, 0)
my_domain.y = (0, 1)
my_domain.row = 4
my_domain.column = 9
print("my_domain.plotly_name: ", my_domain.plotly_name)
print("my_domain.parent: ", my_domain.parent)
print("my_domain.figure: ", my_domain.figure)
print("my_domain.row: ", my_domain.row)
print("my_domain.column: ", my_domain.column)
print("my_domain.x: ", my_domain.x)
print("my_domain.y: ", my_domain.y)

# Nodes & links
nodes = [
    ['ID', 'Label', 'Color'],
    [1, custom_wrap('Gotaways 600,000', 12), 'red'],
    [96, custom_wrap('Gotaway 600,000', 12), 'red'],
    [2, 'Entrances', '#D4C1FA'],
    [
        3,
        custom_wrap('Humanitarian Parole', 15),
        'darkorange'
    ],
    [
        4,
        custom_wrap('Affirmative Asylum Applications', 15),
        'darkorange'
    ],

    [
        11,
        custom_wrap('Northern Border Encounters', 15),
        '#4994CE'
    ],
    [
        12,
        custom_wrap('Southern Border Encounters', 13),
        'darkorchid'
    ],
    [
        13,
        custom_wrap('Western Border Encounters', 15),
        '#449E9E'
    ],
    [
        14,
        custom_wrap('Eastern Border Encounters', 15),
        '#7FC241'
    ],
    [
        15,
        custom_wrap('Other Border Encounters', 15),
        '#D3D3D3'
    ],

    [20, 'Encounters', '#8A5988'],

    [30, 'Title 42', 'red'],
    [31, 'Title 8', 'green'],

    [41, 'Expedited Retained', 'blue'],
    [42, 'NTA (Detained)', 'red'],
    [
        43,
        custom_wrap('NTA in Court (Released)', 15),
        'goldenrod'
    ],
    [44, 'Other*', 'purple'],
    [45, 'Paroled', 'orange'],

    [46, 'Approved', 'purple'],
    [47, 'Denied', 'black'],
    [48, 'Added to Backlog', 'lightsalmon'],

    [50, 'Enter Processing', 'orange'],

    [60, 'Processed', 'purple'],

    [70, 'Voluntary Departure', 'blue'],
    [71, 'Relief Denied', 'red'],
    [
        72,
        custom_wrap('Relief Granted in Court', 15),
        'green'
    ],
    [73, 'Case altered', 'yellow'],

    [
        97,
        custom_wrap('Deported (Removal Order)', 15),
        'red'
    ],
    [98, custom_wrap('Formal Relief (Granted)', 15), 'green'],
    [99, custom_wrap('Proceedings (Ongoing/Temporary Relief)', 15), 'yellow'],
]

# links with your data
links = [
    ['Source', 'Target', 'Value', 'Link Color', 'Label'],

    # Entrance (pre-government transitory)
    [1, 96, 600000, 'lightpink', '"Gotaways"<br>600,000'],  # entrances to gotaways

    [2, 11, 0, 'darkgray', 'Northern Border Entrance'],
    [2, 12, 2500000, 'darkgray', 'Southern Border Entrance'],
    [2, 13, 0, 'darkgray', 'Western Border Entrance'],
    [2, 14, 0, 'darkgray', 'Easter Border Entrance'],
    [2, 15, 0, 'darkgray', 'Other Border Entrance'],

#    [2, 2, 800000, 'lightgreen', 'Repeat<br>Multiple Attempts'],
    #
    [11, 20, 0, 'darkgray', 'Northern Border'],
    [12, 20, 2500000, 'darkgray', 'Southern Border'],
    [13, 20, 0, 'darkgray', 'Western Border'],
    [14, 20, 0, 'darkgray', 'Eastern Border'],
    [15, 20, 0, 'darkgray', 'Other borders'],

    [3, 99, 240000, 'lightgreen', 'Humanitarian Parole'],

    [4, 46, 18000, 'lightblue', 'Approved Affirmative Asylum Applications'],
    [4, 47, 6000, 'red', 'Denied Affirmative Asylum Applications'],
    [4, 48, 440000, 'orange', 'Added to Backlog'],

    [20, 30, 565000, 'lightsalmon', 'Title 42'],  # Title 42
    [20, 31, 1900000, 'lightgreen', 'Title 8'],  # Title 8

    [30, 97, 565000, 'lightsalmon', 'EEEE'],  # Title 42

    [31, 97, 135000, 'lightsalmon', 'Voluntary Departure'],
    [31, 97, 230000, 'red', 'Expedited Removal'],
    [31, 42, 230000, 'red', 'Notice To Appear (Detained)'],
    [31, 43, 965000, 'goldenrod', 'Notice to Appear in Court (Released)'],
    [31, 45, 350000, 'orange', 'Paroled'],

    [42, 50, 230000, 'orange', 'NTA (Detained)'],
    [43, 50, 965000, 'goldenrod', 'Immigration Court'],
    [44, 50, 250000, 'purple', 'Others'],
    [45, 97, 350000, 'red', 'Paroled'],
    [46, 98, 18000, 'rgba(127, 194, 65, 0.2)', 'Approved'],
    [47, 97, 18000, 'red', 'Denied'],
    [48, 99, 415000, 'orange', 'AAA Added to Backlog'],

    [50, 60, 100000, 'gray', 'Processed'],
    [50, 99, 1350000, 'yellow', 'Added to Backlog'],

    [60, 70, 2500, 'lightsteelblue', 'Voluntary Departure'],
    [60, 71, 45000, 'darkred', 'Relief Denied'],
    [60, 72, 2000, 'green', 'Relief Granted in Court'],
    [60, 73, 50000, 'gray', 'Case altered'],

    [70, 97, 2500, 'lightsalmon', 'Voluntary Departure'],
    [71, 97, 45000, 'lightsalmon', 'Relief Denied'],
    [73, 99, 50000, 'lightyellow', 'Case altered'],
]

new_idx = 1
mapped_idx = []
for this_idx in range(1, len(nodes)):
    x = nodes[this_idx]
    if nodes[this_idx][0] in mapped_idx:
        print("Node[0] already done: ", nodes[this_idx])
        break
    # Training index
    old_idx: int = int(nodes[this_idx][0])
    # Remapping index
    mapped_idx.insert(new_idx, old_idx)
    # Remapping index
    nodes[this_idx][0] = new_idx
    new_idx = new_idx + 1

for this_idx in range(1, len(links)):
    old_source = links[this_idx][0]
    if old_source not in mapped_idx:
        print(f"Link Idx: {this_idx} is not found in nodes[].source")
        sys.exit(errno.ENOTBLK)
    new_source = mapped_idx.index(old_source)
    links[this_idx][0] = new_source

    old_target = links[this_idx][1]
    if old_target not in mapped_idx:
        print(f"Link Idx: {this_idx} is not found in nodes[].target")
        sys.exit(errno.ENOTBLK)
    new_target = mapped_idx.index(old_target)
    links[this_idx][1] = new_target

# Retrieve headers and build dataframes
nodes_headers = nodes.pop(0)  # take off the header row
links_headers = links.pop(0)  # take off the header row
df_nodes = pd.DataFrame(nodes, columns=nodes_headers)
df_links = pd.DataFrame(links, columns=links_headers)

# Sankey plot setup
my_link = plotly.graph_objs.sankey.Link()
my_link.arrowlen = 15
my_link.source = df_links['Source'].dropna(axis=0, how='any')
my_link.target = df_links['Target'].dropna(axis=0, how='any')
my_link.value = df_links['Value'].dropna(axis=0, how='any')
my_link.color = df_links['Link Color'].dropna(axis=0, how='any')
my_link.label = df_links['Label'].dropna(axis=0, how='any')

my_node = plotly.graph_objs.sankey.Node()
my_node.color = df_nodes['Color'].dropna(axis=0, how='any')
my_node.label = df_nodes['Label'].dropna(axis=0, how='any')
my_node.line = dict(color='black', width=1)
my_node.pad = 10
my_node.thickness = 30
my_node.hoverinfo = None  # 'none', 'skip'
#my_node.groups = 5
#my_node.align = 'right'  # we have too many floating nodes, need node-grouping assist
#my_node = dict(
#    pad=10,
#    # thickness = 30,
#    line=dict(
#        color="black",
#        width=0
#    ),
#    # align='right'  # we have too many floating nodes, need grouping support
#    label=df_nodes['Label'].dropna(axis=0, how='any'),
#    color=df_nodes['Color']
#)

my_sankey = plotly.graph_objs.Sankey()
my_sankey.arrangement = 'freeform'  # 'perpendicular', 'snap', 'fixed', 'freeform'
my_sankey.orientation = 'h'
my_sankey.valueformat = '.0f'
my_sankey.domain = my_domain
my_sankey.link = my_link
my_sankey.node = my_node

my_layout = plotly.graph_objs.Layout()
my_layout.title = "US Border Encounters & Enforcement 2022"
#my_layout.height = 772
my_layout.font = dict(size=16)

fig = plotly.graph_objs.Figure(data=[my_sankey], layout=my_layout)
# could have used fig.add_sankey(link=())
fig.layout = my_layout

fig.layout.xaxis = {
    'showgrid': False,  # thin lines in the background
    'zeroline': False,  # thick line at x=0
    'visible': False,  # numbers below
}
fig.layout.yaxis = {
    'showgrid': False,  # thin lines in the background
    'zeroline': False,  # thick line at x=0
    'visible': False,  # numbers below
}
fig.layout.autosize = True
#fig.layout.width = 640*1.8
#fig.layout.height = 480*1.55
fig.layout.plot_bgcolor = 'rgba(0,0,0,0)'
fig.layout.margin = {'l': 25, 'r': 75, 't': 70, 'b': 0}
for x_coordinate, column_name in enumerate(["Entrances", "Encounters", "Court Processing", "End Results"]):
    fig.add_annotation(
        x=x_coordinate,
        y=1.05,
        xref="x",
        yref="paper",
        text=column_name,
        showarrow=False,
        font=dict(
            # family="Courier New, monospace",
            size=16,
            color="black"
        ),
        align="center",
    )

fig.show()
fig.write_image(file="/tmp/panda-plotly-test1.png")

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(fig)

# plotly.io.to_json(fig))
# iplot(fig, validate=False)
