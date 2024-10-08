import plotly.graph_objects as go

fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=["A1", "A2", "B1", "B2", "C1", "C2"],
        color="green"
    ),
    link=dict(
        source=[0, 1, 0, 2, 3, 3],  # indices correspond to labels, eg A1, A2, A1, B1, ...
        target=[2, 3, 3, 4, 4, 5],
        value=[7, 5, 3, 9, 5, 3]
    ))])

fig.update_layout(title_text="Simple Sankey Diagram using plotly in Python.", font_size=10)
#fig_go_layout.update_layout(hovermode="x")
fig.show()
