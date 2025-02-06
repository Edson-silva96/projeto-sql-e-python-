import sqlite3

corn = sqlite3.connect('base_varejo.db')

cur = corn.cursor()

sql = """
CREATE TABLE Vendas_varrejo1 (
    Id INTEGER,
    Data_da_venda TEXT,
    Nome_da_loja TEXT,
    Uf_da_compra TEXT,
    Nome_do_produto TEXT,
    Categoria_do_produto TEXT,
    Marca_do_produto TEXT,
    Quantidade_venda INTEGER,
    Valor_venda FLOAT,
    Preço_por_unidade FLOAT,
    primary key(Id)
    ) """
cur.execute(sql)

print("Tabela criada com sucesso!")

corn.commit()
corn.close()

