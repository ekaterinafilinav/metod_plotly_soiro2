from plotly.subplots import make_subplots

fig = make_subplots(rows=2, cols=2,
                    specs=[[{"type": "xy"}, {"type": "polar"}],
                           [{"type": "domain"}, {"type": "scene"}]])
fig.add_bar(row=1, col=1, y=[2, 3, 1], )
fig.add_pie(row=2, col=1, values=[2, 3, 1])
fig.add_barpolar(row=1, col=2, theta=[0, 45, 90], r=[2, 3, 1])
fig.add_scatter3d(row=2, col=2, x=[2, 3], y=[0, 0], z=[0.5, 1])
fig.update_layout(height=700, showlegend=False)
fig.show()
