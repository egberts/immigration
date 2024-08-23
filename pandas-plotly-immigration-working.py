# Sankey chart for US Immigration & Deportation 2023
#
# Sources:
# * https://www.uscis.gov/citizenship-resource-center/naturalization-statistics
# * https://www.uscis.gov/tools/reports-and-studies/immigration-and-citizenship-data/eligible-to-naturalize-dashboard
# * https://www.uscis.gov/military/military-naturalization-statistics
# imports
import errno
import pprint
import sys
import textwrap

import pandas as pd
import plotly
from plotly.offline import download_plotlyjs, init_notebook_mode, iplot

import my_go_utils


def custom_wrap(s, width=13):
    return "<br>".join(textwrap.wrap(s, width=width))


plotly.offline.init_notebook_mode(connected=True)
my_domain = plotly.graph_objs.sankey.Domain(
    x=(1, 0),
    y=(0, 1),
    row=4,
    column=9
)
my_go_utils.print_domain(my_domain)

# Nodes & links
x = plotly.graph_objs.sankey.Node()

nodes = [
    ['ID', 'Label', 'Color', 'X', 'Y'],
    [0, 'The World', 'darkorchid', .09, 0.3825],

    [1, 'Gotaways 600,000', 'red', 0.48, 0.21],
    [96, custom_wrap('Gotaway 600,000', 12), 'red', 1, 0.48],
    [2, 'Entrances<br>3,300,004', '#7f8600', 0.18, .42],
    [
        4,
        custom_wrap('Affirmative Asylum Applications'),
        'darkorange', 0.18, .75
    ],
    [
        3,
        custom_wrap('Humanitarian Parole'),
        'darkorange', 0.18, .85
    ],
    [
        11,
        custom_wrap('Northern Border Encounters'),
        '#4994CE', .27, .245
    ],
    [
        12,
        custom_wrap('Southern Border Encounters'),
        '#8A5988', .27, .38
    ],
    [
        13,
        custom_wrap('Western Border Encounters'),
        '#449E9E', .27, .52
    ],
    [
        14,
        custom_wrap('Eastern Border Encounters'),
        '#7FC241', .27, .53
    ],
    [
        15,
        custom_wrap('Other Border Encounters'),
        '#D3D3D3', .27, .54
    ],

    [20, 'Encounters', 'darkgray', .38, .385],

    [30, 'Title 42: 565,000', 'red', .48, .2775],
    [31, 'Title 8<br>965,000', '#7f8600', .48, .415],
    [
        97,
        custom_wrap('Deported (Removal Order)', 13),
        'red',
        .79,
        .30
    ],
    [45, 'Paroled', 'orange', .56, .39],
    [
        99,
        custom_wrap('Proceedings (Ongoing/Temporary Relief) 28,000,000', 15),
        'yellow',
        0.79,
        0.64
    ],
    [42, 'NTA (Detained)', 'red', .56, .54],
    #[41, 'Expedited Retained', 'blue', .4, .4],
    [
        43,
        custom_wrap('NTA in Court (Released)', 15),
        'goldenrod', .56, .48
    ],
    [44, 'Other*', 'purple', .56, .63],
    [49, 'Military', 'blue', .56, .66],

    [47, 'Denied', 'black', .48, .535],
    [48, 'Added to Backlog', 'lightsalmon', .48, .69],
    [46, 'Approved', 'purple', .38, .75],

    [50, 'Enter Processing', 'orange', .64, .6],

    [60, 'Processed', 'purple', .68, .5],

    [70, 'Voluntary Departure', 'blue', .72, .4],
    [71, 'Relief Denied', 'red', .72, .43],
    [72, 'Relief Granted in Court', 'green', .72, .88],
    [73, 'Case altered', 'yellow', .72, .76],

    [98, 'Formal Relief (Granted)', 'green', .72, .90],

    [100, 'Green Card<br>878,500', 'lightgreen', .9, .7],
    [110, 'Citizenship<br>878,500', 'lightblue', 1, .6],
]

