import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs('resultados', exist_ok=True)

df = pd.read_csv('datos/annual.csv')

print("=== ANÁLISIS DE DATOS CLIMÁTICOS ===\n")
print("Primeras 5 filas:")
print(df.head())
print("\n")

promedio = df['Mean'].mean()
maximo = df['Mean'].max()
minimo = df['Mean'].min()

print("=== RESULTADOS ===")
print(f"Temperatura promedio: {promedio:.2f} °C")
print(f"Temperatura máxima: {maximo:.2f} °C")
print(f"Temperatura mínima: {minimo:.2f} °C")

with open('resultados/resultados.txt', 'w') as f:
    f.write(f"Temperatura promedio: {promedio:.2f} °C\n")
    f.write(f"Temperatura máxima: {maximo:.2f} °C\n")
    f.write(f"Temperatura mínima: {minimo:.2f} °C\n")

plt.figure(figsize=(10, 5))
plt.plot(df['Year'], df['Mean'], color='blue')
plt.title('Evolución de la Temperatura Global')
plt.xlabel('Año')
plt.ylabel('Anomalía de Temperatura (°C)')
plt.grid(True, alpha=0.3)
plt.savefig('resultados/grafico.png')
plt.show()

print("\n✅ Resultados guardados en resultados/")
