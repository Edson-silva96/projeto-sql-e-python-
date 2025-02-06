import pandas as pd
import sqlite3

# Conecta ao banco de dados
connection = sqlite3.connect("base_varejo.db")

# Consulta SQL
query = """
    SELECT * FROM Vendas_varrejo
"""

# Lê os dados diretamente com a query
nova_variavel = pd.read_sql_query(query, connection)

print(nova_variavel.head())

connection.close()

