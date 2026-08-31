from scipy import stats

lamb = 2

probabilidade = stats.poisson.cdf(3, lamb)

print(f"Probabilidade: {probabilidade:.4f}")
print(f"Porcentagem: {probabilidade * 100:.2f}%")
