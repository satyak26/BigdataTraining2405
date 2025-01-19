/*Task 3:
create table table1 using these fields name (3), age(2), city(5), zipcode(5), phone(10),state_code(2), order_id(uuid()
create table table2 using these fields  state_code(2), County(6),order_date("yyyy-MM-dd hh:mm:ss"),
 phone(10), order_id(uuid()), name (3) using the uuid library.*/
-- Create two tables for the above two tables.
CREATE TABLE table1 (
    name VARCHAR(3),
    age CHAR(2), -- Age is now 2 characters (CHAR(2))
    city VARCHAR(5),
    zipcode VARCHAR(5),
    phone VARCHAR(10),
    state_code VARCHAR(2),
    order_id CHAR(36) DEFAULT (UUID()) -- UUID stored as CHAR(36)
);

SELECT UUID();

CREATE TABLE table2 (
    state_code VARCHAR(2),
    County VARCHAR(6),
    order_date DATETIME, -- Use DATETIME for "yyyy-MM-dd hh:mm:ss" format
    phone VARCHAR(10),
    order_id CHAR(36) DEFAULT (UUID()), -- UUID stored as CHAR(36)
    name VARCHAR(3)
);

select * from table1;
select * from table2;

create table oldtable1data as select * from table1;
create table oldtable2data as select * from table2;

select * from oldtable1data;
select * from oldtable2data;

SELECT (SELECT COUNT(*) FROM table1) AS table1_count,
       (SELECT COUNT(*) FROM table2) AS table2_count
FROM dual;

truncate table table1;
truncate table table2;

-- check condition Order_Date range should be from 2020-2024
SELECT *
FROM table2
WHERE order_date >= '2020-01-01' AND order_date <= '2024-12-31'
order by order_date desc;

SELECT count(*)
FROM table2
WHERE order_date >= '2020-01-01' AND order_date <= '2024-12-31'
order by order_date desc;

/*Task4: Join the two tables on State_code and name (3)  to create a single table with 
all the rows and also columns from both the tables. Name the table table3 */
drop table if exists table5;
CREATE TABLE table3 AS
SELECT  t1.*, t2.County, t2.order_date FROM table1 t1 JOIN table2 t2
ON t1.state_code = t2.state_code AND t1.name = t2.name;

drop table table3;

SELECT 
   count(*)
FROM table1 t1
JOIN table2 t2
ON t1.state_code = t2.state_code AND t1.name = t2.name;

select state_code, name,COUNT(*)  FROM table3
GROUP BY state_code, name
HAVING COUNT(*) > 1;

/*Task5: From table 3, write sql queries to do the following.
a) Create a table table5 with records from states TX, CA, AZ, NY, FL */
drop table if existsS table5;
CREATE TABLE table5 AS
SELECT *
FROM table3
WHERE state_code IN ('TX', 'CA', 'AZ', 'NY', 'FL');

SELECT count(*)
FROM table3
WHERE state_code IN ('TX', 'CA', 'AZ', 'NY', 'FL');

-- b) To find the State with most orders using order_id
SELECT 
    state_code, 
    COUNT(order_id) AS total_orders
FROM table3
GROUP BY state_code
ORDER BY total_orders DESC
LIMIT 1;

-- c) To find the State with most orders by Year using order_id 
SELECT 
    state_code, 
    YEAR(order_date) AS year,
    COUNT(order_id) AS total_orders
FROM table3
GROUP BY state_code, YEAR(order_date)
ORDER BY total_orders DESC;

-- d) To find the State with most orders by Year and also City using order_id 
SELECT 
    state_code,
    YEAR(order_date) AS year,
    city,
    COUNT(order_id) AS total_orders
FROM table3
GROUP BY state_code, YEAR(order_date), city
ORDER BY total_orders DESC;

-- e) To find the oldest person to have placed more than 10 orders.  If there are no results find the oldest person to have placed more than 3 orders.
SELECT 
    name, 
    MAX(age) AS oldest_age
FROM table3
GROUP BY name
HAVING COUNT(order_id) > 10
ORDER BY oldest_age DESC
LIMIT 1;

-- If no results for > 10 orders:
SELECT 
    name, 
    MAX(age) AS oldest_age
FROM table3
GROUP BY name
HAVING COUNT(order_id) > 3
ORDER BY oldest_age DESC
LIMIT 1;

-- f) Create a query to find the length of the order_id from table 3 and also split it into parts and display the length of each part. 
SELECT 
    order_id,
    LENGTH(order_id) AS order_id_length,
    LENGTH(SUBSTRING_INDEX(order_id, '-', 1)) AS part1_length,
    LENGTH(SUBSTRING_INDEX(SUBSTRING_INDEX(order_id, '-', 2), '-', -1)) AS part2_length,
    LENGTH(SUBSTRING_INDEX(SUBSTRING_INDEX(order_id, '-', 3), '-', -1)) AS part3_length,
    LENGTH(SUBSTRING_INDEX(SUBSTRING_INDEX(order_id, '-', 4), '-', -1)) AS part4_length,
    LENGTH(SUBSTRING_INDEX(SUBSTRING_INDEX(order_id, '-', 5), '-', -1)) AS part5_length
FROM table3;


