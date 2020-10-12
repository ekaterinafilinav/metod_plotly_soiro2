import plotly.express as px

fig = px.scatter(
    x=[1, 2, 3, 4],
    y=[10, 11, 12, 13],
    size=[10, 100, 500, 1000],
    color=[0, 1, 2, 3],
    marginal_x="histogram", trendline="ols", error_x=[1.2, 1, 1.5, 1.3],
    error_y=[0.4, 0.5, 0.3, 0.6], template='presentation')

fig.show()
