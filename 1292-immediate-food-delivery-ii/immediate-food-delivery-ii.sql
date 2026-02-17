# Write your MySQL query statement below
SELECT 
    ROUND(
        SUM(CASE 
                WHEN DATEDIFF(order_date, customer_pref_delivery_date) = 0 
                THEN 1 
                ELSE 0 
            END) 
        / COUNT(*) * 100
    , 2) AS immediate_percentage
FROM Delivery
WHERE (CUSTOMER_ID, ORDER_DATE) IN (
    SELECT
        CUSTOMER_ID,
        MIN(ORDER_DATE)
    FROM DELIVERY
    GROUP BY 1
);
