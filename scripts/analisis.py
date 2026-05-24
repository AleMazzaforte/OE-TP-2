import pandas as pd
import matplotlib.pyplot as plt


# Leer el archivo CSV
df = pd.read_csv('datos/annual.csv')

print("=== ANALISIS DE DATOS CLIMATICOS ===\n")
print("Primeras 5 filas:")
print(df.head())
print("\n")

# Calcular indicadores
promedio = df['Mean'].mean()
maximo = df['Mean'].max()
minimo = df['Mean'].min()

print("=== RESULTADOS ===")
print(f"Temperatura promedio: {promedio:.2f} °C")
print(f"Temperatura maxima: {maximo:.2f} °C")
print(f"Temperatura minima: {minimo:.2f} °C")

# Guardar resultados en archivo de texto
with open('resultados/resultados.txt', 'w') as f:
    f.write("RESULTADOS DEL ANALISIS CLIMATICO\n")
    f.write("================================\n")
    f.write(f"Temperatura promedio: {promedio:.2f} °C\n")
    f.write(f"Temperatura maxima: {maximo:.2f} °C\n")
    f.write(f"Temperatura minima: {minimo:.2f} °C\n")

# Generar grafico
plt.figure(figsize=(10, 5))
plt.plot(df['Year'], df['Mean'], color='blue', linewidth=1)
plt.title('Evolucion de la Temperatura Global')
plt.xlabel('Año')
plt.ylabel('Anomalia de Temperatura (°C)')
plt.grid(True, alpha=0.3)
plt.savefig('resultados/grafico.png')
plt.show()

print("\n✅ Resultados guardados en resultados/")
print("   - resultados.txt")
print("   - grafico.png")
