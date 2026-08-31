import numpy as np
import matplotlib.pyplot as plt

n = 20
p = 0.7
tamanho_amostra = 1000

amostras = np.random.binomial(n, p, tamanho_amostra)

plt.hist(amostras, bins=np.arange(-0.5, n + 1.5, 1), density=True, alpha=0.7)

plt.title("Distribuição Binomial")
plt.xlabel("Número de sucessos")
plt.ylabel("Frequência relativa")
plt.show()
