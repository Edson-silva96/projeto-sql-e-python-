import sqlite3

connection = sqlite3.connect("base_varejo.db")

cursor = connection.cursor()

with open('vendas_varrejo1.csv', 'r') as file:
    records = 0
    next(file)  # Ignora o cabeçalho
    for row in file:
        # Remove espaços em branco e quebra de linha
        values = row.strip().split(",")
        
        # Converte os dados para os tipos corretos
        values[0] = int(float(values[0]))  # Id, se estiver vindo com ponto decimal
        values[7] = int(float(values[7]))  # Quantidade_venda
        values[8] = float(values[8])  # Valor_venda
        values[9] = float(values[9])  # Preço_por_unidade

        cursor.execute("INSERT INTO Vendas_varrejo1 VALUES (?,?,?,?,?,?,?,?,?,?)", values)
        connection.commit()
        records += 1

connection.close()
print('\n{} registros transferidos com sucesso!'.format(records))

