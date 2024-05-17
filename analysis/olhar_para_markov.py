from markovlib import generate_random_dice, create_matrix, print_matriz, rodar_markov
import numpy as np
from time import sleep
from random import random

p1 = 0.9 
p2 = 0.02
p3 = 0.02
p4 = 0.02
p5 = 0.02
p6 = 0.02

probabilities = np.array([p1, p2, p3, p4, p5, p6])
if probabilities.sum() != 1:
    raise ValueError("Probabilidades devem somar 1")
matrix = create_matrix(probabilities)
#print_matriz(matrix)
rodar_markov(matrix, 3, True)

print("--"*30)
print("--"*30)
p1 = 0.03
p2 = 0.07
p3 = 0.70
p4 = 0.08
p5 = 0.04
p6 = 0.08

probabilities = np.array([p1, p2, p3, p4, p5, p6])
if not np.isclose(probabilities.sum(), 1):
    raise ValueError("Probabilidades devem somar 1, soma deu: ", probabilities.sum())
matrix = create_matrix(probabilities)
#print_matriz(matrix)

print_matriz(rodar_markov(matrix, 3, True))

#        1    2    3    4    5    6
#  1 | 0.00 0.00 0.02 0.82 0.03 0.12
#  2 | 0.00 0.00 0.00 0.89 0.00 0.11
#  3 | 0.00 0.00 0.00 0.94 0.00 0.06
#  4 | 0.00 0.00 0.00 1.00 0.00 0.00
#  5 | 0.00 0.00 0.02 0.06 0.00 0.92
#  6 | 0.00 0.00 0.00 0.00 0.00 1.00