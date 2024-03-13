import numpy as np
import matplotlib.pyplot as plt

#Desafio

# Dados fictícios de preços médios diários para duas ações (em dólares)
preco_medio_acao1 = np.array([50, 52, 48, 55, 53, 51, 49, 50, 54, 52])
preco_medio_acao2 = np.array([120, 122, 118, 125, 123, 121, 119, 120, 124, 122])
# Número de ações que o investidor possui de cada empresa
acoes_acao1 = 100  # Exemplo: o investidor possui 100 ações da Ação 1
acoes_acao2 = 50   # Exemplo: o investidor possui 50 ações da Ação 2

# Calculando o valor do investimento em cada dia
valor_investimento_acao1 = preco_medio_acao1 * acoes_acao1
valor_investimento_acao2 = preco_medio_acao2 * acoes_acao2

# Calculando o patrimônio total do investidor em cada dia
patrimonio_total = valor_investimento_acao1 + valor_investimento_acao2

# Exibindo os resultados diariamente
for dia in range(len(preco_medio_acao1)):
    print(f"Patrimônio total no dia {dia + 1}: ${patrimonio_total[dia]:.2f}")

# Plotando o gráfico da evolução patrimonial do investidor
dias = np.arange(1, len(preco_medio_acao1) + 1)
plt.plot(dias, patrimonio_total, marker='o')
plt.title("Evolução Patrimonial do Investidor")
plt.xlabel("Dia")
plt.ylabel("Patrimônio Total ($)")
plt.grid(True)
plt.show()
