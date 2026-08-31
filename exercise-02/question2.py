import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

media = 50
desvio_padrao = 10
tamanho_amostra = 1000

amostras = np.random.normal(media, desvio_padrao, tamanho_amostra)

x = np.linspace(10, 90, 500)

curva = stats.norm.pdf(x, media, desvio_padrao)

plt.hist(amostras, bins=30, density=True, alpha=0.7, label="Amostras")

plt.plot(x, curva, linewidth=2, label="Curva teórica")

plt.title("Distribuição Normal")
plt.xlabel("Valor")
plt.ylabel("Densidade")
plt.legend()
plt.show()
