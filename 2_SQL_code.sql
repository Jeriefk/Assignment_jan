WITH max_order AS
(
          SELECT    order_id,
                    country,
                    Sum(order_value) order_value
          FROM      orders a
          LEFT JOIN country d
          ON        a.country_id=d.id
          GROUP BY  1,
                    2 ), rwn AS
(
         SELECT   *,
                  Row_number() OVER(partition BY country ORDER BY order_value DESC) rn
         FROM     max_order)
SELECT    a.order_id,
          status,
          d.country,
          Date_part('day',CURRENT_DATE::timestamp-creation_date::timestamp)    number_of_days_between_order_and_today,
          string_agg(category,'|' order BY creation_date)                   AS category,
          sum(a.order_value)                                                   order_amount,
          max(rn)                                                              country_order_value_index
FROM      orders a
LEFT JOIN order_status b
ON        a.status_id=b.status_code
LEFT JOIN category c
ON        a.category_id=c.id
LEFT JOIN country d
ON        a.country_id=d.id
LEFT JOIN rwn e
ON        a.order_id=e.order_id
GROUP BY  1,
          2,
          3,
          4;
