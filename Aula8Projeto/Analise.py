# Este programa lê os dados do arquivo DadosDeVendas.yaml e exibe as primeiras 
# linhas para entender a estrutura dos dados . Em seguida, calcula estatísticas 
# descritivas básicas para as colunas numéricas usando o método describe() do 
# Pandas DataFrame

import pandas as pd
import yaml

# Ler o arquivo YAML
with open("Aula8Projeto/DadosDeVendas.yaml", "r") as file:
    dados_yaml = yaml.safe_load(file)

# Criar DataFrame Pandas a partir dos dados YAML
df = pd.DataFrame(dados_yaml["vendas"])

# Visualizar as primeiras linhas do DataFrame
print("Primeiras linhas do DataFrame:")
print(df.head())

# Calcular estatísticas descritivas básicas para as colunas numéricas
print("\nEstatísticas descritivas básicas para as colunas numéricas:")
print(df.describe())
