## Create connection to the database
import psycopg2

# Altere as conexões para o seu banco de dados
params = {
    "host":"localhost",
    "database":"my_company",
    "user":"postgres",
    "port":5432,
    "password":"postgres"}
    

def run_queries(params, commands):
    """ Runs the given query"""
    conn = None
    
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # Run Queries one by one
        for command in commands:
            # checks for select queries then call fetchall() method
            if "select" in command.lower():
                print("Executing command: %s" % command)
                cur.execute(command)
                print("Returning result: %s" % cur.fetchall())
                print("--------------------------------")
            else:
                print("Executing command: %s" % command)
                cur.execute(command)
                print("--------------------------------") 

        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# Não alterar acima desta linhas
## --------------------------------------##
## Desafio

query_1 = """create database my_company;"""

# Crie uma nova query para cada tarefa

# Criar uma tabela Produto com as colunas (ID, Nome, Marca, Preço)
query_2 = """create table produtos (
	         id_produto int primary key,
	         nome varchar(50) not null,
	         marca varchar(50) not null,
	         preco float);"""

# Adicionar 10 produtos na tabela Produto
query_3 = """insert into produtos (id_produto, nome, marca, preco) values
             (1, 'Linha Cléa 1000 7030 mostarda', 'Círculo', 16.99),
             (2, 'Linha Cléa 1000 5800 pistache', 'Círculo', 15.90),
             (3, 'Fio Amigurumi 2829 azul bic', 'Círculo', 13.49),
             (4, 'Fio Amigurumi 7564 porcelana', 'Círculo', 13.49),
             (5, 'Barbante Barroco maxcolor 200g 6394 lavanda lilás', 'Círculo', 18.99),
             (6, 'Barbante Barroco premium 400g 9360 café', 'Círculo', 44.89),
             (7, 'Enrolador manual fios tricô e crochê', 'Clamak', 125.99),
             (8, 'Kit agulhas crochê bambu 12 unidades', 'Fazamak', 48.90),
             (9, 'Kit ferramentas amigurumi 51 peças', 'Lanmax', 45.99),
             (10, 'Revistas Ponto de Cruz 10 unidades', 'Editora Central', 49.90);"""

# Adicionar uma tabela Pedido Item que relacione Pedidos e Produtos através de chaves estrangeiras
query_4 = """create table pedidos (
	         id_pedido int primary key,
	         cliente varchar(50) not null);"""

query_5 = """create table pedido_item (
	         id_produto int,
	         id_pedido int,
	         quantidade int);"""

#Adicionar 5 pedidos com pelo menos 1 item em cada pedido.
query_6 = """insert into pedidos (id_pedido, cliente) values
             (1, 'Julian Lima Pereira'),
             (2, 'Tânia Dias Cavalcanti'),
             (3, 'Gabrielle Ferreira Sousa'),
             (4, 'Luiza Ferreira Melo'),
             (5, 'Renan Araujo Cavalcanti')"""

query_7 = """insert into pedido_item (id_produto, id_pedido, quantidade) values
             (1, 1, 3),
             (1, 8, 1),
             (1, 10, 1),
             (2, 2, 5),
             (2, 3, 4),
             (2, 4, 4),
             (3, 5, 3),
             (3, 6, 3),
             (3, 7, 1),
             (3, 10, 1),
             (4, 7, 1),
             (4, 8, 2),
             (4, 3, 2),
             (5, 3, 6),
             (5, 4, 6),
             (5, 10, 1);"""

# Criar um índice na tabela pedidos para a coluna ID
query_8 = """create index indice
             on pedidos (id_pedido)"""

# Adicione todas as queries na lista abaixo
queries = [query_2, query_3, query_4, query_5, query_6, query_7, query_8]

#----------------------------------------##
# Não alterar abaixo desta linha

if __name__ == '__main__':
    run_queries(params, queries)

