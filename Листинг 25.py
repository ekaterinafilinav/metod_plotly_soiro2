import plotly.express as px

df = {'x': [], 'y': [], 'z': []}
for xi in range(-100, 101):
    for yi in range(-100, 101):
        df['x'].append(xi)
        df['y'].append(yi)
        df['z'].append(xi ** 2 + yi ** 2)

fig = px.scatter_3d(df, x="x", y="y", z="z", color="z")
fig.show()
