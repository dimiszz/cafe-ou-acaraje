import time
import numpy as np
from markovlib import *
from likelihoodlib import *
from random import choice
from collections import Counter
from matplotlib import pyplot as plt

quantidade_dados = 50
dados = []
for i in range(quantidade_dados):
    dados.append(random_dice())

dado_escolhido = choice(dados)
jogadas = play_dice(100, dado_escolhido)
jogadas_unicas = Counter(jogadas)

#print("########## JOGADAS ##########")
#print(jogadas, "\n")

#print("########## JOGADAS UNICAS ##########")
#print(jogadas_unicas, "\n")

print("########## DADO ESCOLHIDO ##########")
print("Dado escolhido:\t\t\t", dado_escolhido, "\n")

print("########## LIKELIHOOD SEM COUNTER ##########")
start = time.time()
likelihoods = likelihoods(dados, jogadas)
max_index = np.argmax(likelihoods)
end = time.time()

print_info(end - start, likelihoods[max_index], max_index, dados[max_index])

print("########## LIKELIHOOD COM COUNTER ##########")
start = time.time()
likelihoods = likelihoods_c(dados, jogadas_unicas)
max_index = np.argmax(likelihoods)
end = time.time()

print_info(end - start, likelihoods[max_index], max_index, dados[max_index])

print("########## LOGLIKELIHOOD SEM COUNTER ##########")
start = time.time()
loglikelihoods = loglikelihoods(dados, jogadas)
max_index = np.argmax(loglikelihoods)
end = time.time()

print_info(end - start, likelihoods[max_index], max_index, dados[max_index])

print("########## LOGLIKELIHOOD COM COUNTER ##########")
start = time.time()
loglikelihoods = loglikelihoods_c(dados, jogadas_unicas)
max_index = np.argmax(loglikelihoods)
end = time.time()

print_info(end - start, likelihoods[max_index], max_index, dados[max_index])

print("########## GRÁFICO ##########")
passo = 2
quantidade_passos = 100
quantidade_dados = 20

plot_y = np.zeros(quantidade_passos)
plot_x = np.zeros(quantidade_passos)

for k in range(1, quantidade_passos+1):
    acertos = 0
    for i in range(50):
        dados = []
        for i in range(quantidade_dados):
            dados.append(random_dice())
        
        dado_escolhido = choice(dados)
        jogadas = play_dice(passo*k, dado_escolhido)
        jogadas_unicas = Counter(jogadas)

        likelihoods = likelihoods_c(dados, jogadas_unicas)
        max_index = np.argmax(likelihoods)

        if (dados[max_index] == dado_escolhido).all():
            acertos += 1
    plot_y[k-1] = acertos/50
    plot_x[k-1] = passo*k

    barrinha(k, quantidade_passos)

plt.title(f"Passo {passo}, Quantidade de passos{quantidade_passos}")
plt.xlabel("quantidade de jogadas")
plt.ylabel("Frequencia de acertos")
plt.plot(plot_x,plot_y)
plt.show()