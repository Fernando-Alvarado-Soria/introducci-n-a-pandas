import pandas as pd

# 1. CARGAR EL DATASET
df = pd.read_csv("GoogleApps.csv")
# ============================================================

# Ejercicio 1:
print("Respuesta ejercicio 1: ")
print(len(df[df["Type"] == "Paid"]))
print("---")
# ============================================================

# Ejercicio 2:
print("Respuesta ejercicio 2: ")
print(df[df["Type"] == "Free"]["Rating"].mean())
print("---")
# ============================================================

# Ejercicio 3
print("Respuesta ejercicio 3: ")
print(df[df["Type"] == "Paid"]["Rating"].mean())
print("---")
# ============================================================

# Ejercicio 4
print("Respuesta ejercicio 4: ")
print(df[df["Price"] > 0]["Price"].max())
print("---")
# ============================================================

# Ejercicio 5
print("Respuesta ejercicio 5: ")
print(df[df["Category"] == "GAME"]["Installs"].mean())
print("---")
# ============================================================

# Ejercicio 6
print("Respuesta ejercicio 6: ")
print(len(df[(df["Rating"] >= 4.5) & (df["Type"] == "Free")]))
print("---")
# ============================================================

# Ejercicio 7
print("Respuesta ejercicio 7: ")
print(df[(df["Type"] == "Free") & (df["Rating"] > 4.0)]["Reviews"].mean())
print("---")
# ============================================================

# Ejercicio 8
print("Respuesta ejercicio 8: ")
print(df[(df["Category"] == "EDUCATION") & (df["Type"] == "Free")]["Rating"].mean())
print("---")
# ============================================================

# Ejercicio 9
print("Respuesta ejercicio 9: ")
print(len(df[(df["Installs"] >= 1000000) & (df["Type"] == "Paid")]))
print("---")
# ============================================================

# Ejercicio 10
print("Respuesta ejercicio 10: ")
print("Gratuitas:", df[df["Type"] == "Free"]["Installs"].mean())
print("De pago:  ", df[df["Type"] == "Paid"]["Installs"].mean())
print("---")
# ============================================================