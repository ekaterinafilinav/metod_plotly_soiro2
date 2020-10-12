import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html

fig = px.line(y=[1, 2, 3])
app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)
