import numpy as np
from random import random
from time import sleep

# Função que gera um array de 6 posições com números aleatórios
def generate_random_dice():
    numbers = np.array([0, 0, 0, 0, 0, 0], dtype=float)
    for i in range(len(numbers)):
        numbers[i] = random()
    sum_numbers = sum(numbers)
    for i in range(len(numbers)):
        numbers[i] = numbers[i] / sum_numbers
    return numbers

# Função que imprime uma matriz
# matrix: matriz a ser impressa
def print_matriz(matrix):
        # Criar labels para as linhas
    labels = np.arange(1, matrix.shape[0] + 1)

    # Imprimir labels das colunas
    print("   ", end="")
    for j in range(matrix.shape[1]):
        print(f"{j+1:5}", end="")
    print()

    # Imprimir matriz com labels das linhas
    for i in range(matrix.shape[0]):
        print(f"{labels[i]:2} |", end="")
        for j in range(matrix.shape[1]):
            print(f"{matrix[i, j]:5.2f}", end="")
        print()

# Roda o algoritmo de Markov
# matrix: matriz de transição inicial
# quantidade: passos de Markov
# printar: se True, imprime as matrizes intermediárias
def rodar_markov(matrix, quantidade, printar=True):
    actual = matrix
    for i in range(quantidade):
        if printar:
            print()
            print(f"MATRIZ {i+1} POSIÇÃO:")
        actual = np.dot(actual, matrix)
        if printar:
            print_matriz(actual)
    return actual

# Cria uma matriz considerando as regras do jogo Café ou Acarajé
# array: array com as probabilidades de cada dado
def create_matrix(array):
    return np.array([
    [ 0 , array[0], array[1], array[2], array[3]+array[5], array[4]],
    [ 0 , 0, array[0], array[1]+array[5], array[2]+array[4], array[3]],
    [ 0 , 0, array[5], array[0]+array[4], array[1]+array[3], array[2]],
    [ 0 , 0, 0, 1, 0, 0],
    [array[5], array[4], array[3], array[2], array[1], array[0]],
    [0, 0, 0, 0, 0, 1],
])


# Sequência de linhas para gerar a matriz de transição com valores fixos:
# p1 = 1/6
# p2 = 1/6
# p3 = 1/6
# p4 = 1/6
# p5 = 1/6
# p6 = 1/6
# array = np.array([p1, p2, p3, p4, p5, p6])
# matrix = create_matrix(array)
# result = rodar_markov(matrix, 5, False)
# print_matriz(matrix)

data = np.empty((0, 6))

quantidade = 6
print(f"Jogado {quantidade} vezes e caiu acarajé.")

for i in range(50):
    random_array = generate_random_dice()
    random_matrix = create_matrix(random_array)
    random_markov = rodar_markov(random_matrix, quantidade, False)
    while random_markov[0][5] < 0.7: # aceitamos o dado apenas se a probabilidade de cair acarajé for maior que 70%
        random_array = generate_random_dice()
        random_matrix = create_matrix(random_array)
        random_markov = rodar_markov(random_matrix, quantidade, False)
        #print_matriz(random_markov)
        #sleep(0.5)
    #print_matriz(random_markov)
    #print(f"PROBABILIDADE DOS DADOS:")

    data = np.vstack([data, random_array])

    print(f"1: {random_array[0]:.2f} \t 2: {random_array[1]:.2f}\t",
        f"3: {random_array[2]:.2f} \t 4: {random_array[3]:.2f} \t"
        f"5: {random_array[4]:.2f} \t 6: {random_array[5]:.2f}")

# calculando a média das probabilidades
mean = np.mean(data, axis=0)
print(f"Médias:")
for i in range(6):
    print(f"{i+1}: {mean[i]:.2f}")

# rodando markov com a média das probabilidades adquiridas:
random_matrix = create_matrix(mean)
random_markov = rodar_markov(random_matrix, quantidade, False)
print_matriz(random_markov)

# Abaixo há alguns testes que foram feitos antes de chegar nos resultados
# (serão usados para documentação futura do processo de chegar no resultado):

# mat = np.array([
#     [ 0 , p1, p2, p3, p4+p6, p5],
#     [ 0 , 0, p1, p2+p6, p3+p5, p4],
#     [ 0 , 0, p6, p1+p5, p2+p4, p3],
#     [ 0 , 0, 0, 1, 0, 0],
#     [p6, p5, p4, p3, p2, p1],
#     [0, 0, 0, 0, 0, 1],
# ])

# mat2 = np.array([
#     [ 0 , p1, p2, p3, p4+p6, p5],
#     [ 0 , 0, p1, p2+p6, p3+p5, p4],
#     [ 0 , 0, p6, p1+p5, p2+p4, p3],
#     [ 0 , 0, 0, 0, 0, 0],
#     [p6, p5, p4, p3, p2, p1],
#     [0, 0, 0, 0, 0, 0],
# ])

# rodar_markov(mat, 5)
# print_matriz(mat)
#    1   2   3   4   5   6
# 1  0  1/6 1/6 1/6 2/6 1/6
# 2  0   0  1/6 2/6 2/6 1/6
# 3  0   0  1/6 2/6 2/6 1/6
# 4  0  1/6 1/6 1/6 2/6 1/6
# 5 1/6 2/6 1/6 1/6 1/6 1/6
# 6 1/6 2/6 1/6 1/6 1/6  0 


# MATRIZ 100 POSIÇÃO:
#        1    2    3    4    5    6
#  1 | 0.01 0.02 0.15 0.33 0.34 0.15
#  2 | 0.01 0.02 0.15 0.33 0.34 0.15
#  3 | 0.01 0.02 0.15 0.33 0.34 0.15
#  4 | 0.01 0.02 0.15 0.33 0.34 0.15
#  5 | 0.01 0.02 0.15 0.33 0.34 0.15
#  6 | 0.01 0.02 0.15 0.33 0.34 0.15


# MATRIZ 100 POSIÇÃO:
#        1    2    3    4    5    6
#  1 | 0.00 0.01 0.15 0.34 0.34 0.15
#  2 | 0.00 0.01 0.15 0.34 0.34 0.15
#  3 | 0.00 0.01 0.15 0.34 0.34 0.16
#  4 | 0.00 0.01 0.15 0.34 0.34 0.15
#  5 | 0.00 0.01 0.15 0.34 0.34 0.15
#  6 | 0.00 0.01 0.16 0.34 0.34 0.15

# RODADA QUE ACABOU + RESULTADO


