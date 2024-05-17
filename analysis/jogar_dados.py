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

# p1 = 0.03
# p2 = 0.07
# p3 = 0.04
# p4 = 0.03
# p5 = 0.73
# p6 = 0.10


probabilities = np.array([p1, p2, p3, p4, p5, p6])
if probabilities.sum() != 1:
    raise ValueError("Probabilidades devem somar 1")
matrix = create_matrix(probabilities)
print_matriz(matrix)

# _ _ _ C _ A
# 1 2 3 4 5 6

# f(x) = pos + x, se pos + x <= 6 
# ou f(x) = |pos - x|, se pos + x > 6

data = []
array = np.empty(100, dtype=object)


for i in range(100):
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
    print(f"QUANTIDADE: {count}, RESULTADO: {cafe_ou_acaraje}")
    data.append((count, cafe_ou_acaraje))
    array[i] = cafe_ou_acaraje

print(np.count_nonzero(array == "Acarajé"))
print(np.count_nonzero(array == "Café"))
# [(15, "Acarajé"), (2, "Acarajé"), (3, "Café"), (4, "Acarajé"), (7, "Acarajé"), (1, "Café"), (2, "Café"),
#  (3, "Café"), (2, "Acarajé")]

print(data)




# DADO ORIGINAl:
# p1 = 0.4
# p2 = 0.1
# p3 = 0.05
# p4 = 0.3
# p5 = 0.1
# p6 = 0.05

# ACHADOS:
# Médias:
# 1: 0.04
# 2: 0.09
# 3: 0.09
# 4: 0.04
# 5: 0.69
# 6: 0.04
#        1    2    3    4    5    6
#  1 | 0.00 0.00 0.00 0.25 0.00 0.74
#  2 | 0.00 0.01 0.00 0.69 0.01 0.28
#  3 | 0.00 0.00 0.00 0.86 0.00 0.14
#  4 | 0.00 0.00 0.00 1.00 0.00 0.00
#  5 | 0.00 0.01 0.00 0.68 0.02 0.29
#  6 | 0.00 0.00 0.00 0.00 0.00 1.00




## DADO ORIGINAL: 
# p1 = 0.9
# p2 = 0.02
# p3 = 0.02
# p4 = 0.02
# p5 = 0.02
# p6 = 0.02
# Médias:
# 1: 0.03
# 2: 0.07
# 3: 0.04
# 4: 0.03
# 5: 0.73
# 6: 0.10
#        1    2    3    4    5    6
#  1 | 0.00 0.00 0.00 0.20 0.00 0.79
#  2 | 0.00 0.02 0.00 0.66 0.01 0.30
#  3 | 0.00 0.00 0.00 0.91 0.00 0.08
#  4 | 0.00 0.00 0.00 1.00 0.00 0.00
#  5 | 0.00 0.01 0.00 0.61 0.02 0.36
#  6 | 0.00 0.00 0.00 0.00 0.00 1.00