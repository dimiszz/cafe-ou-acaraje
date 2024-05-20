import numpy as np
from markovlib import *
from random import random
from time import sleep
from collections import Counter

data = np.empty((0, 6))

quantidade = 10
print(f"Jogado {quantidade} vezes e caiu acarajé.")

for i in range(50):
    random_array = generate_random_dice()
    random_matrix = create_matrix(random_array)
    random_markov = rodar_markov(random_matrix, quantidade, False)
    while random_markov[0][5] < 0.3 or random_markov[0][3] < 0.3: # aceitamos o dado apenas se a probabilidade de cair acarajé for maior que 70%
        random_array = generate_random_dice()
        random_matrix = create_matrix(random_array)
        random_markov = rodar_markov(random_matrix, quantidade, False)


    data = np.vstack([data, random_array])

    print(f"{i+1} 1: {random_array[0]:.2f} \t 2: {random_array[1]:.2f}\t",
        f"3: {random_array[2]:.2f} \t 4: {random_array[3]:.2f} \t"
        f"5: {random_array[4]:.2f} \t 6: {random_array[5]:.2f}")


random_index = np.random.randint(0, 50)
random_dice = data[random_index]


print(f"Dado escolhido: {random_index+1}")
print(f"1: {random_dice[0]:.2f} \t 2: {random_dice[1]:.2f}\t",
    f"3: {random_dice[2]:.2f} \t 4: {random_dice[3]:.2f} \t"
    f"5: {random_dice[4]:.2f} \t 6: {random_dice[5]:.2f}")

# rodando para obter dados visuais
new_matrix = create_matrix(random_dice)
#print_matriz(new_matrix)
new_markov = np.dot(new_matrix, new_matrix)
#print_matriz(new_markov)
new_markov2 = np.dot(new_markov, new_matrix)
#print_matriz(new_markov2)
new_markov3 = np.dot(new_markov2, new_matrix)
#print_matriz(new_markov3)
new_markov4 = np.dot(new_markov3, new_matrix)
#print_matriz(new_markov4)
new_markov5 = np.dot(new_markov4, new_matrix)
#print_matriz(new_markov5)
new_markov10 = rodar_markov(new_matrix, 10000, False)
#print_matriz(new_markov10)


# Função para gerar amostragem
def lancar_dado(prob):
    return np.random.choice([1, 2, 3, 4, 5, 6], p=prob)

# Função que simula o jogo café ou acarajé
def cafe_ou_acaraje():
    jogos = 0
    amostra = []
    pos = 1
    while True:
        jogos += 1
        dado = lancar_dado(random_dice)
        pos += dado
        if pos > 6:
            pos = 12-pos
        if pos == 6 or pos == 4:
            return jogos
        
num_amostras2 = 10000
amostras2 = [cafe_ou_acaraje() for _ in range(num_amostras2)]
freq2 = Counter(amostras2) 
print(f"Quantidade de jogadas até terminar (n=10000):")
for i in range(1, 6):
    print(f"{i}: {freq2[i]} vezes")
print(f"Amostragem normalizada e probabilidade acumulada de Markov com dado {random_index+1}:")
print(f"Amostragem: 1: {freq2[1]/num_amostras2}, 2: {(freq2[1]+freq2[2])/num_amostras2}, 3: {(freq2[1]+freq2[2]+freq2[3])/num_amostras2}, 4: {(freq2[1]+freq2[2]+freq2[3]+freq2[4])/num_amostras2}, 5: {(freq2[1]+freq2[2]+freq2[3]+freq2[4]+freq2[5])/num_amostras2}, 6: {(freq2[1]+freq2[2]+freq2[3]+freq2[4]+freq2[5]+freq2[6])/num_amostras2}")
print(f"""Markov: 
      1: {round(new_matrix[0][3]+new_matrix[0][5], 3)}, 
      2: {round(new_markov[0][3]+new_markov[0][5], 3)}, 
      3: {round(new_markov2[0][3]+new_markov2[0][5], 3)},
      4: {round(new_markov3[0][3]+new_markov3[0][5], 3)}, 
      5: {round(new_markov4[0][3]+new_markov4[0][5], 3)}, 
      6: {round(new_markov5[0][3]+new_markov5[0][5], 3)},
      10: {round(new_markov10[0][3]+new_markov10[0][5], 3)}
""")
#rodamos markov 10 vezes para cada dado e calculamos o erro médio quadrático em comparação com amostragem normalizada
mse = []
for i in range(50):
    lista = []
    new_matrix = create_matrix(data[i])
    new_markov, lista = rodar_markov2(new_matrix, 9)
    soma = 0
    freq = 0
    for j in range(10):
        freq = freq + (freq2[j+1])/num_amostras2
        soma += (lista[j]-freq)**2
    
      
    soma = np.sqrt(soma/10)
    mse.append(soma)
    
