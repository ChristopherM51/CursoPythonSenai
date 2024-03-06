#Operações com Variaveis
#Ao colocar um número que contém virgula automaticamente ele se torna string

salario = 50
bonus = 500
salario_total = salario + bonus
print(salario_total)

#Manipulação de string

nome = "Maria"
Sobrenome = "Silva"
nome_completo =  nome + " " + Sobrenome
print(nome_completo)

#Atualização de variaveis 

contador = 0
contador += 1
print(contador)

#variaveis estruturas de controle
idade = 18
if idade >=18:
    pode_votar = True
else:
    pode_votar = False

#Tipagem
numero = 42
texto = "Python"
print(f"{numero}"+texto)
 #resultado = numero+texto
 #print(resultado)

#Variaveis Booleanas
tem_cafe = True
tem_cha = False
    
#Expressões booleanas
tem_bebida_quente = tem_cafe or tem_cha
tem_as_dois = tem_cafe and tem_cha

    