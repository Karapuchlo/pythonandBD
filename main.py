import psycopg2

# подключение к БД
conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="240615Nastya"
)

# создание курсора
cur = conn.cursor()

# заполнение таблицы из north_data
'''
with open("orders_data.csv", "r") as f:
    next(f)
    for line in f:
        data = line.strip().split(",")
        cur.execute("INSERT INTO orders (order_id, customer_id,	employee_id, order_date, ship_city) VALUES (%s, %s, %s, %s, %s)", (int(data[0]), str(data[1]), data[2], data[3], data[4]))
'''
with open("employees_data.csv", "r") as f1:
    next(f1)
    for line in f1:
        data = line.strip().split(",")
        cur.execute("INSERT INTO employees (first_name, last_name,	title,	birth_date,	notes) VALUES (%s, %s, %s, %s, %s)", (data[0], data[1], data[2], data[3], data[4]))

with open("orders_data.csv", "r") as f2:
    next(f2)
    for line in f2:
        data = line.strip().split(",")
        cur.execute("INSERT INTO customers (customer_id, company_name,	contact_name) VALUES (%s, %s, %s)", (data[0], data[1], data[2]))


# сохранение изменений и закрытие соединения
conn.commit()
cur.close()
conn.close()