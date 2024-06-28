from markovlib import *
import numpy as np
from random import choice
from collections import Counter

# dado um conjunto de dados, encontre o dado que mais se assemelha ao conjunto de dados
dados = []

for i in range(49):
    dados.append(generate_random_dice())

dado_escolhido = choice(dados)
jogadas = jogar_dados(100, probabilities=dado_escolhido)
jogadas_unicas = Counter(jogadas)

# LIKELIHOOD SEM COUNTER
print(jogadas)

likelihoods = np.ones(len(dados))
for (quantidade, label)  in jogadas:
    #print("quantidade:", quantidade, "label:", label)
    label = 3 if label == "Café" else 5
    for index, dice in enumerate(dados):
        markov = rodar_markov(create_matrix(dice), quantidade=quantidade, printar=False)
        likelihoods[index] *= markov[0][label]
max_index = np.argmax(likelihoods)

print(likelihoods)
print("Index of the maximum value:", max_index)
print("valor q ele falou q é o maior: ", likelihoods[max_index])
print("dado escolhido:", dados[max_index])
print("dado de verdade: ", dado_escolhido)
print()

# LIKELIHOOD COM COUNTER
print(jogadas_unicas)

likelihoods = np.ones(len(dados))
for (quantidade, label), value in jogadas_unicas.items():
    #print("quantidade:", quantidade, "label:", label, "aconteceu:", value, "vezes")
    label = 3 if label == "Café" else 5
    for index, dice in enumerate(dados):
        markov = rodar_markov(create_matrix(dice), quantidade=quantidade, printar=False)
        likelihoods[index] *= (markov[0][label] ** value)
max_index = np.argmax(likelihoods)

print(likelihoods)
print("Index of the maximum value:", max_index)
print("valor q ele falou q é o maior: ", likelihoods[max_index])
print("dado escolhido:", dados[max_index])
print("dado de verdade: ", dado_escolhido)
print()

# LOGLIKELIHOOD SEM COUNTER
print(jogadas)

loglikelihoods = np.zeros(len(dados))
for (quantidade, label) in jogadas:
    #print("quantidade:", quantidade, "label:", label)
    label = 3 if label == "Café" else 5
    for index, dice in enumerate(dados):
        markov = rodar_markov(create_matrix(dice), quantidade=quantidade, printar=False)
        loglikelihoods[index] += np.log(markov[0][label])
max_index = np.argmax(loglikelihoods)

print(loglikelihoods)
print("Index of the maximum value:", max_index)
print("valor q ele falou q é o maior: ", loglikelihoods[max_index])
print("dado escolhido:", dados[max_index])
print("dado de verdade: ", dado_escolhido)
print()

# LOGLIKELIHOOD COM COUNTER
print(jogadas_unicas)

loglikelihoods = np.zeros(len(dados))
for (quantidade, label), value in jogadas_unicas.items():
    #print("quantidade:", quantidade, "label:", label, "aconteceu:", value, "vezes")
    label = 3 if label == "Café" else 5
    for index, dice in enumerate(dados):
        markov = rodar_markov(create_matrix(dice), quantidade=quantidade, printar=False)
        loglikelihoods[index] += np.log(markov[0][label]) * value
max_index = np.argmax(loglikelihoods)

print(loglikelihoods)
print("Index of the maximum value:", max_index)
print("valor q ele falou q é o maior: ", loglikelihoods[max_index])
print("dado escolhido:", dados[max_index])
print("dado de verdade: ", dado_escolhido)
print()