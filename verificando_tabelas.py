import sqlite3

# Conecta ao banco de dados
connection = sqlite3.connect("base_varejo.db")

cursor = connection.cursor()

# Consulta para listar as tabelas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Recupera os nomes das tabelas
tables = cursor.fetchall()

print("Tabelas no banco de dados:")
for table_name in tables:
    print(table_name[0])

connection.close()
