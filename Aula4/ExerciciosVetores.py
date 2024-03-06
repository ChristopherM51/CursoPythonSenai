#Exercicio 1
# Função para ler um vetor de 5 números inteiros
def ler_vetor():
    vetor = []
    for i in range(5):
        numero = int(input(f"Digite o {i+1}º número inteiro: "))
        vetor.append(numero)
    return vetor

# Função para imprimir os elementos do vetor
def imprimir_vetor(vetor):
    print("Os números digitados são:")
    for num in vetor:
        print(num)

# Programa principal
if __name__ == "__main__":
    vetor = ler_vetor()
    imprimir_vetor(vetor)
    
#Exercico 2
# Função para ler um vetor de 10 números reais
def ler_vetor():
    vetor = []
    for i in range(10):
        num = float(input(f"Digite o {i+1}º número real: "))
        vetor.append(num)
    return vetor

# Função para imprimir os elementos do vetor na ordem inversa
def imprimir_vetor_inverso(vetor):
    print("Os números digitados em ordem inversa são:")
    for num in reversed(vetor):
        print(num)

# Programa principal
if __name__ == "__main__":
    vetor = ler_vetor()
    imprimir_vetor_inverso(vetor)

#Exercico 3
# Função para ler as 4 notas
def ler_notas():
    notas = []
    for i in range(4):
        nota = float(input(f"Digite a {i+1}ª nota: "))
        notas.append(nota)
    return notas

# Função para calcular a média das notas
def calcular_media(notas):
    return sum(notas) / len(notas)

# Função para mostrar as notas e a média na tela
def mostrar_resultados(notas, media):
    print("Notas digitadas:")
    for i, nota in enumerate(notas, start=1):
        print(f"Nota {i}: {nota}")
    print(f"Média das notas: {media}")

# Programa principal
if __name__ == "__main__":
    notas = ler_notas()
    media = calcular_media(notas)
    mostrar_resultados(notas, media)

#Exercicio 4
# Função para ler um vetor de 10 caracteres e contar consoantes
def ler_vetor_e_contar_consoantes():
    vetor = []
    consoantes = 0
    for _ in range(10):
        caractere = input("Digite um caractere: ")
        vetor.append(caractere)
        # Verifica se o caractere é uma consoante (não é vogal nem é um número ou símbolo)
        if caractere.isalpha() and caractere.lower() not in 'aeiou':
            consoantes += 1
    return vetor, consoantes

# Programa principal
if __name__ == "__main__":
    vetor, num_consoantes = ler_vetor_e_contar_consoantes()
    print(f"Número de consoantes: {num_consoantes}")
    print("Consoantes lidas:")
    for caractere in vetor:
        if caractere.isalpha() and caractere.lower() not in 'aeiou':
            print(caractere)

