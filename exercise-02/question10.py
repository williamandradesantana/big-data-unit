import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

n = 10
p = 0.3

k = np.arange(0, n + 1)

probabilidades = stats.binom.pmf(k, n, p)

probabilidade = stats.binom.cdf(6, n, p) - stats.binom.cdf(2, n, p)

plt.bar(k, probabilidades)

plt.title("Distribuição Binomial")
plt.xlabel("Número de sucessos")
plt.ylabel("Probabilidade")
plt.xticks(k)
plt.show()

print(f"P(3 <= X <= 6) = {probabilidade:.6f}")
print(f"Porcentagem = {probabilidade * 100:.2f}%")
