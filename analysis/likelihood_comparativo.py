from markovlib import *
import numpy as np
from time import sleep
from random import random, choice
from collections import Counter

# dado um conjunto de dados, encontre o dado que mais se assemelha ao conjunto de dados

p1 = 0.1
p2 = 0.1
p3 = 0.5
p4 = 0.05
p5 = 0.05
p6 = 0.2

probabilities = np.array([p1, p2, p3, p4, p5, p6])
if probabilities.sum() != 1:
    raise ValueError("Probabilidades devem somar 1")


# rodando para obter dados visuais
# new_matrix = create_matrix(probabilities)
# print_matriz(new_matrix)
# new_markov = np.dot(new_matrix, new_matrix)
# print_matriz(new_markov)
# new_markov2 = np.dot(new_markov, new_matrix)
# print_matriz(new_markov2)
# new_markov3 = np.dot(new_markov2, new_matrix)
# print_matriz(new_markov3)
# new_markov4 = np.dot(new_markov3, new_matrix)
# print_matriz(new_markov4)
# new_markov5 = np.dot(new_markov4, new_matrix)
# print_matriz(new_markov5)
# new_markov10 = rodar_markov(new_matrix, 10000, False)



#jogadas = jogar_dados(1000, probabilities=probabilities)

dados = []

#rand = (random() * 50) // 1 

for i in range(49):
    # if i == rand:
    #     dados.append(probabilities)
    #     continue
    dados.append(generate_random_dice())

dado_escolhido = choice(dados)

jogadas = jogar_dados(100, probabilities=dado_escolhido)

jogadas_unicas = Counter(jogadas)

print(jogadas_unicas)
print("maximo:",max(jogadas_unicas))

loglikelihoods = np.zeros(len(dados))

for (quantidade, label), value in jogadas_unicas.items():
    print("quantidade:", quantidade, "label:", label, "aconteceu:", value, "vezes")
    label = 3 if label == "Café" else 5
    for index, dice in enumerate(dados):
        markov = rodar_markov(create_matrix(dice), quantidade=quantidade, printar=False)
        # Somatório 
        loglikelihoods[index] += np.log(markov[0][label]) * value
    #loglikelihood += np.log(valor)*

print(loglikelihoods)
# find the index of the maximium value of this array
max_index = np.argmax(loglikelihoods)
print("Index of the maximum value:", max_index)
print("valor q ele falou q é o maior: ", loglikelihoods[max_index])
print("dado escolhido:", dados[max_index])
print("dado de verdade: ", dado_escolhido)


#        1    2    3    4    5    6
#  1 | 0.00 0.00 0.02 0.82 0.03 0.12
#  2 | 0.00 0.00 0.00 0.89 0.00 0.11
#  3 | 0.00 0.00 0.00 0.94 0.00 0.06
#  4 | 0.00 0.00 0.00 1.00 0.00 0.00
#  5 | 0.00 0.00 0.02 0.06 0.00 0.92
#  6 | 0.00 0.00 0.00 0.00 0.00 1.00