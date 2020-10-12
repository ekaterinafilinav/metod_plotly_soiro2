import plotly.express as px

fig = px.bar(
    x=['озеро Байкал', 'Онежское озеро', 'Озеро Иссык-Куль', 'Ладожское озеро'],
    y=[1620, 127, 668, 225],
    title='Глубина озер России',
    width=800,
    height=400)
fig.show()
