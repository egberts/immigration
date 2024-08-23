#
# Badly thought that sankey.update() would handle a single datapoint update
# It doesn't: still requires the entire dataset for each 'label', 'value', 'x', 'y'
#
#  BOTCHED
import plotly
my_domain = plotly.graph_objs.sankey.Domain()
my_domain.row = 2
my_domain.column = 2
my_domain.x = [1, 0]
my_domain.y = [0, 1]

# Lone link
my_link = plotly.graph_objs.sankey.Link(
    label='State Transition',
    source=0,
    target=1,
    value=50
)

# Double node
my_node_labels = ['Label A', 'Label B']
my_node_xaxis = [0, 1]
my_node_yaxis = [0, 0]
my_nodes = plotly.graph_objs.sankey.Node(
    label=my_node_labels,
#    x=my_node_xaxis,
#    y=my_node_yaxis
    )
my_sankey_data = plotly.graph_objs.Sankey(domain=my_domain, node=my_nodes, link=my_link)
my_sankey_data.arrangement = 'freeform'

my_layout = plotly.graph_objs.Layout()
# my_layout.height = 744
# my_layout.width = 1408
my_layout.margin = {'b': 0, 'l':25, 'r': 75, 't': 70}
my_layout.selectdirection = 'any'
fig = plotly.graph_objs.Figure(data=my_sankey_data, layout=my_layout)
fig.show()