import plotly.express as px

fig = px.pie(names=['Утренний завтрак', 'Второй завтрак', 'Обед', 'Ужин'],
             values=[25, 15, 45, 15],
             title='Распределение дневной нормы питания',
             width=800,
             height=400,
             template='presentation')

fig.show()
