from random import randint

import plotly.express as px

fig = px.scatter(x=[randint(0, 1000) for i in range(1000)],
                 y=[randint(0, 500) for i in range(1000)],
                 size=[randint(1, 5) for i in range(1000)],
                 color_discrete_sequence=['black'],
                 template='presentation'
                 )
fig.show()
