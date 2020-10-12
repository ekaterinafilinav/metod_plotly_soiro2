import plotly.express as px

f = open("задание 14.txt", 'r', encoding="utf-8")
key_f = f.readline(-1).rstrip().split('\t')
df = {key_f[0]: [], key_f[1]: [], key_f[2]: [], key_f[3]: []}

for line in f:
    line_list = line.rstrip().split('\t')
    df['округ'].append(line_list[0])
    df['фамилия'].append(line_list[1])
    df['предмет'].append(line_list[2])
    df['балл'].append(int(line_list[3]))
# print(df)
f.close()

fig = px.strip(df, x='округ', y='балл', color="предмет",
               template='presentation')
fig.show()
