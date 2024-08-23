#
# https://stackoverflow.com/questions/69110226/plotly-sankey-diagram-aligning-nodes

import errno
import sys

import pandas as pd
import plotly.graph_objects as go

my_domain = go.sankey.Domain(x=(1, 0), y=(0, 1))

nodes = [
    ['ID', 'Label', 'Color', 'X', 'Y'],
    [12, 'PP', 'gray', 0.001, 0.201],
    [5, 'P', 'gray', 0.001, 0.581],
    [23, 'A', 'gray', 0.3, 0.421],
    [33, 'Y', 'gray', 0.6, 0.101],
    [11, 'Z', 'gray', 1, 0.081],
    [28, 'DD', 'gray', 1, 0.212],
    [9, 'BB', 'gray', 1, 0.248],
    [14, 'CC', 'gray', 1, 0.26],
    [26, 'AA', 'gray', 1, 0.27],

    [18, 'T', 'gray', 0.6, 0.34],
    [3, 'X', 'gray', 1, 0.32],
    [0, 'W', 'gray', 1, 0.41],
    [4, 'V', 'gray', 1, 0.46],
    [31, 'U', 'gray', 1, 0.47],

    [16, 'EE', 'gray', 0.6, 0.45],
    [10, 'GG', 'gray', 1, 0.49],
    [29, 'FF', 'gray', 1, 0.51],

    [20, 'Q', 'gray', 0.6, .47],
    [22, 'S', 'gray', 1, 0.51],
    [27, 'R', 'gray', 1, 0.52],

    [21, 'B', 'gray', 0, 0],
    [1, 'C', 'gray', 0, 0],
    [13, 'D', 'gray', 0, 0],
    [6, 'E', 'gray', 0, 0],
    [7, 'F', 'gray', 0, 0],

    [2, 'G', 'gray', 0, 0],
    [15, 'H', 'gray', 0, 0],
    [24, 'I', 'gray', 0.001, .765],
    [8, 'J', 'gray', 0.001, 0.841],
    [17, 'MM', 'gray', 0.001, 0.879],
    [30, 'O', 'gray', 0.001, 0.900],
    [19, 'M', 'gray', 0.601, 0.915],

    [32, 'K', 'gray', 0, 0],

    [25, 'L', 'gray', 0, 0],

]
links = [
    ['Source', 'Target', 'Value'],
    [23, 21, 2619.76],
    [23, 1, 1583.26],
    [23, 13, 1542.78],
    [23, 6, 287.44],
    [23, 7, 50.0],

    [23, 2, 722.1],
    [23, 15, 5133.69],
    [24, 23, 6544.0],
    [8, 23, 2563.35],
    [23, 32, 6576.59],

    [23, 25, 4314.0],
    [23, 19, 82.87],
    [30, 23, 650.0],
    [17, 23, 1773.68],
    [5, 23, 16723.0],

    [12, 23, 32297.7],
    [20, 27, 81.64],
    [20, 22, 266.92],
    [23, 20, 348.56],
    [18, 31, 388.57],

    [18, 4, 743.2],
    [18, 0, 5403.24],
    [18, 3, 5821.52],
    [23, 18, 12356.53],
    [33, 11, 12905.68],

    [33, 26, 316.12],
    [33, 9, 497.68],
    [33, 14, 354.42],
    [33, 28, 3830.44],
    [23, 33, 17904.34],

    [16, 29, 175.95],
    [16, 10, 1224.46],
    [23, 16, 1400.41]
]

# Remap the node IDs
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

# Renumber the node IDs in all links, both source and target
for this_idx in range(1, len(links)):
    old_source = links[this_idx][0]
    if old_source not in mapped_idx:
        print(f"Node {old_source} of Link Idx: {this_idx} is not found in nodes[].source")
        sys.exit(errno.ENOTBLK)
    new_source = mapped_idx.index(old_source)
    links[this_idx][0] = new_source

    old_target = links[this_idx][1]
    if old_target not in mapped_idx:
        print(f"Node {old_target} of Link Idx: {this_idx} is not found in nodes[].target")
        sys.exit(errno.ENOTBLK)
    new_target = mapped_idx.index(old_target)
    links[this_idx][1] = new_target

# Retrieve headers and build dataframes
nodes_headers = nodes.pop(0)  # take off the header row
links_headers = links.pop(0)  # take off the header row
df_nodes = pd.DataFrame(nodes, columns=nodes_headers)
df_links = pd.DataFrame(links, columns=links_headers)

# Sankey plot setup
my_link = go.sankey.Link(
    arrowlen=15,
    source=df_links['Source'].dropna(axis=0, how='any'),
    target=df_links['Target'].dropna(axis=0, how='any'),
    value=df_links['Value'].dropna(axis=0, how='any'),
    # color=df_links['Link Color'].dropna(axis=0, how='any'),
    # label=df_links['Label'].dropna(axis=0, how='any')
)

my_node = go.sankey.Node(
    label=df_nodes['Label'].dropna(axis=0, how='any'),
    line=dict(color='black', width=0.5),
    hoverinfo=None,  # 'none', 'skip'
    color="blue",
    pad=5,
    thickness=10,
    # color=df_nodes['Color'].dropna(axis=0, how='any'),
    x=df_nodes['X'].dropna(axis=0, how='any'),
    y=df_nodes['Y'].dropna(axis=0, how='any'),
)

my_sankey_data = go.Sankey(
    arrangement='freeform',
    domain=my_domain,
    orientation='h',
    valueformat='.0f',
    node=my_node,
    link=my_link,
)
fig = go.Figure(data=my_sankey_data)

# Do layout lastly
my_margin = go.layout.Margin(l=25, r=75, t=70, b=0)
my_xaxis = go.layout.XAxis(
    showgrid=False,  # thin lines in the background
    zeroline=False,  # thick line at x=0
    visible=False,  # numbers below
)
my_yaxis = go.layout.YAxis(
    showgrid=False,  # thin lines in the background
    zeroline=False,  # thick line at x=0
    visible=False,  # numbers below
)
fig.update_layout(
    title_text="Basic Sankey Diagram", font_size=8,
    margin=my_margin,
    autosize=False,
    xaxis=my_xaxis,
    yaxis=my_yaxis,
    selectdirection='any',  # 'h', 'v', 'any'
    width=640 * 2.2,
    height=480 * 1.55,
)
x = ['blue', 'red', 'white']
fig.update_traces(node_color = x)
fig.show()
# fig.write_html("test.html")
