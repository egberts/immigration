#
#  Exercising the addition of datapoint of each node

import plotly

my_node = plotly.graph_objs.sankey.Node()
my_node.update(
    label=['Label A', 'Label B'],
    color='red',
    x=[0, 1],
    y=[0, 0],
    overwrite=False,
    thickness=1,
    )
my_links = plotly.graph_objs.sankey.Link()
my_links.value = [50]
my_links.source = [0]
my_links.target = [1]
print('node: ', my_node)
my_sankey_data = plotly.graph_objs.Sankey(node=my_node, link=my_links)
fig = plotly.graph_objs.Figure(data=my_sankey_data)

fig.show()
