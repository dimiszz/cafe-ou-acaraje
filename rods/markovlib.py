import numpy as np
from random import random

# Função que gera um dado com array de 6 posições com números aleatórios
def random_dice():
    numbers = np.array([0, 0, 0, 0, 0, 0], dtype=float)
    for i in range(len(numbers)):
        numbers[i] = random()
    sum_numbers = sum(numbers)
    for i in range(len(numbers)):
        numbers[i] = numbers[i] / sum_numbers
    return numbers

# Função que gera um array de dados aleatórios
def random_dice_array(quantity):
    dados = []
    for i in range(quantity):
        dados.append(random_dice())
    return dados

# Função para criar uma matriz considerando as regras do jogo Café ou Acarajé
def create_matrix(p):
    return np.array([
    [    0    ,  p[0]   ,  p[1]   ,  p[2]   ,p[3]+p[5],  p[4]   ,    0    ],
    [    0    ,    0    ,  p[0]   ,p[1]+p[5],p[2]+p[4],  p[3]   ,    0    ],
    [    0    ,    0    ,  p[5]   ,p[0]+p[4],p[1]+p[3],  p[2]   ,    0    ],
    [    0    ,    0    ,    0    ,    0    ,    0    ,    0    ,    1    ],
    [  p[5]   ,  p[4]   ,  p[3]   ,  p[2]   ,  p[1]   ,  p[0]   ,    0    ],
    [    0    ,    0    ,    0    ,    0    ,    0    ,    0    ,    1    ],
    [    0    ,    0    ,    0    ,    0    ,    0    ,    0    ,    0    ]
])

# Função para calcular a matriz da cadeia de Markov
def markov_chain(matrix, quantity):
    actual = matrix
    for i in range(1, quantity):
        actual = np.dot(actual, matrix)
    return actual

# Função que simula o jogo Café ou Acarajé
def play_dice(quantity, probabilities):
    data = []
    for i in range(quantity):
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
                posicao = 12 - (dado + posicao)
        cafe_ou_acaraje = "Café" if posicao == 4 else "Acarajé"
        data.append((count, cafe_ou_acaraje))
    return data