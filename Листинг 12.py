import plotly.express as px

fig = px.line(x=[1, 2, 3, 4], y=[3, 5, 4, 8], template='presentation')
fig.show()
