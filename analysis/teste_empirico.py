from markovlib import *
import numpy as np
from time import sleep
from random import random, choice
from collections import Counter

d1 = [0.3, 0.3, 0.3, 0.05, 0.05, 0]

d2 = [0, 0.05, 0.05, 0.3, 0.3, 0.3]

d3 = [0.16, 0.16, 0.16, 0.16, 0.16, 0.2]

d4 = [1, 0, 0, 0, 0, 0]

d5 = [0.5, 0.5, 0, 0, 0, 0]

results1 = [(2, 'Acarajé'), (1, 'Café'), (2, 'Acarajé'), (1, 'Café'), (1, 'Café'), (3, 'Café'), (1, 'Café'), (3, 'Café'), (1, 'Acarajé'), (3, 'Acarajé'), (1, 'Acarajé'), (2, 'Café'), (3, 'Café'), (2, 'Acarajé'), (1, 'Café'), (4, 'Acarajé'), (2, 'Acarajé'), (2, 'Café'), (4, 'Café'), (1, 'Café')]

results2 = [(1, 'Acarajé'), (4, 'Café'), (1, 'Acarajé'), (6, 'Café'), (1, 'Acarajé'), (3, 'Acarajé'), (1, 'Acarajé'), (3, 'Acarajé'), (1, 'Café'), (3, 'Acarajé'), (3, 'Café'), (2, 'Café'), (5, 'Café'), (1, 'Acarajé'), (3, 'Café'), (1, 'Acarajé'), (5, 'Café'), (3, 'Acarajé'), (1, 'Café'), (8, 'Acarajé')]

results3 = [(1, 'Café'), (3, 'Acarajé'), (1, 'Café'), (1, 'Acarajé'), (3, 'Café'), (3, 'Acarajé'), (1, 'Acarajé'), (6, 'Acarajé'), (2, 'Café'), (2, 'Café'), (2, 'Café'), (1, 'Café'), (1, 'Café'), (6, 'Café'), (3, 'Café'), (1, 'Acarajé'), (4, 'Café'), (3, 'Acarajé'), (1, 'Café'), (1, 'Acarajé')]

results4 = [(3, 'Café'), (3, 'Café'), (3, 'Café'), (3, 'Café'), (3, 'Café'), 
            (3, 'Café'), (3, 'Café'), (3, 'Café'), (3, 'Café'), (3, 'Café'), 
            (3, 'Café'), (3, 'Café'), (3, 'Café'), (3, 'Café'), (3, 'Café'), 
            (3, 'Café'), (3, 'Café'), (3, 'Café'), (3, 'Café'), (3, 'Café')]

results5 = [(2, 'Café'), (2, 'Café'), (2, 'Café'), (8, 'Acarajé'), (7, 'Acarajé'), (2, 'Café'), 
            (5, 'Acarajé'), (5, 'Acarajé'), (2, 'Café'), (3, 'Acarajé'), (6, 'Acarajé'), (2, 'Café'), 
            (2, 'Café'), (6, 'Acarajé'), (2, 'Café'), (3, 'Acarajé'), (2, 'Café'), (3, 'Acarajé'), 
            (2, 'Café'), (4, 'Acarajé')]

results = [results1, results2, results3, results4, results5]

dados = [d1, d2, d3, d4, d5]

for num_dado, result in enumerate(results):
    resultados = [0, 0, 0, 0, 0]

    for quantidade, label in result:
        label_numbered = 3 if label == "Café" else 5

        for index, dado in enumerate(dados):
            matrix = create_matrix(dado)
            markov = rodar_markov(matrix, quantidade, False)

            if markov[0][label_numbered] == 0 and num_dado == 4 and dado == d5:
                print("Quantidade em que ocorreu: ", quantidade, "Label: ", label)
                #print_matriz(matrix)
                markov = rodar_markov(matrix, quantidade, True)
                print(resultados[index])
                print(np.log(markov[0][label_numbered]))

            resultados[index] += np.log(markov[0][label_numbered])
            #print(f"Likelihood do dado {dado} em ({label}, {quantidade}): {resultados[index]}")

    for index, dado in enumerate(dados):
        print(f"Likelihood do dado {dado}: {resultados[index]}")
    print("Dado real: ", num_dado)
    print("Dado que consegui: ", resultados.index(max(resultados)))
    print("Quantidade de valores: ", len(result))
    print("---------------------------")
