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
    [ 0 , array[0], array[1], array[2], array[3]+array[5], array[4], 0],
    [ 0 , 0, array[0], array[1]+array[5], array[2]+array[4], array[3], 0],
    [ 0 , 0, array[5], array[0]+array[4], array[1]+array[3], array[2], 0],
    [ 0 , 0, 0, 0, 0, 0, 1],
    [array[5], array[4], array[3], array[2], array[1], array[0], 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0]
])

def printar_dados(array):
    print(f"1: {array[0]:.2f} \t 2: {array[1]:.2f}\t",
    f"3: {array[2]:.2f} \t 4: {array[3]:.2f} \t"
    f"5: {array[4]:.2f} \t 6: {array[5]:.2f}")

def jogar_dados(quantidade, probabilities):
    data = []
    if abs(probabilities.sum() - 1) > 0.001:
        raise ValueError("Probabilidades devem somar 1")
    for i in range(quantidade):
        posicao = 1
        count = 0
        while True:
            if posicao == 4 or posicao == 6:
                break
            count += 1
            dado = np.random.choice([1, 2, 3, 4, 5, 6], p=probabilities)
            if dado + posicao <= 6:
                posicao += dado
            else:
                posicao = abs(posicao - dado)
        cafe_ou_acaraje = "Café" if posicao == 4 else "Acarajé"
        data.append((count, cafe_ou_acaraje))
    return data