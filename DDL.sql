CREATE TABLE order_status
  (
     status_code INT,
     status      VARCHAR(20)
  );


CREATE TABLE country
  (
     id      INT,
     country VARCHAR(20)
  );


CREATE TABLE category
  (
     id       INT,
     category VARCHAR(20)
  );


CREATE TABLE orders
  (
     order_id      VARCHAR(100),
     creation_date DATE,
     order_value   FLOAT,
     country_id    INT,
     status_id     INT,
     category_id   INT
  ); 
