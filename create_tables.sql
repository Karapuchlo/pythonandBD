CREATE TABLE employees
(
	first_name varchar(20),
	last_name varchar(20),
	title varchar(50),
	birth_date DATE,
	notes TEXT
)
CREATE TABLE customer
(
	customer_id	varchar(10) UNIQUE,
	company_name varchar(100),	
	contact_name varchar(100)
)
CREATE TABLE orders
(
	order_id int PRYMARY_KEY,
	customer_id	int,
	employee_id	int,
	order_date	DATE,
	ship_city varchar(50)
)