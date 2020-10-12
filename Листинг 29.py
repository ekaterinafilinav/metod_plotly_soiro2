import json

import pandas as pd
import plotly
import plotly.express as px

file = 'задание 14.xls'

xl = pd.read_excel(file)
fig4 = px.violin(xl, x='предмет', y='балл', color="округ",
                 template='presentation', points='outliers', box=True)

fig4.show()
fig4.write_html('file.html')
print(plotly.io.to_json(fig4))

with open('file.json', 'w', encoding='utf-8') as f:
    json.dump(fig4, f, cls=plotly.utils.PlotlyJSONEncoder, ensure_ascii=False, indent=4)


