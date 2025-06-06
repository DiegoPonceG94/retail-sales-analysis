# Analisis Prediccion Ventas

import numpy as np
import pandas as pd

# Paso 1: Cargar los datos desde el archivo CSV
ruta_archivo = 'data/retail_sales_analysis.csv'
datos = np.genfromtxt(ruta_archivo, delimiter=',', dtype=str, skip_header=1)

# Paso 2: Definir los encabezados
headers = ['Transaction ID', 'Date', 'Customer ID', 'Gender', 'Age', 'Product Category', 'Quantity', 'Price per Unit', 'Total Amount']
df = pd.DataFrame(datos, columns=headers)

# Paso 3: Conversión de tipos de datos
df['Total Amount'] = pd.to_numeric(df['Total Amount'], errors='coerce')
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna()

# Paso 4: Análisis Exploratorio
# Total de ventas por categoría
total_por_categoria = df.groupby('Product Category')['Total Amount'].sum()

# Promedio de ventas diarias por categoría
promedio_diario = df.groupby(['Date', 'Product Category'])['Total Amount'].sum().groupby('Product Category').mean()

# Categorías con mayores y menores ventas
categoria_mayor_venta = total_por_categoria.idxmax()
categoria_menor_venta = total_por_categoria.idxmin()

# Paso 5: Manipulación de Datos
# Filtrar por una categoría específica
categoria_objetivo = 'Electronics'
ventas_filtradas = df[df['Product Category'] == categoria_objetivo]

# Estadísticas adicionales
suma_total = df['Total Amount'].sum()
resta_media = df['Total Amount'] - df['Total Amount'].mean()
multiplicacion_doble = df['Total Amount'] * 2
division_por_media = df['Total Amount'] / df['Total Amount'].mean()

# Mostrar resultados
print("Total por categoría:\n", total_por_categoria)
print("\nPromedio diario por categoría:\n", promedio_diario)
print(f"\nCategoría con mayor venta: {categoria_mayor_venta}")
print(f"Categoría con menor venta: {categoria_menor_venta}")

