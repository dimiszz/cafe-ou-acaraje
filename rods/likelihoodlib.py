import numpy as np
from markovlib import *

# Função para desenhar o progresso de um laço
def barrinha(actual, max_value):
    kamin = actual// (int) (max_value*0.1)
    tepan = (max_value-actual)// (int) (max_value*0.1)
    print(kamin * '=' + ">" +  tepan * '#', end="\r")

# Função para imprimir informações do likelihood
def print_info(time, likelihoods, max_index, dados):
    print("Tempo de execução:\t\t", time)
    print("Maior likelihood:\t\t", likelihoods)
    print("Índice do Maior likelihood:\t", max_index)
    print("Dado do Maior likelihood:\t", dados, "\n")

# Função para calcular os likelihoods SEM counter
def likelihoods(dados, jogadas):
    likelihoods = np.ones(len(dados))
    for (quantidade, label)  in jogadas:
        label = 3 if label == "Café" else 5
        for index, dice in enumerate(dados):
            markov = markov_chain(create_matrix(dice), quantidade)
            likelihoods[index] *= markov[0][label]
    return likelihoods

# Função para calcular os likelihoods COM counter
def likelihoods_c(dados, jogadas):
    likelihoods = np.ones(len(dados))
    for (quantidade, label), value in jogadas.items():
        label = 3 if label == "Café" else 5
        for index, dice in enumerate(dados):
            markov = markov_chain(create_matrix(dice), quantidade)
            likelihoods[index] *= (markov[0][label] ** value)
    return likelihoods

# Função para calcular os loglikelihoods SEM counter
def loglikelihoods(dados, jogadas):
    loglikelihoods = np.zeros(len(dados))
    for (quantidade, label) in jogadas:
        label = 3 if label == "Café" else 5
        for index, dice in enumerate(dados):
            markov = markov_chain(create_matrix(dice), quantidade)
            loglikelihoods[index] += np.log(markov[0][label])
    return loglikelihoods

# Função para calcular os loglikelihoods COM counter
def loglikelihoods_c(dados, jogadas):
    loglikelihoods = np.zeros(len(dados))
    for (quantidade, label), value in jogadas.items():
        label = 3 if label == "Café" else 5
        for index, dice in enumerate(dados):
            markov = markov_chain(create_matrix(dice), quantidade)
            loglikelihoods[index] += np.log(markov[0][label]) * value
    return loglikelihoods