# links with your data
links = [
    ['Source', 'Target', 'Value', 'Link Color', 'Label'],

    [0, 1, 600000, 'lightpink', 'Gotaways<br>600,000'],
    [0, 2, 2500000, 'darkorange', 'Entrances'],
    [0, 3, 240000, 'darkgray', 'Humanitarian Paroles'],
    [0, 4, 464000, 'darkgray', custom_wrap('Affirmative Asylum Applications')],

    # Entrance (pre-government transitory)
    [1, 96, 600000, 'lightpink', '"Gotaways"<br>600,000'],  # entrances to gotaways

    [2, 11, 1, 'darkgray', 'Northern Border Entrance'],
    [2, 12, 2500000, '#8A5988', 'Southern Border Entrance'],
    [2, 13, 1, 'darkgray', 'Western Border Entrance'],
    [2, 14, 1, 'darkgray', 'Easter Border Entrance'],
    [2, 15, 1, 'darkgray', 'Other Border Entrance'],

    [2, 0, 800000, 'lightgreen', 'Repeat<br>Multiple Attempts'],
    #
    [11, 20, 1, 'darkgray', 'Northern Border'],
    [12, 20, 2500000, 'darkgray', 'Southern Border'],
    [13, 20, 1, 'darkgray', 'Western Border'],
    [14, 20, 1, 'darkgray', 'Eastern Border'],
    [15, 20, 1, 'darkgray', 'Other borders'],

    [3, 99, 240000, 'lightgreen', 'Humanitarian Parole'],

    [4, 46, 18000, 'lightblue', 'Approved Affirmative Asylum Applications'],
    [4, 47, 6000, 'red', 'Denied Affirmative Asylum Applications'],
    [4, 48, 440000, 'orange', 'Added to Backlog'],

    [20, 30, 565000, 'lightsalmon', 'Title 42'],  # Title 42
    [20, 31, 1900000, 'lightgray', 'Title 8'],  # Title 8

    [30, 97, 565000, 'lightsalmon', 'EEEE'],  # Title 42

    [31, 97, 135000, 'lightsalmon', 'Voluntary Departure'],
    [31, 97, 230000, 'red', 'Expedited Removal'],
    [31, 42, 230000, 'orange', 'Notice To Appear (Detained)'],
    [31, 43, 965000, 'goldenrod', 'Notice to Appear in Court (Released)'],
    [31, 45, 350000, 'darkorange', 'Paroled'],

    [42, 50, 230000, 'orange', 'NTA (Detained)'],
    [43, 50, 965000, 'goldenrod', 'Immigration Court'],
    [44, 50, 250000, 'purple', 'Others'],
    [45, 97, 350000, 'red', 'Paroled'],
    [46, 98, 18000, 'rgba(127, 194, 65, 0.2)', 'Approved'],
    [47, 97, 18000, 'red', 'Denied'],
    [48, 99, 415000, 'orange', 'AAA Added to Backlog'],
    [49, 50, 12140, 'blue', 'US Military'],

    [50, 60, 100000, 'gray', 'Processed'],
    [50, 99, 1350000, 'yellow', 'Added to Backlog'],

    [60, 70, 2500, 'lightsteelblue', 'Voluntary Departure'],
    [60, 71, 45000, 'darkred', 'Relief Denied'],
    [60, 72, 2000, 'green', 'Relief Granted in Court'],
    [60, 73, 50000, 'gray', 'Case altered'],

    [70, 97, 2500, 'lightsalmon', 'Voluntary Departure'],
    [71, 97, 45000, 'lightsalmon', 'Relief Denied'],

    [72, 100, 2000, 'green', 'Relief Accepted'],
    [73, 50, 50000, 'goldenrod', 'Case altered'],
    [97, 0, 1345500, 'lightgreen', 'Deported'],

    [98, 100, 18000, 'yellowgreen', 'Formal Relief'],
    [99, 100, 600000, 'lightgreen', 'Naturalized'],
    # [99, 31, 28000000, 'yellowgreen', 'WAITING'],  # Uncomment for a BIG surprise!
    [100, 110, 878500, 'lightblue', 'Citizenship'],
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
my_link = plotly.graph_objs.sankey.Link(
    arrowlen=15,
    source=df_links['Source'].dropna(axis=0, how='any'),
    target=df_links['Target'].dropna(axis=0, how='any'),
    value=df_links['Value'].dropna(axis=0, how='any'),
    color=df_links['Link Color'].dropna(axis=0, how='any'),
    label=df_links['Label'].dropna(axis=0, how='any')
)

my_node = plotly.graph_objs.sankey.Node(
    color=df_nodes['Color'].dropna(axis=0, how='any'),
    label=df_nodes['Label'].dropna(axis=0, how='any'),
    x=df_nodes['X'].dropna(axis=0, how='any'),
    y=df_nodes['Y'].dropna(axis=0, how='any'),
    line=dict(color='black', width=1),
    pad=10,
    thickness=30,
    hoverinfo=None  # 'none', 'skip'
    # my_node.groups = 5
    # my_node.align = 'right'  # we have too many floating nodes, need node-grouping assist
)

my_sankey = plotly.graph_objs.Sankey(
    # Arrangement, enables end-user to use mouse to repositions node(s).
    arrangement='freeform',  # 'perpendicular', 'snap', 'fixed', 'freeform'
    orientation='h',
    valueformat='.0f',
    domain=my_domain,
    link=my_link,
    node=my_node
)

my_xaxis = plotly.graph_objs.layout.XAxis(
    showgrid=False,  # thin lines in the background
    zeroline=False,  # thick line at x=0
    visible=False,  # numbers below
)
my_yaxis = plotly.graph_objs.layout.YAxis(
    showgrid=False,  # thin lines in the background
    zeroline=False,  # thick line at x=0
    visible=False,  # numbers below
)
my_margin = plotly.graph_objs.layout.Margin(l=25, r=75, t=70, b=0)

text_font = plotly.graph_objs.layout.Font(
    size=24
)
title_font = plotly.graph_objs.layout.Font(
    size=32
)
my_title = plotly.graph_objs.layout.Title(
    skip_invalid=True,
    text="US Border Encounters & Enforcement 2023",
    font=title_font,
)

my_layout = plotly.graph_objs.Layout(
    title=my_title,
    titlefont={'size': 32},  # layout.title.Font().size is broken for `.size`
    font=text_font,
    margin=my_margin,
    xaxis=my_xaxis,
    yaxis=my_yaxis,
    autosize=False,
    selectdirection='any',  # 'h', 'v', 'any'
    width=640 * 3.2,
    height=480 * 2.2,
    plot_bgcolor='rgba(0,0,0,0)',
    ###autosize=True,  # Weird, didn't get take by Sankey() class
)

my_frame = plotly.graph_objs.Frame()

fig = plotly.graph_objs.Figure(
    data=[my_sankey],
    layout=my_layout,
    skip_invalid=False,
    frames=[my_frame]
)
# could have used fig.add_sankey(link=())

# Annotate up the chart
for x_coordinate, column_name in enumerate(["Entrances", "Encounters", "Court Processing", "End Results"]):
    fig.add_annotation(
        x=x_coordinate,
        y=0.95,
        xref="x",
        yref="paper",
        text=column_name,
        showarrow=False,
        font=dict(
            # family="Courier New, monospace",
            size=24,
            color="black"
        ),
        align="center",
    )
# To slap annotations all over the char, use following examples
fig.add_annotation(x=0.24, y=0.74, text='8', showarrow=False)
fig.add_annotation(x=0.25, y=0.75, text='<a href="https://egbert.net/">8</a>', showarrow=False)
# fig.add_annotation(x=0.75, y=0.25, text='4', textangle=-90, showarrow=False)

plotly.offline.plot(fig, show_link=False)

#fig.show()
#fig.write_image(file="/tmp/panda-plotly-test1.png")

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(fig)

# plotly.io.to_json(fig))
# iplot(fig, validate=False)  # Jupyter Notebook
