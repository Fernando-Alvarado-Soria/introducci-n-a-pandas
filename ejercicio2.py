import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("GoogleApps.csv")

# Promedio de Rating por tipo (Free vs Paid)
promedios = df.groupby("Type")["Rating"].mean()

promedios.plot(kind="bar", color=["steelblue", "orange"])
plt.title("Promedio de Rating: Gratuitas vs De Pago")
plt.ylabel("Rating promedio")
plt.xlabel("Tipo de app")
plt.tight_layout()
plt.show()