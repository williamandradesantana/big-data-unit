from __init__ import jm1_data
import matplotlib.pyplot as plt

# Histograma de LOC
plt.hist(jm1_data["loc"], bins=10)

plt.title("Distribuição de LOC")
plt.xlabel("LOC")
plt.ylabel("Frequência")

plt.show()


# Histograma de N
plt.hist(jm1_data["n"], bins=10)

plt.title("Distribuição de N")
plt.xlabel("N")
plt.ylabel("Frequência")

plt.show()


# Histograma de V(G)
plt.hist(jm1_data["v(g)"], bins=10)

plt.title("Distribuição de V(G)")
plt.xlabel("V(G)")
plt.ylabel("Frequência")

plt.show()


plt.boxplot(jm1_data["loc"])
plt.title("Boxplot de LOC")
plt.ylabel("LOC")

plt.show()


quantity_defects = jm1_data["defects"].value_counts()
print(quantity_defects)

quantity_defects.plot(kind="bar")

plt.title("Módulos com e sem defeitos")
plt.xlabel("Defeito")
plt.ylabel("Quantidade de módulos")

plt.show()