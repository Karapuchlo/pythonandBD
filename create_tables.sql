CREATE TABLE employees
(
	first_name varchar(20),
	last_name varchar(20),
	title varchar(50),
	birth_date DATE,
	notes TEXT
);
CREATE TABLE customers
(
	customer_id	varchar(10) UNIQUE,
	company_name varchar(100),	
	contact_name varchar(100)
);
CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id	varchar(50),
	employee_id	int,
	order_date	DATE,
	ship_city varchar(50)
);
