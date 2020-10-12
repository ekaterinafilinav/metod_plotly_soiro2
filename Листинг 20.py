import plotly.express as px

fig = px.scatter_geo(lat=[51.555051, 55.753215],
                     lon=[46.013428, 37.622504],
                     size=[800000, 12000000])
