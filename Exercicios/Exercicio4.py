#Condições Clímaticas

tem_sol = True
tem_chuva = False

if tem_sol and not tem_chuva:
    print("Hoje o dia está muito quente")
else:
    print("Hoje o dia está muito chuvoso")

#Verificando se os números digitados são pares
numero1 = int(input("Digite o primeiro N°: "))
numero2 = int(input("Digite o segundo N°: "))

if numero1 % 2 == 0  and numero2 % 2 == 0:
    print("Ambos os números sao Pares")
else:
    
    print("Pelo menos um dos números não é par")

# Verificando multiplos de 3 e ímpares em uma lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
for numero in numeros:
        if numero % 3 == 0 and numero % 2 != 0:
            print(numero)

#Verificando se a idade do úsuario está no intervalo de 18 a 65 anos
            idade=int(input("Digite sua idade"))

            if idade >= 18 and idade <= 65:
                print("Sua idade está dentro do intervalo Trabalhista")
            else:
                print("Sua idade não está no intervalo Trabalhista")
