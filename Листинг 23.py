import plotly.express as px

df = {'Информатика': [3.3, 4.4, 3.5],
      'Физика': [3.2, 4.5, 5],
      'Математика': [3.4, 3.8, 4.2]

      }
fig = px.density_contour(df, x="Информатика", y="Физика", color="Математика",
                         template='presentation')

fig.show()
