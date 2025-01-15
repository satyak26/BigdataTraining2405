#Create two tables for the above two tables.
CREATE TABLE addresstable1 (
    name VARCHAR(100),
    age INT,
    city VARCHAR(50),
    zipcode INT,
    phone VARCHAR(15),
    state_code CHAR(2),
    order_id CHAR(36)
);

drop table  addresstable1;
truncate table addresstable1;
Select * from addresstable1;
Select * from addresstable2;

CREATE TABLE addresstable2 (
    state_code CHAR(2),
    County VARCHAR(100),
    order_date TIMESTAMP,
    phone VARCHAR(15),
    order_id CHAR(36),
    name VARCHAR(100)
);

drop table  addresstable2;

#Join the two tables on State_code and phone to create a single table with all the rows and also columns from both the tables. Name the table table3
CREATE TABLE Finaladdresstable AS
SELECT t1.name, t1.age, t1.city, t1.zipcode, t1.phone, t1.state_code,
    t2.County, t2.order_date, t2.order_id
FROM   addresstable1 t1 JOIN  addresstable2 t2
ON     t1.state_code = t2.state_code
AND      t1.phone = t2.phone;

#Create a table table5 with records from states TX, CA, AZ, NY, FL from  Finaladdresstable
CREATE TABLE statetable AS
SELECT *
FROM Finaladdresstable
WHERE state_code IN ('TX', 'CA', 'AZ', 'NY', 'FL');

#To find the State with most orders using order_id from Finaladdresstable
SELECT state_code, COUNT(order_id) AS order_count
FROM Finaladdresstable
GROUP BY state_code
ORDER BY order_count DESC
LIMIT 1;

#To find the State with most orders by Year using order_id from Finaladdresstable
SELECT YEAR(order_date) AS order_year, state_code, COUNT(order_id) AS order_count
FROM Finaladdresstable
GROUP BY order_year, state_code
ORDER BY order_count DESC
LIMIT 1;

#To find the State with most orders by Year and also City using order_id from Finaladdresstable
SELECT YEAR(order_date) AS order_year, state_code, city, COUNT(order_id) AS order_count
FROM Finaladdresstable
GROUP BY order_year, state_code, city
ORDER BY order_count DESC
LIMIT 1;

# To find the oldest person to have placed more than 10 orders.  If there are no results find the oldest person to have placed more than 3 orders.
SELECT t1.name, t1.age, COUNT(t2.order_id) AS order_count
FROM addresstable1 t1
JOIN addresstable2 t2 ON t1.phone = t2.phone
GROUP BY t1.name, t1.age
HAVING order_count > 10
ORDER BY t1.age DESC
LIMIT 1;

