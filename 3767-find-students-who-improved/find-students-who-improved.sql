# Write your MySQL query statement below
WITH temp AS (SELECT DISTINCT student_id,subject,
       FIRST_VALUE(score) OVER(PARTITION BY student_id,subject ORDER BY exam_date) AS first_score,
       LAST_VALUE(score) OVER(PARTITION BY student_id,subject ORDER BY exam_date ROWS 
       BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS latest_score,
       COUNT(exam_date) OVER(PARTITION BY student_id,subject) AS cnt
       FROM Scores)

SELECT student_id,subject,first_score,latest_score
FROM temp WHERE latest_score>first_score
AND cnt>1
