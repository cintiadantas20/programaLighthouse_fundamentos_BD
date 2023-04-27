import psycopg2

# Altere as conexões para o seu banco de dados

params = {
    "host":"localhost",
    "database":"northwind",
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
            print("Executing command: %s" % command)
            cur.execute(command)
            print("Returning result: %s" % cur.fetchall())
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

## Qual foi o melhor mês de vendas da Northwind?
# Considerando ser o mês com maior número de vendas, de todos os anos
query_1 = """select 
                date_trunc('month', order_date) as month, 
                count(order_id) as contagem 
            from orders 
            group by month
            order by contagem desc
            limit 1;"""

# Considerando o mês com maior faturamento, de todos os anos
query_2 = """select 
                date_trunc('month', order_date) as month, 
                sum(quantity * unit_price*(1-discount)) as total 
            from order_details as d 
            inner join orders as o 
            on d.order_id = o.order_id 
            group by month 
            order by total desc
            limit (1);"""

## Qual o total de vendas dos 5 maiores clientes do Brasil?
query_3 = """select sum (total)
            from (
                select 
                    c.company_name, 
                    c.customer_id, 
                    o.ship_country, 
                    sum(quantity * unit_price*(1-discount)) as total 
                from customers as c 
                inner join orders as o
                on c.customer_id = o.customer_id 
                inner join order_details as d
                on d.order_id = o.order_id 
                where ship_country = 'Brazil' 
                group by 
                    company_name, 
                    c.customer_id, 
                    ship_country 
                order by total desc 
                limit (5))
            as cinco_maiores;"""

## Qual supplier com mais vendas para o Brasil?
# Considerando como mais vendas a quantidade total de vendas
query_4 = """select 
                s.company_name, 
                s.supplier_id, 
                o.ship_country, 
                count (o.order_id) as contagem 
            from suppliers as s 
            inner join products as p 
            on s.supplier_id = p.supplier_id 
            inner join order_details as d 
            on d.product_id = p.product_id 
            inner join orders as o 
            on d.order_id = o.order_id 
            where ship_country = 'Brazil' 
            group by 
                company_name, 
                s.supplier_id, 
                ship_country 
            order by contagem 
            desc limit (1);"""

# Considerando como mais vendas o valor total do faturamento
query_5 = """select 
                s.company_name, 
                s.supplier_id, 
                o.ship_country, 
                sum(d.quantity * d.unit_price*(1-d.discount)) as total 
            from suppliers as s 
            inner join products as p 
            on s.supplier_id = p.supplier_id 
            inner join order_details as d 
            on d.product_id = p.product_id 
            inner join orders as o 
            on d.order_id = o.order_id 
            where ship_country = 'Brazil' 
            group by 
                company_name, 
                s.supplier_id, 
                ship_country 
            order by total desc 
            limit (1);"""

## Qual vendedor (employee) realizou mais vendas para clientes com customer.postal_code do Brasil?
# Considerando mais vendas como maior número de vendas
query_6 = """select
                e.employee_id, 
                e.first_name, 
                e.last_name, 
                count (o.order_id) as contagem  
            from employees as e 
            inner join orders as o 
            on e.employee_id = o.employee_id 
            inner join order_details as d 
            on o.order_id = d.order_id 
            inner join customers as c 
            on c.customer_id = o.customer_id 
            where c.postal_code like '_____-___' 
            group by e.employee_id 
            order by contagem desc
            limit (1);"""

# Considerando mais vendas como maior faturamento
query_7 = """select
                e.employee_id, 
                e.first_name, 
                e.last_name, 
                sum(d.quantity * d.unit_price*(1-d.discount)) as total 
            from employees as e 
            inner join orders as o 
            on e.employee_id = o.employee_id 
            inner join order_details as d 
            on o.order_id = d.order_id 
            inner join customers as c 
            on c.customer_id = o.customer_id 
            where c.postal_code like '_____-___' 
            group by e.employee_id 
            order by total desc
            limit (1);"""

## Qual employee que mais gerou resultados para a Northwind? 
# em número de pedidos
query_8 = """select
                e.employee_id, 
                e.first_name, 
                e.last_name, 
                count (o.order_id) as contagem 
            from employees as e 
            inner join orders as o 
            on e.employee_id = o.employee_id 
            inner join order_details as d 
            on o.order_id = d.order_id 
            inner join customers as c 
            on c.customer_id = o.customer_id 
            group by e.employee_id 
            order by contagem desc
            limit (1);"""

# em total de itens vendidos
query_9 = """select
                e.employee_id, 
                e.first_name, 
                e.last_name, 
                sum (d.quantity) as contagem  
            from employees as e 
            inner join orders as o 
            on e.employee_id = o.employee_id 
            inner join order_details as d 
            on o.order_id = d.order_id 
            inner join customers as c 
            on c.customer_id = o.customer_id 
            group by e.employee_id 
            order by contagem desc
            limit (1);"""

# em valor total dos pedidos
query_10 = """select
                e.employee_id, 
                e.first_name, 
                e.last_name, 
                sum (d.quantity * d.unit_price*(1-d.discount)) as total   
            from employees as e 
            inner join orders as o 
            on e.employee_id = o.employee_id 
            inner join order_details as d 
            on o.order_id = d.order_id 
            inner join customers as c 
            on c.customer_id = o.customer_id 
            group by e.employee_id 
            order by total desc
            limit (1);"""

# Adicione todas as queries na lista abaixo
queries = [query_1, query_2, query_3, query_4, query_5, query_6, query_7, query_8, query_9, query_10]

#----------------------------------------##
# Não alterar abaixo desta linha

if __name__ == '__main__':
    run_queries(params, queries)
