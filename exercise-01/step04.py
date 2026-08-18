from __init__ import data
import matplotlib.pyplot as plt

# Histograma de LOC
plt.hist(data["loc"], bins=10)

plt.title("Distribuição de LOC")
plt.xlabel("LOC")
plt.ylabel("Frequência")

plt.show()


# Histograma de N
plt.hist(data["n"], bins=10)

plt.title("Distribuição de N")
plt.xlabel("N")
plt.ylabel("Frequência")

plt.show()


# Histograma de V(G)
plt.hist(data["v(g)"], bins=10)

plt.title("Distribuição de V(G)")
plt.xlabel("V(G)")
plt.ylabel("Frequência")

plt.show()


plt.boxplot(data["loc"])
plt.title("Boxplot de LOC")
plt.ylabel("LOC")

plt.show()


quantity_defects = data["defects"].value_counts()
print(quantity_defects)

quantity_defects.plot(kind="bar")

plt.title("Módulos com e sem defeitos")
plt.xlabel("Defeito")
plt.ylabel("Quantidade de módulos")

plt.show()