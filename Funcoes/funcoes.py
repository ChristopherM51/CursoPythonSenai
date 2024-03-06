# Função Simples:
def saudacao(nome):
    return f"Olá, {nome}!"

# Função com Parâmetros Padrão:
def potencia(base, expoente=2):
    return base ** expoente

# Função com Retorno Múltiplo:
def opera_numeros(a, b):
    soma = a + b
    diferenca = a - b
    return soma, diferenca

# Exemplos de escopo
def exemplo_escopo():
    variavel_local = 10
    print(variavel_local)

exemplo_escopo()  # Saída: 10
# print(variavel_local)  # Erro: variavel_local não está definida fora da função

# Chamada de Funções:
def calcular_quadrado(numero):
    return numero ** (1/2)

resultado = calcular_quadrado(25)
print(resultado)  # Saída: 25

# Recursividade:
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

resultado = fatorial(5)
print(resultado)  # Saída: 120

import operacoes

dados = [2, 3, 5, 7, 11, 13, 17]
media = operacoes.calcular_media(dados)
mediana = operacoes.calcular_mediana(dados)

print (media)
print (mediana)
