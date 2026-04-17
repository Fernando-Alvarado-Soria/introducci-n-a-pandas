import pandas as pd

# ============================================================
# 1. CARGAR EL DATASET
# ============================================================
df = pd.read_csv("GoogleApps.csv")


# ============================================================
# 2. EXPLORACIÓN BÁSICA DEL DATAFRAME
# ============================================================

# Ver las primeras 5 filas
print("--- HEAD ---")
print(df.head())

# Ver las últimas 5 filas
print("\n--- TAIL ---")
print(df.tail())

# Información general: columnas, tipos de dato y valores no nulos
print("\n--- INFO ---")
df.info()

# Estadísticas numéricas: media, desviación estándar, min, max, percentiles
print("\n--- DESCRIBE ---")
print(df.describe())


# ============================================================
# 3. PREGUNTAS SIMPLES CON FUNCIONES BÁSICAS
# ============================================================

# ¿Cuál es el promedio de calificación (Rating)?
print("\nPromedio de Rating:", df["Rating"].mean())

# ¿Cuál es la mediana de instalaciones (Installs)?
print("Mediana de Installs:", df["Installs"].median())

# ¿Cuánto cuesta la app más cara?
print("Precio máximo:", df["Price"].max())

# ¿Cuál es el tamaño mínimo de una app?
print("Tamaño mínimo:", df["Size"].min())


# ============================================================
# 4. FILTRADO DE DATOS - UNA CONDICIÓN
# ============================================================

# Filtrar apps con Rating mayor a 4.9
print("\n--- Apps con Rating > 4.9 ---")
apps_altas = df[df["Rating"] > 4.9]
print(apps_altas)

# Promedio de instalaciones de apps con Rating > 4.9
print("\nPromedio de Installs (Rating > 4.9):", df[df["Rating"] > 4.9]["Installs"].mean())


# ============================================================
# 5. FILTRADO DE DATOS - DOS CONDICIONES
# ============================================================

# Filtrar apps GRATUITAS con Rating mayor a 4.9
# IMPORTANTE: cada condición va entre paréntesis, y se unen con & (y) o | (o)
print("\n--- Apps GRATUITAS con Rating > 4.9 ---")
filtro_dos = df[(df["Rating"] > 4.9) & (df["Type"] == "Free")]
print(filtro_dos)

# Promedio de instalaciones de apps gratuitas con Rating > 4.9
print("\nPromedio de Installs (Gratuitas + Rating > 4.9):", filtro_dos["Installs"].mean())


# ============================================================
# 6. MINI EJERCICIOS PARA PRACTICAR EN CLASE
# ============================================================

# Ejercicio 1: ¿Cuántas apps son de tipo "Paid" (de pago)?
# print(len(df[df["Type"] == "Paid"]))

# Ejercicio 2: ¿Cuál es el promedio de Rating de las apps gratuitas?
# print(df[df["Type"] == "Free"]["Rating"].mean())

# Ejercicio 3: ¿Cuál es el máximo de Installs de apps con precio mayor a 0?
# print(df[df["Price"] > 0]["Installs"].max())

# Ejercicio 4: ¿Cuántas apps tienen más de 10,000,000 de instalaciones Y son gratuitas?
# print(len(df[(df["Installs"] > 10000000) & (df["Type"] == "Free")]))
