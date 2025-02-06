# projeto-sql-e-python-
# Projeto de Integração SQL e Python para Análise de Vendas no Varejo

## Introdução

Bem-vindo ao projeto de criação e manipulação de um banco de dados SQLite com Python, desenvolvido para analisar dados de vendas no setor varejista. Este repositório demonstra uma abordagem eficiente e robusta para armazenar, consultar e manipular dados de vendas, permitindo insights valiosos para a tomada de decisão.

A proposta deste projeto é mostrar desde a criação da estrutura de banco de dados até consultas complexas e visualizações, usando bibliotecas como `sqlite3` e `pandas`.

---

## Estrutura do Projeto

### **Parte 1: Criação da Tabela Vendas_varrejo1**

![banco1](https://github.com/user-attachments/assets/d730a8bb-a36e-4985-b1fe-c3786ca1c0ef)

Nesta etapa, uma tabela é criada para armazenar dados estruturados sobre vendas no varejo. Os campos abrangem informações essenciais, como id da venda, data, nome da loja, unidade federativa, tipo e marca do produto, quantidade e valores.

---

### **Parte 2: Inserção de Dados no Banco**

![banco2](https://github.com/user-attachments/assets/fcba4cc7-6b3d-40c2-874f-e37e35b265b7)



Aqui, os dados contidos no arquivo CSV `vendas_varrejo1.csv` são inseridos na tabela criada anteriormente. O script realiza uma conversão adequada dos tipos de dados e ignora o cabeçalho do arquivo.

---

### **Parte 3: Consulta de Dados**

![banco3](https://github.com/user-attachments/assets/da9a5015-f4ee-4722-b7ae-46b6cd1106a3)

Nesta parte, mostramos como consultar e filtrar dados da tabela. No exemplo, recuperamos apenas as vendas realizadas no estado de São Paulo.

---

### **Parte 4: Análise com Pandas**

![banco4](https://github.com/user-attachments/assets/55421412-1019-4e88-99b7-475523ae1d13)


Nesta etapa, utilizamos o Pandas para executar consultas SQL e trazer insights significativos. Aqui, somamos o valor total de vendas por unidade federativa.

---

### **Parte 5: Listagem de Tabelas no Banco**

![banco5](https://github.com/user-attachments/assets/1da51024-4603-4479-ba2c-d9f3c149c8d6)



Esta parte permite listar todas as tabelas presentes no banco de dados SQLite, facilitando a inspeção e verificação da estrutura do banco.

---

## Conclusão

Este projeto mostra como integrar Python e SQLite para manipular dados de forma eficaz, desde a criação de tabelas até análises mais complexas com Pandas. Com essas ferramentas, é possível construir soluções poderosas para a tomada de decisão baseada em dados.

