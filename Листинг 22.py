import plotly.express as px

df = {'Информатика': [3, 3.3, 4.4, 3.5, 5],
      'Физика': [3, 3.2, 4.5, 5, 5],
      'Математика': [3, 3.4, 3.8, 4.2, 5]
      }
fig = px.parallel_coordinates(df, color='Математика',
                              color_continuous_midpoint=2,
                              template='presentation')
fig.show()
