from scipy.stats import binom

n = 10
k = 7
p = 0.5

probabilidade = binom.pmf(k, n, p)

print(f"Probabilidade: {probabilidade:.4f}")
print(f"Porcentagem: {probabilidade * 100:.2f}%")
