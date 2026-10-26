import pandas as pd

clientes = pd.read_csv("informes/pruebas_codigo/clientes_400.csv").drop_duplicates()  # 400 clientes únicos
jovenes = clientes[(clientes["edad"] >= 18) & (clientes["edad"] <= 29)].copy()
jovenes["estrato"] = pd.cut(jovenes["edad"], bins=[17, 23, 29], labels=["18-23", "24-29"])

# Muestreo estratificado: 10 por estrato, con semilla para reproducibilidad
muestra = jovenes.groupby("estrato", observed=True, group_keys=False).sample(n=10, random_state=42)
print(muestra["estrato"].value_counts())



