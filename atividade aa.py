import pandas as pd
df = pd.read_csv("alunos_desempenho.csv")
df.iloc[0]

df = pd.read_csv("alunos_desempenho.csv")
df.head()
df.columns
colunas = ['aluno','curso','periodo']
df[colunas]

pd.read_excel("alunos_localidade_carro_merge.xlsx")
df.head()
df.columns
colunas = [id_]