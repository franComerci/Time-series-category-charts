import pandas as pd
import matplotlib.pyplot as plt



print("loading file...")

df = pd.read_excel('superstore_sales.xlsx', sheet_name='Orders')


df['order_date'] = pd.to_datetime(df['order_date'])

df = df.sort_values('order_date')


print("first graph...")

# date is the index
df_tiempo = df.set_index('order_date')

# 'M' means monthly frequency
ventas_mensuales = df_tiempo['sales'].resample('M').sum()

plt.figure(figsize=(10, 6))  

plt.plot(ventas_mensuales.index, ventas_mensuales.values, marker='o', linestyle='-', color='b')


plt.title('Monthly sales (tendence over time)')
plt.xlabel('Date')
plt.ylabel('Sales ($)')
plt.grid(True) 


plt.savefig('salesTendence.png')
plt.show()

# Second graph
print("Second graph...")


ventas_categoria = df.groupby('category')['sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))

ventas_categoria.plot(kind='bar', color='orange')

plt.title('Total sales by category')
plt.xlabel('Category')
plt.ylabel('Sales ($)')
plt.xticks(rotation=0) # Que los nombres se lean horizontales

plt.savefig('SalesByCategory.png')
plt.show()

# third graph

print("third graph...")

plt.figure(figsize=(7, 7))
# autopct='%1.1f%%' es lo que hace que salgan los numeritos de porcentaje
plt.pie(ventas_categoria, labels=ventas_categoria.index, autopct='%1.1f%%', startangle=140)

plt.title('Sales Participation by Category')

plt.savefig('MarketSales.png')
plt.show()


#Summary
print("\n--- Summary ---")
print(f"Total sales: ${df['sales'].sum():,.2f}")
print(f"Most sold category: {ventas_categoria.idxmax()} (${ventas_categoria.max():,.2f})")
print(f"Least sold category: {ventas_categoria.idxmin()} (${ventas_categoria.min():,.2f})")
print(f"Month with most sales: {ventas_mensuales.idxmax().strftime('%B %Y')}")
print("-------------------------")
