import time
import numpy as np
from markovlib import *
from likelihoodlib import *
from random import choice
from collections import Counter
from matplotlib import pyplot as plt

quantidade_dados = 50
quantidade_jogadas = 100

dados = random_dice_array(quantidade_dados)
dado_escolhido = choice(dados)
jogadas = play_dice(quantidade_jogadas, dado_escolhido)
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
quantidade_testes = 50
quantidade_dados = 20

plot_y = np.zeros(quantidade_passos)
plot_x = np.zeros(quantidade_passos)

for k in range(quantidade_passos):
    acertos = 0

    for i in range(quantidade_testes):
        dados = dados = random_dice_array(quantidade_dados)
        dado_escolhido = choice(dados)
        jogadas = play_dice(passo*(k+1), dado_escolhido)
        jogadas_unicas = Counter(jogadas)

        loglikelihoods = loglikelihoods_c(dados, jogadas_unicas)
        max_index = np.argmax(loglikelihoods)

        if (dados[max_index] == dado_escolhido).all():
            acertos += 1
        
    plot_y[k] = acertos/quantidade_testes
    plot_x[k] = passo*k

    barrinha(k, quantidade_passos)

plt.title(f"Passo: {passo}, Quantidade de passos: {quantidade_passos}\nQuantidade de testes: {quantidade_testes}, Quantidade de dados: {quantidade_dados}")
plt.xlabel("Quantidade de jogadas")
plt.ylabel("Frequencia de acertos")
plt.plot(plot_x,plot_y)
plt.show()