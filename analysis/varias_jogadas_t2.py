from markovlib import *
import numpy as np
from random import random
from time import sleep
from collections import Counter

data1 = np.empty((0, 6))

results = jogar_dados(500, np.array([0.9, 0.02,0.02,0.02,0.02,0.02]))
results = jogar_dados(500, np.array([0.13, 0.13, 0.35, 0.13, 0.13, 0.13]))
# results = [(3, 'Café'), (1, 'Café'), (3, 'Café'), (2, 'Café'), (2, 'Café'), (3, 'Café'), 
# (3, 'Café'), (15, "Acarajé"), (2, "Acarajé"), (3, "Café"), (4, "Acarajé"), (7, "Acarajé"),
# (1, "Café"), (2, "Café"), (3, "Café"), (2, "Acarajé")]

teste = Counter(results) # quantidade, só preciso desse.

tamanho = len(results)

data = np.empty(50, dtype=float)

markovs = np.ones(len(teste), dtype=float)
referencias = np.zeros(len(teste), dtype=float)

random_array = generate_random_dice()
random_matrix = create_matrix(random_array)

vezes = 0

while True:
    for index, i in enumerate(teste.keys()):
        cafe_ou_acaraje = 4 if i[1] == "Café" else 6
        quantidade = i[0]
        referencias[index] = teste[i] / tamanho
        random_markov = rodar_markov(random_matrix, quantidade, False)
        markovs[index] = random_markov[0][cafe_ou_acaraje-1]
    if len(np.where(abs(markovs - referencias) < 0.1)) > 2:
        break
    random_array = generate_random_dice()
    random_matrix = create_matrix(random_array)
    vezes+= 1
    print(random_array)
printar_dados(random_array)
data1 = np.vstack([data1, random_array])
