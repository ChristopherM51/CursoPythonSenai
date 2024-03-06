import numpy as np

#Criação de Arrays:
#Para criar uma matriz NumPy vazia, podemos usar a função numpy.empty(shape).
#Por exemplo:
empty_array = np.empty((3, 3))
print(empty_array)


#Para criar uma matriz preenchida com valores iguais a 1, podemos usar a função numpy.ones(shape).
#Por exemplo:
ones_array = np.ones((2, 2))
print(ones_array)


#Para criar uma matriz preenchida com todos os zeros, podemos usar a função numpy.zeros(shape).
#Por exemplo:


zeros_array = np.zeros((4, 4))
print(zeros_array)


#Para criar uma matriz com valores aleatórios entre 0 e 1, podemos usar a função numpy.random.rand(shape).
#Por exemplo:
random_array = np.random.rand(3, 3)
print(random_array)

#Indexação e Seleção:
#Para selecionar elementos específicos de uma matriz NumPy, usamos a indexação por posição.
#Por exemplo:
my_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(my_array)
print(my_array[1, 2])  # Seleciona o elemento na segunda linha e terceira coluna (6)


#Para encontrar o valor máximo e mínimo em uma matriz, usamos numpy.max() e numpy.min().
#Por exemplo:
max_value = np.max(my_array) #Valor maximo do array
min_value = np.min(my_array) #Valor minimo do array
print(f"Valor máximo: {max_value}, Valor mínimo: {min_value}")

#Para calcular a soma dos valores em uma matriz, usamos numpy.sum().
#Por exemplo:
total_sum = np.sum(my_array)
print(f"Soma total: {total_sum}")


#Manipulação de Arrays:
#Para remover entradas unidimensionais de uma matriz, usamos numpy.squeeze().
#Por exemplo:
squeezed_array = np.squeeze(my_array)
print(squeezed_array)


#Adição de Matrizes: usamos o operador +. 
#Aqui está um exemplo:
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
resultado = matriz1 + matriz2
print("Resultado da adição de matrizes:")
print(resultado)


#Subtração de Matrizes: usamos o operador -.
#Aqui está um exemplo:
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
resultado = matriz1 - matriz2
print("Resultado da subtração de matrizes:")
print(resultado)

#Multiplicação de Matrizes:
#Para multiplicar matrizes em Python, podemos usar a função numpy.dot() ou o operador @. 
#Aqui está um exemplo:
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
resultado = np.dot(matriz1, matriz2)
# Ou, alternativamente: resultado = matriz1 @ matriz2
print("Resultado da multiplicação de matrizes:")
print(resultado)


#Operações Estatísticas:
#Para calcular a média, mediana e desvio padrão de uma matriz plana,
#usamos numpy.mean(), numpy.median() e numpy.std().
#Para calcular a soma dos elementos diagonais de uma matriz NumPy, usamos numpy.trace(). Por exemplo:
diagonal_sum = np.trace(my_array)
print(f"Soma diagonal: {diagonal_sum}")


#Número de Linhas e Colunas de uma Matriz:
#Para encontrar o número de linhas e colunas de uma matriz, usamos a função numpy.shape.
#Ela retorna uma tupla de inteiros representando o tamanho de cada dimensão da matriz.
#Aqui está um exemplo:
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
num_linhas, num_colunas = np.shape(matriz)
print(f"Número de linhas: {num_linhas}")
print(f"Número de colunas: {num_colunas}")


#Verificar se um Array NumPy Contém uma Linha Específica:
#Para verificar se um array NumPy contém uma linha específica, podemos usar a função numpy.isin().
#Aqui está um exemplo:
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
linha_especifica = np.array([4, 5, 6])
contem_linha = np.isin(matriz, linha_especifica).all(axis=1).any()
print(f"Contém a linha específica? {contem_linha}")


#Trocar Dois Eixos de uma Matriz:
#Para trocar dois eixos de uma matriz, podemos usar numpy.transpose() ou simplesmente .T.
#Aqui está um exemplo:
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matriz_transposta = np.transpose(matriz)
# Ou, alternativamente: matriz_transposta = matriz.T
print("Matriz original:")
print(matriz)
print("Matriz transposta:")
print(matriz_transposta)
