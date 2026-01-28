# Write your MySQL query statement below
WITH temp AS (
    SELECT *
    FROM Activity
    WHERE activity_type = 'end'
),
temp2 AS (
    SELECT *
    FROM Activity
    WHERE activity_type = 'start'
)
SELECT a.machine_id,ROUND(AVG(a.timestamp-t.timestamp),3) AS processing_time FROM temp a
JOIN temp2 t ON t.machine_id=a.machine_id
GROUP BY a.machine_id