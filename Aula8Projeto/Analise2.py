# Este código cria um arquivo chamado analisePrimaria.yaml com os dados do
# total de vendas de cada produto e suas respectivas receitas

import yaml
from collections import defaultdict
from datetime import datetime

# Carregar dados do arquivo YAML
with open('Aula8Projeto/DadosDeVendas.yaml', 'r') as file:
    dados = yaml.safe_load(file)

vendas = dados['vendas']

# Dicionário para armazenar a contagem de vendas e receita total por produto por mês
relatorio_vendas_por_mes = defaultdict(lambda: defaultdict(lambda: {'quantidade': 0, 'receita_total': 0.0}))

# Calcular a contagem de vendas e receita total por produto por mês
for venda in vendas:
    produto = venda['produto']
    data_venda = datetime.strptime(venda['data'], '%Y-%m-%d')
    mes = data_venda.strftime('%Y-%m')
    quantidade = venda['quantidade']
    preco_unitario = venda['preco_unitario']
    receita = quantidade * preco_unitario
    relatorio_vendas_por_mes[produto][mes]['quantidade'] += quantidade
    relatorio_vendas_por_mes[produto][mes]['receita_total'] += receita

# Criar dicionário com os dados de análise primária separados por produto e por mês
analise_primaria = {}
for produto, vendas_por_mes in relatorio_vendas_por_mes.items():
    analise_primaria[produto] = {}
    for mes, dados in vendas_por_mes.items():
        analise_primaria[produto][mes] = {
            'total_vendas': dados['quantidade'],
            'receita_total': dados['receita_total']
        }

# Escrever os resultados em um arquivo YAML
with open('Aula8Projeto/analisePrimaria.yaml', 'w') as file:
    yaml.dump(analise_primaria, file, default_flow_style=False)
