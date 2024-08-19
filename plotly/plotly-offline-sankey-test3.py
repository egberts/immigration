import plotly.offline

data_trace = {'domain': {'x': [0, 1], 'y': [0, 1]},
              'height': 772,
              'link': {'label': ['EM', 'GWF9C51E', 'GWF9C511', 'GWF9C51E Sensor Set',
                                 'GWF9C511 Sensor Set'],
                       'source': [0, 1, 3, 1, 4, 2, 0, 2],
                       'target': [1, 3, 1, 0, 2, 0, 2, 4],
                       'value': [40, 76, 29, 86, 30, 75, 41, 65]},
              'node': {'color': ['blue', 'yellow', 'yellow', 'green', 'green'],
                       'label': ['EM', 'GWF9C51E', 'GWF9C511', 'GWF9C51E Sensor Set',
                                 'GWF9C511 Sensor Set'],
                       'line': {'color': 'black', 'width': 0.5},
                       'pad': 15,
                       'thickness': 15},
              'orientation': 'h',
              'type': 'sankey',
              'valueformat': '.3s',
              'valuesuffix': 'pkts',
              'width': 1118}
layout = dict(
    title="Testing Sankey",
    font=dict(
        size=10
    )
)

fig = dict(data=[data_trace], layout=layout)
plotly.offline.plot(fig, validate=False)
