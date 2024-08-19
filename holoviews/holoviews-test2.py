import holoviews as hv

hv.extension('bokeh')

nodes = ["PhD", "Career Outside Science", "Early Career Researcher", "Research Staff",
         "Permanent Research Staff", "Professor", "Non-Academic Research"]

nodes = hv.Dataset(enumerate(nodes), 'index', 'label')

edges = [
    (0, 1, 53),
    (0, 2, 47),
    (2, 6, 17),
    (2, 3, 30),
    (3, 1, 22.5),
    (3, 4, 3.5),
    (3, 6, 4.),
    (4, 5, 0.45),
    (4, 0, 2)
]

my_data = (edges, nodes)
my_kdims = ['From', 'To']
value_dim = hv.Dimension('Percentage', unit='%')

h2 = hv.Sankey(data=my_data, kdims=my_kdims, vdims=value_dim)
h2.options(
    label_index='label',
    label_position='left',
    width=900,
    height=600,
    edge_color_index='To'
)

renderer = hv.renderer('bokeh')

renderer.save(h2, 'h2')
