import yaml
import matplotlib.pyplot as plt

def carregar_dados(arquivo):
    with open(arquivo, 'r') as file:
        dados = yaml.safe_load(file)
    return dados

def extrair_gastos_e_compras(dados):
    gastos_por_cliente = {}
    compras_por_cliente = {}
    
    for venda in dados['vendas']:
        cliente_id = venda['cliente_id']
        preco_total = venda['quantidade'] * venda['preco_unitario']
        
        # Atualiza gastos por cliente
        if cliente_id in gastos_por_cliente:
            gastos_por_cliente[cliente_id] += preco_total
        else:
            gastos_por_cliente[cliente_id] = preco_total
        
        # Atualiza compras por cliente
        if cliente_id in compras_por_cliente:
            compras_por_cliente[cliente_id] += 1
        else:
            compras_por_cliente[cliente_id] = 1
    
    return gastos_por_cliente, compras_por_cliente

def identificar_clientes_mais_fieis(gastos_por_cliente):
    clientes_mais_fieis = sorted(gastos_por_cliente.items(), key=lambda x: x[1], reverse=True)
    return clientes_mais_fieis

def plotar_grafico(gastos_por_cliente, compras_por_cliente):
    valores_gastos = list(gastos_por_cliente.values())
    frequencia_compras = list(compras_por_cliente.values())
    
    plt.figure(figsize=(10, 6))
    plt.scatter(valores_gastos, frequencia_compras, alpha=0.5)
    plt.title('Valor Total Gasto vs Frequência de Compras')
    plt.xlabel('Valor Total Gasto')
    plt.ylabel('Frequência de Compras')
    plt.grid(True)
    plt.show()

def main():
    arquivo = 'Aula8Projeto/DadosDeVendas.yaml'
    dados = carregar_dados(arquivo)
    gastos_por_cliente, compras_por_cliente = extrair_gastos_e_compras(dados)
    clientes_mais_fieis = identificar_clientes_mais_fieis(gastos_por_cliente)
    plotar_grafico(gastos_por_cliente, compras_por_cliente)
    
    print("Clientes mais fiéis (por ordem de valor total gasto):")
    for cliente_id, valor_gasto in clientes_mais_fieis:
        print(f"Cliente ID: {cliente_id}, Valor Total Gasto: R$ {valor_gasto:.2f}")

if __name__ == "__main__":
    main()
