import plotly.express as px

df = {'Название озера': ['озеро Байкал', 'Онежское озеро', 'Озеро Иссык-Куль',
                         'Ладожское озеро'],
      'Глубина, м': [1620, 127, 668, 225]}

fig = px.pie(df, names='Название озера',
             values='Глубина, м',
             title='Глубина озер России',
             width=800,
             height=400, template='presentation')
fig.show()
