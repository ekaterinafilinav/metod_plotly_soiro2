import plotly.express as px

fig = px.line_geo(lat=[51.555051, 55.753215, 28.613506],
                       lon=[46.013428,37.622504, 77.207917],
                       projection="orthographic")
