# Notebook: Análisis Exploratorio de Ventas

# Paso 1: Importar librerías
import numpy as np
import pandas as pd

# Paso 2: Cargar los datos desde el archivo CSV
ruta_archivo = '../data/retail_sales_analysis.csv'
datos = np.genfromtxt(ruta_archivo, delimiter=',', dtype=str, skip_header=1)

# Paso 3: Definir los encabezados manualmente
headers = ['Transaction ID', 'Date', 'Customer ID', 'Gender', 'Age', 'Product Category', 'Quantity', 'Price per Unit', 'Total Amount']

# Convertir a DataFrame
df = pd.DataFrame(datos, columns=headers)

# Convertir tipos de datos
df['Total Amount'] = pd.to_numeric(df['Total Amount'], errors='coerce')
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna()

# Vista previa de los datos
df.head()
