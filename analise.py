import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Leitura dos dados

df = pd.read_csv('Customer_support_data.csv')
df.info()

#  ------------- TRATAMENTO DOS DADOS
print(df.describe())
print(df.isnull().sum())

# Remocao de colunas desnecessarias para a analise proposta

df_tratado = df.drop(["Customer Remarks", "Order_id", "order_date_time"], axis=1)

# Substituir valores numericos faltantes pela media

df_tratado["Item_price"].fillna(df_tratado["Item_price"].median(), inplace=True)
df_tratado["connected_handling_time"].fillna(df_tratado["connected_handling_time"].median(), inplace=True)

# Substituir valores categoricos faltantes

df_tratado["Customer_City"].fillna("Unknown", inplace=True)
df_tratado["Product_category"].fillna("Unknown", inplace=True)

print(df_tratado.head())
print()
print(df_tratado['Product_category'].unique())


#  ------------- ANALISE EXPLORATORIA
# Plotar histograma do CSAT Score

plt.figure(figsize=(12, 8))
sns.histplot(df_tratado['CSAT Score'], bins=20, kde=True)
plt.title('Distribuição do CSAT Score')
plt.xlabel('CSAT Score')
plt.ylabel('Frequência')
plt.show()

# Plotar relacao entre CSAT e categoria de produtos

plt.figure(figsize=(12, 12))
sns.boxplot(x='Product_category', y='CSAT Score', data=df_tratado)
plt.title('CSAT Score por Categoria de Produto')
plt.xlabel('Categoria de Produto')
plt.ylabel('CSAT Score')
plt.xticks(rotation=45)
plt.show()


# Preparar dados para o pie chart
channel_counts = df_tratado['channel_name'].value_counts()
labels = channel_counts.index  # Nomes dos canais de atendimento
sizes = channel_counts.values   # Contagens de ocorrências de cada canal

colors = ['darkgreen', 'green', 'lightgreen', 'yellow', 'orange']

plt.figure(figsize=(12, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Distribuição dos Canais de Atendimento')
plt.axis('equal')
plt.show()

# CSAT Score % por canal de atendimento

plt.figure(figsize=(12, 8))
sns.boxplot(x='channel_name', y='CSAT Score', data=df_tratado, palette='viridis')
plt.title('Distribuição do CSAT Score por Canal de Atendimento')
plt.xlabel('Canal de Atendimento')
plt.ylabel('CSAT Score')
plt.xticks(rotation=45)
plt.show()

# Produtos mais comuns com CSAT Score igual a 1

df_csat_1 = df[df['CSAT Score'] == 1]
top_product_types = df_csat_1['Product_category'].value_counts().head(10)

plt.figure(figsize=(12, 12))
sns.barplot(x=top_product_types.index, y=top_product_types.values, palette='viridis')
plt.title('Tipos de Produtos Mais Comuns com CSAT Score = 1')
plt.xlabel('Tipo de Produto')
plt.ylabel('Contagem')
plt.xticks(rotation=45)
plt.show()

# Produtos mais comuns com CSAT Score igual a 5

df_csat_5 = df[df['CSAT Score'] == 5]
top_product_types = df_csat_5['Product_category'].value_counts().head(10)

plt.figure(figsize=(12, 12))
sns.barplot(x=top_product_types.index, y=top_product_types.values, palette='viridis')
plt.title('Tipos de Produtos Mais Comuns com CSAT Score = 5')
plt.xlabel('Tipo de Produto')
plt.ylabel('Contagem')
plt.xticks(rotation=45)
plt.show()

# Relacao entre tempo de permanencia e CSAT Score

order = ['On Job Training', '0-30', '31-60', '61-90', '>90']
csat_by_tenure = df.groupby('Tenure Bucket')['CSAT Score'].mean().reindex(order)

plt.figure(figsize=(12, 12))
sns.lineplot(x=csat_by_tenure.index, y=csat_by_tenure.values, marker='o', color='b')
plt.title('CSAT Score Médio por Tempo de Serviço', fontsize=14)
plt.xlabel('Intervalo de Tempo', fontsize=12)
plt.ylabel('CSAT Score Médio', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

tenure_counts = df['Tenure Bucket'].value_counts().reindex(order)

plt.figure(figsize=(12, 12))
sns.barplot(x=tenure_counts.index, y=tenure_counts.values, order=order, palette='viridis')
plt.title('Quantidade de Atendimentos por Tempo de Serviço')
plt.xlabel('Intervalo de Tempo')
plt.ylabel('Número de Atendimentos')
plt.xticks(rotation=45)
plt.show()