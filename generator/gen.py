import pandas as pd
import random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()

# Função para gerar datas aleatórias em um intervalo
def random_dates(start_date, end_date, n=10):
    date_list = [start_date + timedelta(days=random.randint(0, (end_date - start_date).days)) for _ in range(n)]
    return date_list

# Número de registros
num_employees = 20
num_products = 4
num_sales = 100000

# Tabela de Funcionários
employees = pd.DataFrame({
    'EmployeeID': range(1, num_employees + 1),
    'Name': [fake.name() for _ in range(num_employees)],
    'Group': [random.choice(['Sales Alpha', 'Sales Beta', 'Sales Sigma']) for _ in range(num_employees)],
})

# Tabela de Produtos (incluindo apenas os produtos desejados)
products = pd.DataFrame({
    'ProductID': range(1, num_products + 1),
    'ProductName': [
        'Cloud Computing - Tier A',
        'Cloud Computing - Tier S',
        'Virtual Network - Tier A',
        'Virtual Network - Tier S'
    ],
    'price_unit': [
        75.00,
        120.00,
        112.00,
        200.00
    ]
})

start_date = datetime(2013, 1, 1)
end_date = datetime(2023, 1, 1)

# Tabela de Vendas
sales = pd.DataFrame({
    'SaleID': range(1, num_sales + 1),
    'EmployeeID': [random.choice(employees['EmployeeID']) for _ in range(num_sales)],
    'ProductID': [random.choice(products['ProductID']) for _ in range(num_sales)],
    'SaleDate': random_dates(start_date, end_date, num_sales),
    'Quantity': [random.randint(1, 10) for _ in range(num_sales)],
    'Discount': [random.uniform(0, 0.2) for _ in range(num_sales)],
})

# Imprimir as tabelas geradas
print("Funcionários:")
print(employees)
employees.to_csv('data/employees.csv', index=False)

print("\nProdutos:")
print(products)
products.to_csv('data/products.csv', index=False)

print("\nVendas:")
print(sales)
sales.to_csv('data/sales.csv', index=False)
