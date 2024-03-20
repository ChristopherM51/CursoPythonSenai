import yaml
import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados do arquivo YAML
with open('Aula8Projeto/DadosDeVendas.yaml', 'r') as file:
    dados = yaml.safe_load(file)

# Converter os dados em DataFrames
df_vendas = pd.DataFrame(dados['vendas'])

# Transformar a coluna 'data' em datetime
df_vendas['data'] = pd.to_datetime(df_vendas['data'])

# Extrair o mês das datas de venda
df_vendas['mes'] = df_vendas['data'].dt.month

# Contar o número de vendas por mês
vendas_por_mes = df_vendas.groupby('mes').size()

# Reindexar para garantir que todos os meses estejam presentes
vendas_por_mes = vendas_por_mes.reindex(range(1, 13), fill_value=0)

# Plotar o gráfico de barras
plt.bar(vendas_por_mes.index, vendas_por_mes.values)
plt.xlabel('Mês')
plt.ylabel('Número de Vendas')
plt.title('Contagem de Vendas por Mês')
plt.show()
