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
    if printar:
        print(f"MATRIZ {1} POSIÇÃO:")
        print_matriz(actual)
    for i in range(1, quantidade):
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

