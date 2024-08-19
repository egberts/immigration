# Get this figure: fig_go_layout = py.get_figure("https://plotly.com/~PlotBot/880/")
# Get this figure's data: data = py.get_figure("https://plotly.com/~PlotBot/880/").get_data()
# Add data to this figure: py.plot(Data([Scatter(x=[1, 2], y=[2, 3])]), filename ="marker-h-bar", fileopt="extend")
# Get y data of first trace: y1 = py.get_figure("https://plotly.com/~PlotBot/880/").get_data()[0]["y"]

# Get figure documentation: https://plotly.com/python/get-requests/
# Add data documentation: https://plotly.com/python/file-options/

# If you're using unicode in your file, you may need to specify the encoding.
# You can reproduce this figure in Python with the following code!

# Learn about API authentication here: https://plotly.com/python/getting-started
# Find your api_key here: https://plotly.com/settings/api

import chart_studio.plotly as py
from plotly.graph_objs import *
#py.sign_in('username', 'api_key')
trace1 = {
  "name": "SF Zoo",
  "type": "bar",
  "x": [20, 14, 23],
  "y": ["giraffes", "orangutans", "monkeys"],
  "marker": {
    "line": {
      "color": "rgba(55, 128, 191, 1.0)",
      "width": 1
    },
    "color": "rgba(55, 128, 191, 0.6)"
  },
  "orientation": "h"
}
trace2 = {
  "name": "LA Zoo",
  "type": "bar",
  "x": [12, 18, 29],
  "y": ["giraffes", "orangutans", "monkeys"],
  "marker": {
    "line": {
      "color": "rgba(255, 153, 51, 1.0)",
      "width": 1
    },
    "color": "rgba(255, 153, 51, 0.6)"
  },
  "orientation": "h"
}

data = Data([trace1, trace2])
layout = {"barmode": "stack"}
fig = Figure(data=data, layout=layout)
fig.show()
#plot_url = py.plot(fig_go_layout)
#print("plot_url: ", plot_url)
