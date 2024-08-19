
import plotly.graph_objs as go

my_data = go.Sankey()
domain = go.sankey.Domain()
hl = go.sankey.Hoverlabel()
lgt = go.sankey.Legendgrouptitle()
link = go.sankey.Link()
node = go.sankey.Node()

my_arrangement = my_data.arrangement
my_cd = my_data.customdata
my_cds = my_data.customdatasrc
my_domain = my_data.domain
my_fig = my_data.figure
my_hi = my_data.hoverinfo
my_hl = my_data.hoverlabel
my_ids = my_data.ids
my_idss = my_data.idssrc
my_l = my_data.legend
my_lgr = my_data.legendgrouptitle
my_lr = my_data.legendrank
my_lw = my_data.legendwidth
my_link = my_data.link
my_meta = my_data.meta
my_metas = my_data.metasrc
my_node = my_data.node
my_o = my_data.orientation
my_parent = my_data.parent
my_plotly_name = my_data.plotly_name
my_sp = my_data.selectedpoints
my_stream = my_data.stream
my_tf = my_data.textfont
my_type = my_data.type
my_uid = my_data.uid
my_uirevision = my_data.uirevision
my_v = my_data.valueformat
my_vs = my_data.valuesuffix
my_visible = my_data.visible

my_nodes = dict(
    pad=15,
    thickness=20,
    line=dict(color="black", width=0.5),
    label=["A1", "A2", "B1", "B2", "C1", "C2"],
    color="blue",
    customdata=["Long name A1", "Long name A2", "Long name B1", "Long name B2",
                "Long name C1", "Long name C2"],
    hovertemplate='Node %{customdata} has total value %{value}<extra></extra>',
)

my_links = dict(
    arrowlen=15,
    source=[0, 1, 0, 2, 3, 3],  # indices correspond to labels, eg A1, A2, A1, B1, ...
    target=[2, 3, 3, 4, 4, 5],
    value=[8, 4, 2, 8, 4, 2],
    customdata=["q", "r", "s", "t", "u", "v"],
    hovertemplate='Link from node %{source.customdata}<br />' +
                  'to node%{target.customdata}<br />has value %{value}' +
                  '<br />and data %{customdata}<extra></extra>',
)
my_data.node = my_nodes
my_data.link = my_links
my_data.arrangement = "snap"

fig_go_layout = go.Figure(data=[my_data])
fig_go_layout.update_layout(
    title_text="Basic Sankey Diagram",
    font_size=10,
    # hovermode='x',  supplanted by `hovertemplate=` in node/link.
)
fig_go_layout.show()  # starts default web browser and display
