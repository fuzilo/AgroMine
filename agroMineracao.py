import pandas as pd
import csv
from datetime import datetime

resultado = []

with open ('vendas_agricolas.csv', 'r', encoding='utf-8') as f:
    
    df = pd.read_csv(f)

print(df.head(5))

print(df.describe())

print('A menor quantidade vendida foi de 14. O produto foi Tomate, na região Oeste ')
print('A maior quantidade vendida foi de 494.')
print('A quantidade média vendia foi de 246,12')
print('Desvio padrão foi de 139.32')
print('No primeiro quartil tivemos 135,25 quantidades vendidas')
print('Na mediana temos 240 quantidades vendidas')
print('No terceiro quartil tivemos 362,75 quantidades vendidas')

print('Tendo sido a média próximo ao segundo quartil, ou seja, metade das vendas foram feitas aproximadamente até a metade do período, pode-se dizer que as vendas foram estáveis, sem uma alta ou queda significativa nas vendas')


df.describe()   


media_qtd = df['quantidade_vendida'].mean()
std_qtd = df['quantidade_vendida'].std()

# Para preço unitário
media_preco = df['preco_unitario'].mean()
std_preco = df['preco_unitario'].std()

print(f"Média de quantidade vendida: {media_qtd:.2f}")
print(f"Desvio padrão da quantidade: {std_qtd:.2f}")
print(f"\nMédia de preço unitário: R$ {media_preco:.2f}")
print(f"Desvio padrão do preço: R$ {std_preco:.2f}")