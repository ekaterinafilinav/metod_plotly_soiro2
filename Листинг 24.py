import plotly.express as px

df = {'Информатика': [3.3, 4.4, 3.5, 5, 2],
      'Физика': [3.2, 4.5, 5, 5, 5],
      'Математика': [3.4, 3.8, 4.2, 2, 5]

      }

fig = px.scatter_ternary(df, a="Информатика", b="Физика", c="Математика", color="Математика", size="Математика",
                         hover_name="Математика",
                         size_max=20,

                         template='presentation')

fig.show()
