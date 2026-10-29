
import pandas as pd

# Ler o arquivo Excel
df = pd.read_excel("VALE3_evolucao.xlsx")

# Funções estatísticas da coluna "valor"
print("Valor máximo:", df["valor"].max())
print("Valor mínimo:", df["valor"].min())
print("Média:", df["valor"].mean())
print("Desvio padrão:", df["valor"].std())

# Selecionar a primeira linha
print(df.iloc[0:1])

# Selecionar a linha de índice 23 e algumas colunas
colunas = ["conta", "valor"]
print(df.loc[df.index[23:24], colunas])

# Filtrar linhas em que o trimestre seja "20262T"
filtro = df["trimestre"] == "20262T"
print(df[filtro])

# Selecionar apenas as colunas "conta" e "valor"
linhas = ["conta", "valor"]
print(df[linhas])

#linha
linhas = df["conta"] == "lucro"
colunas = ["valor"]
df[linhas][colunas].mean()

import seaborn as sns
dados = df[linhas][colunas]
sns.lineplot(data=dados)

#graficos
import seaborn as sns
import matplotlib.pyplot as plt
# Gráfico do lucro
linhas = df["conta"] == "lucro"
colunas = ["trimestre","valor"]
dados = df[linhas][colunas]
sns.lineplot(dados,x='trimestre',y='valor')
plt.title("Gráfico do lucro")
plt.xticks(rotation=45)

import seaborn as sns
import matplotlib.pyplot as plt

# Filtra os dados de lucro
linhas = df["conta"] == "lucro"
colunas = ["trimestre", "valor"]
dados = df.loc[linhas, colunas]

# Tema
sns.set_theme(style="darkgrid")

# Cria figura
plt.figure(figsize=(12, 6))

# Linha principal
sns.lineplot(
    data=dados,
    x="trimestre",
    y="valor",
    color="#00B894",      # Verde
    linewidth=3,
    marker="o",
    markersize=8
)

# Área sombreada abaixo da linha
plt.fill_between(
    dados["trimestre"],
    dados["valor"],
    color="#74B9FF",      # Azul claro
    alpha=0.25
)

# Personalização
plt.title(
    "Evolução do Lucro por Trimestre",
    fontsize=18,
    fontweight="bold",
    color="#0984E3"
)

plt.xlabel("Trimestre", fontsize=12)
plt.ylabel("Lucro (R$)", fontsize=12)

plt.xticks(rotation=45)
plt.grid(True, linestyle="--", alpha=0.5)

# Remove bordas superiores e direitas
sns.despine()

plt.tight_layout()
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

# Dados
dados = df.loc[df["conta"] == "lucro", ["trimestre", "valor"]]

# Estilo escuro
plt.style.use("dark_background")

# Figura
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_facecolor("black")

# Linha verde com marcadores azuis
sns.lineplot(
    data=dados,
    x="trimestre",
    y="valor",
    color="#00FF88",      # Verde neon
    linewidth=3,
    marker="o",
    markersize=8,
    markerfacecolor="#00BFFF",  # Azul
    markeredgecolor="white",
    ax=ax
)

# Título e eixos
ax.set_title(
    "Lucro por Trimestre",
    fontsize=18,
    color="#00FF88",
    weight="bold"
)

ax.set_xlabel("Trimestre", color="white")
ax.set_ylabel("Lucro (R$)", color="white")

# Grade branca como na imagem
ax.grid(
    True,
    color="white",
    linestyle="-",
    linewidth=1,
    alpha=0.8
)

# Bordas


