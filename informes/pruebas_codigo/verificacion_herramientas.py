## UTILIZAR AL TENER LOS DATOS

import pandas as pd

df = pd.read_csv("plantillas/encuesta_respuestas.csv")

print("Tipos por columna:")
print(df.dtypes)

print("\nDatos faltantes por columna:")
print(df.isna().sum())

# Solo respuestas reales para la interpretación de sesgos
reales = df[df["origen"] == "real"]

for col in ["satisfaccion_general", "recomendaria"]:
    print(f"\nDistribución de {col} (solo reales):")
    print(reales[col].value_counts(dropna=False).sort_index())



    