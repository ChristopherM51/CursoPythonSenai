# Identifica os produtos mais vendidos com base na quantidade total de vendas, 
# calcula a receita total gerada por cada produto e, em seguida, plota um gráfico de
# barras mostrando os produtos mais vendidos e um gráfico de pizza mostrando a
# distribuição da receita entre os produtos.

import yaml
import matplotlib.pyplot as plt

# Carregar dados do arquivo YAML
with open('Aula8Projeto/analisePrimaria.yaml', 'r') as file:
    dados = yaml.safe_load(file)

# Identificar os produtos mais vendidos
produtos_mais_vendidos = sorted(dados.items(), key=lambda x: sum(valores['total_vendas'] for valores in x[1].values()), reverse=True)
top_produtos = [produto for produto, _ in produtos_mais_vendidos[:5]]
quantidades_vendidas = [sum(valores['total_vendas'] for valores in dados[produto].values()) for produto in top_produtos]

# Plotar um gráfico de barras mostrando os produtos mais vendidos
plt.figure(figsize=(10, 6))
plt.bar(top_produtos, quantidades_vendidas, color='skyblue')
plt.title('Produtos Mais Vendidos')
plt.xlabel('Produto')
plt.ylabel('Quantidade Vendida')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('produtos_mais_vendidos.png')
plt.show()

# Calcular a receita total gerada por cada produto
receita_por_produto = {produto: sum(valores['receita_total'] for valores in dados[produto].values()) for produto in dados}

# Plotar um gráfico de pizza mostrando a distribuição da receita entre os produtos
plt.figure(figsize=(8, 8))
plt.pie(receita_por_produto.values(), labels=receita_por_produto.keys(), autopct='%1.1f%%', startangle=140)
plt.title('Distribuição da Receita por Produto')
plt.axis('equal')
plt.tight_layout()
plt.savefig('distribuicao_receita_por_produto.png')
plt.show()
