import csv

import plotly.express as px

data_list = [[], [], [], []]

with open('задание 14.csv', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=';')
    for row in data:
        for i in range(4):
            data_list[i].append(row[i])

data_dict = {data_list[0][0]: data_list[0][1:],
             data_list[1][0]: data_list[1][1:],
             data_list[2][0]: data_list[2][1:],
             data_list[3][0]: data_list[3][1:]}

fig = px.histogram(data_dict, x='округ', y='балл', color="предмет",
                   template='presentation')
fig.show()
