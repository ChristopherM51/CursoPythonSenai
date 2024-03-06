import numpy as np

# Criação de Arrays:

# Matriz NumPy vazia
empty_matrix = np.empty((3, 3))
print("Matriz NumPy vazia:")
print(empty_matrix)

# Matriz NumPy preenchida com valores iguais a 1
ones_matrix = np.ones((3, 3))
print("\nMatriz NumPy preenchida com valores iguais a 1:")
print(ones_matrix)

# Matriz NumPy preenchida com todos os zeros
zeros_matrix = np.zeros((3, 3))
print("\nMatriz NumPy preenchida com todos os zeros:")
print(zeros_matrix)

# Matriz NumPy preenchida com valores aleatórios entre 0 e 1
random_matrix = np.random.random((3, 3))
print("\nMatriz NumPy preenchida com valores aleatórios entre 0 e 1:")
print(random_matrix)

# Array unidimensional com os números de 1 a 5
array_1_to_5 = np.array([1, 2, 3, 4, 5])
print("\nArray unidimensional com os números de 1 a 5:")
print(array_1_to_5)

# Array bidimensional (matriz) 2x3 com números inteiros
array_2x3 = np.array([[1, 2, 3], [4, 5, 6]])
print("\nArray bidimensional (matriz) 2x3 com números inteiros:")
print(array_2x3)


# Indexação e Seleção:

# Selecionar elementos específicos de uma matriz NumPy
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
selected_elements = matrix[[1, 1],[0, 2],]  # Seleciona os elementos (0, 0) e (1, 2)
print("\nElementos específicos selecionados:")
print(selected_elements)

# Encontrar o valor máximo e mínimo em uma matriz
max_value = np.max(matrix)
min_value = np.min(matrix)
print("\nValor máximo na matriz:", max_value)
print("Valor mínimo na matriz:", min_value)

# Calcular a soma dos valores em uma matriz
sum_matrix = np.sum(matrix)
print("\nSoma dos valores na matriz:", sum_matrix)


# Manipulação de Arrays:

# Remover entradas unidimensionais de uma matriz
flat_array = np.ravel(matrix)
print("\nArray unidimensional resultante:")
print(flat_array)

# Adicionar ou subtrair matrizes em Python
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
add_result = matrix1 + matrix2
subtract_result = matrix1 - matrix2
print("\nResultado da adição de matrizes:")
print(add_result)
print("Resultado da subtração de matrizes:")
print(subtract_result)

# Multiplicar matrizes usando NumPy
multiply_result = np.dot(matrix1, matrix2)
print("\nResultado da multiplicação de matrizes:")
print(multiply_result)


# Operações Estatísticas:

# Calcular a média, mediana e desvio padrão de uma matriz plana
flat_matrix = matrix.flatten()
mean_value = np.mean(flat_matrix)
median_value = np.median(flat_matrix)
std_value = np.std(flat_matrix)
print("\nMédia da matriz plana:", mean_value)
print("Mediana da matriz plana:", median_value)
print("Desvio padrão da matriz plana:", std_value)

# Calcular a soma dos elementos diagonais de uma matriz NumPy
diagonal_sum = np.trace(matrix)
print("\nSoma dos elementos diagonais da matriz:", diagonal_sum)

# Desafios Avançados:
# Encontrar o número de linhas e colunas de uma matriz usando NumPy
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
num_rows, num_columns = matrix.shape
print("\nNúmero de linhas na matriz:", num_rows)
print("Número de colunas na matriz:", num_columns)

# Verificar se um array NumPy contém uma linha específica
specific_row = np.array([4, 5, 6])
contains_row = np.any(np.all(matrix == specific_row, axis=1))
print("\nA matriz contém a linha específica?", contains_row)

# Trocar dois eixos de uma matriz NumPy
transposed_matrix = np.transpose(matrix)
print("\nMatriz com os eixos trocados:")
print(transposed_matrix)

