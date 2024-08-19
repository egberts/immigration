

import numpy as np
import holoviews as hv
hv.extension('bokeh')

h1=hv.Sankey([
    ['A', 'X', 5],
    ['A', 'Y', 7],
    ['A', 'Z', 6],
    ['B', 'X', 2],
    ['B', 'Y', 9],
    ['B', 'Z', 4]]
).options(width=600, height=400)

h1

renderer = hv.renderer('bokeh')

renderer.save(h1, 'h1')
