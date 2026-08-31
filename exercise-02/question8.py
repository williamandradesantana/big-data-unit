import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

media = 0
desvio_padrao = 1
tamanho_amostra = 2000

amostras = np.random.normal(media, desvio_padrao, tamanho_amostra)

x = np.linspace(-4, 4, 500)

curva = stats.norm.pdf(x, media, desvio_padrao)

plt.hist(amostras, bins=35, density=True, alpha=0.7, label="Amostras")

plt.plot(x, curva, linewidth=2, label="Curva teórica")

plt.title("Distribuição Normal Padrão")
plt.xlabel("Valor")
plt.ylabel("Densidade")
plt.legend()
plt.show()