#ordenando mse para pegar os 5 melhores dados
sorted_mse = np.argsort(mse)
print(f"Melhores dados com MSE calculado:")
for i in range(5):
    print(f"Dado {sorted_mse[i]+1}: {mse[sorted_mse[i]]:.2f}")





# calculando a média das probabilidades
#mean = np.mean(data, axis=0)
#print(f"Médias:")
#for i in range(6):
#    print(f"{i+1}: {mean[i]:.2f}")



# rodando markov com a média das probabilidades adquiridas:
#random_matrix = create_matrix(mean)
#random_markov = rodar_markov(random_matrix, quantidade, False)
#print_matriz(random_markov)

# Abaixo há alguns testes que foram feitos antes de chegar nos resultados
# (serão usados para documentação futura do processo de chegar no resultado):

# mat = np.array([
#     [ 0 , p1, p2, p3, p4+p6, p5],
#     [ 0 , 0, p1, p2+p6, p3+p5, p4],
#     [ 0 , 0, p6, p1+p5, p2+p4, p3],
#     [ 0 , 0, 0, 1, 0, 0],
#     [p6, p5, p4, p3, p2, p1],
#     [0, 0, 0, 0, 0, 1],
# ])

# mat2 = np.array([
#     [ 0 , p1, p2, p3, p4+p6, p5],
#     [ 0 , 0, p1, p2+p6, p3+p5, p4],
#     [ 0 , 0, p6, p1+p5, p2+p4, p3],
#     [ 0 , 0, 0, 0, 0, 0],
#     [p6, p5, p4, p3, p2, p1],
#     [0, 0, 0, 0, 0, 0],
# ])

# rodar_markov(mat, 5)
# print_matriz(mat)
#    1   2   3   4   5   6
# 1  0  1/6 1/6 1/6 2/6 1/6
# 2  0   0  1/6 2/6 2/6 1/6
# 3  0   0  1/6 2/6 2/6 1/6
# 4  0  1/6 1/6 1/6 2/6 1/6
# 5 1/6 2/6 1/6 1/6 1/6 1/6
# 6 1/6 2/6 1/6 1/6 1/6  0 


# MATRIZ 100 POSIÇÃO:
#        1    2    3    4    5    6
#  1 | 0.01 0.02 0.15 0.33 0.34 0.15
#  2 | 0.01 0.02 0.15 0.33 0.34 0.15
#  3 | 0.01 0.02 0.15 0.33 0.34 0.15
#  4 | 0.01 0.02 0.15 0.33 0.34 0.15
#  5 | 0.01 0.02 0.15 0.33 0.34 0.15
#  6 | 0.01 0.02 0.15 0.33 0.34 0.15


# MATRIZ 100 POSIÇÃO:
#        1    2    3    4    5    6
#  1 | 0.00 0.01 0.15 0.34 0.34 0.15
#  2 | 0.00 0.01 0.15 0.34 0.34 0.15
#  3 | 0.00 0.01 0.15 0.34 0.34 0.16
#  4 | 0.00 0.01 0.15 0.34 0.34 0.15
#  5 | 0.00 0.01 0.15 0.34 0.34 0.15
#  6 | 0.00 0.01 0.16 0.34 0.34 0.15

# RODADA QUE ACABOU + RESULTADO

