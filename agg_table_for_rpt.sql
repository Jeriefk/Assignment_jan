CREATE TABLE monthly_rpt AS
  SELECT Extract(year FROM creation_date)  yr,
         Extract(month FROM creation_date) mn,
         Count(order_id)                   total_orders,
         Sum(order_value)                  total_order_value
  FROM   orders
  GROUP  BY 1,
            2;

CREATE TABLE monthly_status_category_rpt AS
  SELECT Extract(year FROM creation_date)  yr,
         Extract(month FROM creation_date) mn,
         status,
         category,
         Count(order_id)                   total_orders,
         Sum(order_value)                  total_order_value
  FROM   orders a
         LEFT JOIN order_status b
                ON a.status_id = b.status_code
         LEFT JOIN category c
                ON a.category_id = c.id
  GROUP  BY 1,
            2,
            3,
            4; 
