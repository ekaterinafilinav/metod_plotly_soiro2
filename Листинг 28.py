import csv

import plotly.express as px

results = []
with open('задание 14.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';', quotechar=',')
    for row in reader:
        results.append(row)
print(results[0])

fig4 = px.box(results, x='предмет', y='балл', color="округ",
              template='presentation')
fig4.show()
