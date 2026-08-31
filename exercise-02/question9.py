import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

lamb = 0.2

x = np.linspace(0, 50, 500)

densidade = stats.expon.pdf(x, scale=1 / lamb)

plt.plot(x, densidade, linewidth=2)

plt.title("Função Densidade da Distribuição Exponencial")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True, alpha=0.3)
plt.show()
