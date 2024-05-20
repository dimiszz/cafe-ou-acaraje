from markovlib import *
import numpy as np
from random import random
from time import sleep

data = np.empty((0, 6))

# Nesse teste, tento chegar em 70% de chance de cair em todos ao mesmo tempo:
# [(3, 'Café'), (1, 'Café'), (3, 'Café'), (2, 'Café'), (2, 'Café'), (3, 'Café'), (3, 'Café')]
# por exemplo, 70% de chance de em 3 jogadas cair em café,  70% de chance de em 1 jogada cair em Café, etc.
# Não é a ideia certa:
# dados geradores:  (0.9, 0.02, 0.02, 0.02, 0.02, 0.02)
# resultado obtido: (0.03, 0.07, 0.70, 0.08, 0.04, 0.08)
# comparação de suas matrizes de transição:
#           DADOS GERADORES:                        RESULTADO OBTIDO:
# MATRIZ 1 POSIÇÃO:
#        1    2    3    4    5    6            1    2    3    4    5    6
#  1 | 0.00 0.90 0.02 0.02 0.04 0.02     1 | 0.00 0.03 0.07 0.70 0.16 0.04
#  2 | 0.00 0.00 0.90 0.04 0.04 0.02     2 | 0.00 0.00 0.03 0.15 0.74 0.08
#  3 | 0.00 0.00 0.02 0.92 0.04 0.02     3 | 0.00 0.00 0.08 0.07 0.15 0.70
#  4 | 0.00 0.00 0.00 1.00 0.00 0.00     4 | 0.00 0.00 0.00 1.00 0.00 0.00
#  5 | 0.02 0.02 0.02 0.02 0.02 0.90     5 | 0.08 0.04 0.08 0.70 0.07 0.03
#  6 | 0.00 0.00 0.00 0.00 0.00 1.00     6 | 0.00 0.00 0.00 0.00 0.00 1.00

# MATRIZ 2 POSIÇÃO:
#        1    2    3    4    5    6            1    2    3    4    5    6
#  1 | 0.00 0.00 0.81 0.08 0.04 0.07     1 | 0.01 0.01 0.02 0.82 0.04 0.10
#  2 | 0.00 0.00 0.02 0.87 0.04 0.07     2 | 0.06 0.03 0.06 0.67 0.06 0.12
#  3 | 0.00 0.00 0.00 0.94 0.00 0.06     3 | 0.01 0.01 0.02 0.18 0.02 0.76
#  4 | 0.00 0.00 0.00 1.00 0.00 0.00     4 | 0.00 0.00 0.00 1.00 0.00 0.00
#  5 | 0.00 0.02 0.02 0.04 0.00 0.92     5 | 0.01 0.01 0.02 0.82 0.06 0.09
#  6 | 0.00 0.00 0.00 0.00 0.00 1.00     6 | 0.00 0.00 0.00 0.00 0.00 1.00

# MATRIZ 3 POSIÇÃO:
#        1    2    3    4    5    6            1    2    3    4    5    6
#  1 | 0.00 0.00 0.02 0.82 0.03 0.12     1 | 0.00 0.00 0.01 0.86 0.01 0.11
#  2 | 0.00 0.00 0.00 0.89 0.00 0.11     2 | 0.00 0.00 0.01 0.76 0.04 0.17
#  3 | 0.00 0.00 0.00 0.94 0.00 0.06     3 | 0.00 0.00 0.00 0.21 0.01 0.78
#  4 | 0.00 0.00 0.00 1.00 0.00 0.00     4 | 0.00 0.00 0.00 1.00 0.00 0.00
#  5 | 0.00 0.00 0.02 0.06 0.00 0.92     5 | 0.00 0.00 0.01 0.86 0.01 0.11
#  6 | 0.00 0.00 0.00 0.00 0.00 1.00     6 | 0.00 0.00 0.00 0.00 0.00 1.00
# ------------------------------------------------------------
# ------------------------------------------------------------


results = [(3, 'Café'), (1, 'Café'), (3, 'Café'), (2, 'Café'), (2, 'Café'), (3, 'Café'), (3, 'Café')]
# (15, "Acarajé"), (2, "Acarajé"), (3, "Café"), (4, "Acarajé"), (7, "Acarajé"), (1, "Café"), (2, "Café"),
# (3, "Café"), (2, "Acarajé")


for i in range(3):
    random_array = generate_random_dice()
    random_matrix = create_matrix(random_array)

    markovs = np.empty(len(results), dtype=float)
    for index, result in enumerate(results):
        random_markov = rodar_markov(random_matrix, result[0], False)
        cafe_ou_acaraje = 4 if result[1] == "Café" else 6
        markovs[index] = random_markov[0][cafe_ou_acaraje-1]

    while True: 
        if all(markovs > 0.7):
            break
        random_array = generate_random_dice()
        random_matrix = create_matrix(random_array)

        markovs = np.empty(len(results), dtype=float)
        for index, result in enumerate(results):
            random_markov = rodar_markov(random_matrix, result[0], False)
            cafe_ou_acaraje = 4 if result[1] == "Café" else 6
            markovs[index] = random_markov[0][cafe_ou_acaraje-1]
        #print_matriz(random_markov)
        #sleep(0.5)
    print(markovs)
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
random_markov = rodar_markov(random_matrix, 0, False)
print_matriz(rodar_markov(random_matrix, 1, False))
print_matriz(rodar_markov(random_matrix, 2, False))
print_matriz(rodar_markov(random_matrix, 3, False))