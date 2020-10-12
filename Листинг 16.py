import plotly.express as px

df = {'x': [], 'y': [], 'k': [], 'm': [], 's': []}
for ki in range(-10, 11):
    for mi in range(-100, 101, 50):
        for xi in range(-10, 11, 2):
            df['x'].append(xi)
            df['k'].append(ki)
            df['m'].append(mi)
            df['y'].append(ki * xi + mi)
            df['s'].append(mi ** 2)

fig = px.scatter(df,
                 x='x',
                 y='y',
                 animation_frame='k',
                 symbol='m',
                 size="s",
                 symbol_sequence=['circle-open', 'square-open', 'diamond-open',
                                  'triangle-down-open'],
                 color_discrete_sequence=['black'],
                 trendline='lowess',
                 trendline_color_override='#000000',
                 template='presentation'
                 )

fig.show()
