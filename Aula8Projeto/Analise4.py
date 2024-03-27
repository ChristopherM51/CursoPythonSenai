import yaml
import matplotlib.pyplot as plt

# Carregar dados do arquivo YAML
with open('Aula8Projeto/analisePrimaria.yaml', 'r') as file:
    dados = yaml.safe_load(file)

# Verificar os dados carregados
print(dados)

# Plotar um gráfico para cada produto
for produto, dados_por_mes in dados.items():
    if isinstance(dados_por_mes, list):
        # Caso os dados estejam em uma lista, podemos precisar de uma manipulação diferente
        # dependendo da estrutura real dos dados
        print(f"Dados para '{produto}' não estão no formato esperado. Verifique a estrutura do arquivo YAML.")
    else:
        meses = []
        receitas = []

        for mes, valores in dados_por_mes.items():
            meses.append(mes)
            receitas.append(valores['receita_total'])

        plt.figure(figsize=(10, 6))
        plt.plot(meses, receitas, marker='o')
        plt.title(f"Receita Total por Mês para o Produto '{produto}'")
        plt.xlabel('Mês')
        plt.ylabel('Receita Total (R$)')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(f'{produto}_receita_total_por_mes.png')
        plt.show()
