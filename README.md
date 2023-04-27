# programaLighthouse_fundamentos_cloud
Desafio referente ao Módulo IV - Fundamentos de cloud do programa Lighthouse, trilha Data Science

Para rodar esta aplicação, é necessário:
* Criar um ambiente virtual;
* Clonar este repositório;
* Criar uma instância de PostgreSQL utilizando docker ou algum serviço de nuvem;
* Conectar-se a um banco de dados, pelo comando psql ou usando DBeaver ou programa semelhante

Para as tarefas da 1ª parte do desafio:
* Rodar o código desafio_db.py

Para as tarefas da 2ª parte do desafio:
* Rodar o script northwind.sql
* Rodar o código desafio_northwind.py

As perguntas desse desafio são as seguintes:
1ª parte:
-  Criar uma tabela Produto com as colunas (ID, Nome, Marca, Preço)
-  Adicionar 10 produtos na tabela Produto
- Adicionar uma tabela Pedido Item que relacione Pedidos e Produtos através de chaves estrangeiras
- Adicionar 5 pedidos com pelo menos 1 item em cada pedido.
- Criar um índice na tabela pedidos para a coluna ID

2ª parte:
- Qual foi o melhor mês de vendas da Northwind?
- Qual o total de vendas dos 5 maiores clientes do Brasil?
- Qual supplier com mais vendas para o Brasil?
- Qual vendedor (employee) realizou mais vendas para clientes com customer.postal_code do Brasil?
- Qual employee que mais gerou resultados para a Northwind? 
    - em número de pedidos
    - em total de itens vendidos
    - em valor total dos pedidos