# Write your MySQL query statement below
with temp AS (SELECT *,LAG(recordDate) OVER(ORDER by recordDate) AS prerecordDate,LAG(temperature) OVER ()AS pretemperature FROM Weather)

SELECT id FROM temp
WHERE temperature>pretemperature AND DATEDIFF(recordDate,prerecordDate)=1
