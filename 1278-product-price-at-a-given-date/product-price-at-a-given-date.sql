# Write your MySQL query statement below
WITH temp_prices AS (SELECT product_id,new_price,change_date,
                     ROW_NUMBER() OVER(PARTITION BY product_id ORDER BY change_date DESC) AS rn
FROM Products WHERE change_date<='2019-08-16')

SELECT p.product_id,COALESCE(tp.new_price,10) AS price FROM (SELECT DISTINCT product_id FROM products) p
LEFT JOIN temp_prices tp ON p.product_id=tp.product_id AND rn=1