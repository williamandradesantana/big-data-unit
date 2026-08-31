from scipy import stats

lamb = 4
k = 6

probabilidade = stats.poisson.pmf(k, lamb)

print(f"Probabilidade: {probabilidade:.4f}")
print(f"Porcentagem: {probabilidade * 100:.2f}%")
