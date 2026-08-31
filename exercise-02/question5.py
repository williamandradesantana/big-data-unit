from scipy import stats

N = 50
K = 10
n = 5
k = 2

probabilidade = stats.hypergeom.pmf(k, N, K, n)

print(f"Probabilidade: {probabilidade:.4f}")
print(f"Porcentagem: {probabilidade * 100:.2f}%")
