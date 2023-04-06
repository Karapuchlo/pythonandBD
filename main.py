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
with open("orders_data.csv", "r") as f:
    for line in f:
        data = line.strip().split(",")
        cur.execute("INSERT INTO orders (order_id, customer_id,	employee_id, order_date, ship_city) VALUES (%s, %s, %s, %s, %s)", (data[0], data[1], data[2], data[3], data[4]))

# сохранение изменений и закрытие соединения
conn.commit()
cur.close()
conn.close()