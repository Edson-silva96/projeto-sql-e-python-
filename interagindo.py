import sqlite3

# Conecta ao banco de dados
connection = sqlite3.connect("base_varejo.db")

cursor = connection.cursor()

# Consulta a tabela completa
cursor.execute("SELECT * FROM Vendas_varrejo1")

#cursor.execute("SELECT * FROM Vendas_varrejo1 WHERE Uf_da_compra = 'SP'")

# Recupera todos os registros
records = cursor.fetchall()

# Exibe os registros
for row in records:
    print(row)

connection.close()
