import numpy as np
import matplotlib.pyplot as plt

lamb = 1 / 20
tamanho_amostra = 1000

amostras = np.random.exponential(scale=1 / lamb, size=tamanho_amostra)

plt.hist(amostras, bins=30, density=True, alpha=0.7)

plt.title("Tempos entre falhas - Distribuição Exponencial")
plt.xlabel("Tempo entre falhas (horas)")
plt.ylabel("Densidade")
plt.show()
