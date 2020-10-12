import plotly.express as px

x = range(-10, 10, 2)
y = []
for i in x:
    y.append(-1.5 * i + 3)
fig = px.line(x=x, y=y,
              line_dash_sequence=['longdash'],
              template='presentation')
fig.show()
