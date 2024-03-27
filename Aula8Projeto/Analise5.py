import yaml

# Carregar o arquivo YAML
with open('Aula8Projeto/DadosDeVendas.yaml', 'r') as file:
    dados = yaml.safe_load(file)

# Criar um dicionário para armazenar os dados de consumo de cada cliente
consumo_clientes = {}

# Iterar sobre as vendas e atualizar o dicionário de consumo de clientes
for venda in dados['vendas']:
    cliente_id = venda['cliente_id']
    produto = venda['produto']
    quantidade = venda['quantidade']
    preco_unitario = venda['preco_unitario']
    data = venda['data']

    # Se o cliente ainda não estiver no dicionário, inicialize seu registro
    if cliente_id not in consumo_clientes:
        consumo_clientes[cliente_id] = {
            'nome': '',
            'idade': None,
            'sexo': '',
            'cidade': '',
            'valor_gasto_total': 0.0,
            'consumo_por_produto': {}
        }

    # Atualizar o nome, idade, sexo e cidade do cliente se ainda não estiverem definidos
    if not consumo_clientes[cliente_id]['nome']:
        for cliente in dados['comportamento_do_cliente']:
            if cliente['id'] == cliente_id:
                consumo_clientes[cliente_id]['nome'] = cliente.get('nome', '')
                consumo_clientes[cliente_id]['idade'] = cliente.get('idade')
                consumo_clientes[cliente_id]['sexo'] = cliente.get('sexo', '')
                consumo_clientes[cliente_id]['cidade'] = cliente.get('cidade', '')
                break

    # Atualizar o valor gasto total pelo cliente
    valor_gasto = quantidade * preco_unitario
    consumo_clientes[cliente_id]['valor_gasto_total'] += valor_gasto

    # Atualizar o consumo do produto pelo cliente
    if produto not in consumo_clientes[cliente_id]['consumo_por_produto']:
        consumo_clientes[cliente_id]['consumo_por_produto'][produto] = {}
    mes = data.split('-')[1]
    if mes not in consumo_clientes[cliente_id]['consumo_por_produto'][produto]:
        consumo_clientes[cliente_id]['consumo_por_produto'][produto][mes] = 0
    consumo_clientes[cliente_id]['consumo_por_produto'][produto][mes] += quantidade

# Escrever os dados de consumo de clientes em um novo arquivo YAML
with open('Aula8Projeto/ConsumoPorCliente.yaml', 'w') as file:
    yaml.dump(consumo_clientes, file, default_flow_style=False)
