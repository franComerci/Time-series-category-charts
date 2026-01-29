import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# PASO 1: CARGA Y LIMPIEZA DE DATOS
# ---------------------------------------------------------
print("Cargando archivo...")
# Cargamos el archivo CSV. Asegúrate de que el archivo esté en la misma carpeta que este script.
df = pd.read_excel('superstore_sales.xlsx', sheet_name='Orders')

# Convertimos la columna de fecha (que suele ser texto) a formato fecha real
df['order_date'] = pd.to_datetime(df['order_date'])

# Ordenamos por fecha (vital para gráficos de tiempo)
df = df.sort_values('order_date')

# ---------------------------------------------------------
# PASO 2: GRÁFICO DE LÍNEA (VENTAS MENSUALES)
# ---------------------------------------------------------
print("Generando gráfico de tendencias...")

# Ponemos la fecha como índice para poder agrupar por mes
df_tiempo = df.set_index('order_date')

# 'M' significa Mensual. Sumamos las ventas de cada mes.
ventas_mensuales = df_tiempo['sales'].resample('M').sum()

plt.figure(figsize=(10, 6))  # Tamaño del gráfico
# Dibujamos la línea
plt.plot(ventas_mensuales.index, ventas_mensuales.values, marker='o', linestyle='-', color='b')

# Estética (Etiquetas y Títulos)
plt.title('Tendencia de Ventas Mensuales (Global)')
plt.xlabel('Fecha')
plt.ylabel('Ventas Totales ($)')
plt.grid(True) # Cuadrícula de fondo

# Guardar y mostrar
plt.savefig('1_tendencia_ventas.png')
plt.show()

# ---------------------------------------------------------
# PASO 3: GRÁFICO DE BARRAS (POR CATEGORÍA)
# ---------------------------------------------------------
print("Generando gráfico de categorías...")

# Agrupamos por Categoría y sumamos las ventas
ventas_categoria = df.groupby('category')['sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
# Dibujamos las barras. 'kind=bar' es la clave.
ventas_categoria.plot(kind='bar', color='orange')

plt.title('Ventas Totales por Categoría')
plt.xlabel('Categoría')
plt.ylabel('Ventas ($)')
plt.xticks(rotation=0) # Que los nombres se lean horizontales

plt.savefig('2_ventas_por_categoria.png')
plt.show()

# ---------------------------------------------------------
# PASO 4: GRÁFICO DE PASTEL (SHARE DE MERCADO)
# ---------------------------------------------------------
print("Generando gráfico de participación...")

plt.figure(figsize=(7, 7))
# autopct='%1.1f%%' es lo que hace que salgan los numeritos de porcentaje
plt.pie(ventas_categoria, labels=ventas_categoria.index, autopct='%1.1f%%', startangle=140)

plt.title('Participación de Ventas por Categoría (Share)')

plt.savefig('3_share_mercado.png')
plt.show()

# ---------------------------------------------------------
# PASO 5: RESUMEN EJECUTIVO (TEXTO)
# ---------------------------------------------------------
print("\n--- RESUMEN EJECUTIVO ---")
print(f"Total de Ventas Analizadas: ${df['sales'].sum():,.2f}")
print(f"Categoría Más Vendida: {ventas_categoria.idxmax()} (${ventas_categoria.max():,.2f})")
print(f"Categoría Menos Vendida: {ventas_categoria.idxmin()} (${ventas_categoria.min():,.2f})")
print(f"Mes con más ventas: {ventas_mensuales.idxmax().strftime('%B %Y')}")
print("-------------------------")
print("¡Listo! Se han generado 3 imágenes PNG y el resumen.")