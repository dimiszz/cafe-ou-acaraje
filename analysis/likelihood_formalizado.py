from markovlib import *
import numpy as np
from time import sleep
from random import random, choice
from collections import Counter

def arrays_sao_iguais(array1, array2):
    # Verifica se os tamanhos são iguais
    if len(array1) != len(array2):
        return False
    
    # Compara os elementos
    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return False
    
    return True




plot_x = np.zeros((10))
plot_y = np.zeros((10))

results = np.zeros(10)

for i in range(1,10):
    acertos = 0
    for i in range(100):
        
        dados = []
        for i in range(3):
            dados.append(generate_random_dice())
        
        dado_escolhido = choice(dados)
        
        jogadas = jogar_dados(100*i, probabilities=dado_escolhido)
        
        jogadas_unicas = Counter(jogadas)
        
        loglikelihoods = np.zeros(len(dados))
        
        for (quantidade, label), value in jogadas_unicas.items():
            label = 3 if label == "Café" else 5
            for index, dice in enumerate(dados):
                markov = rodar_markov(create_matrix(dice), quantidade=quantidade, printar=False)
                loglikelihoods[index] += np.log(markov[0][label]) * value
        
        max_index = np.argmax(loglikelihoods)
        
        if arrays_sao_iguais(dados[max_index], dado_escolhido):
            acertos += 1
    plot_x[i] = acertos/100
    plot_y[i] = 100*i

