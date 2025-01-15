WITH cte AS (SELECT student_id,subject,MIN(exam_date) AS fd,MAX(exam_date) AS ld
FROM Scores
GROUP BY student_id, subject
HAVING COUNT(DISTINCT exam_date) > 1)
    -- ^ ensures the student took that subject on at least two different dates

SELECT c.student_id,
    c.subject,
    s_first.score AS first_score,
    s_last.score  AS latest_score
FROM cte c
JOIN Scores s_first
  ON s_first.student_id = c.student_id
 AND s_first.subject    = c.subject
 AND s_first.exam_date  = c.fd
JOIN Scores s_last
  ON s_last.student_id = c.student_id
 AND s_last.subject    = c.subject
 AND s_last.exam_date  = c.ld
WHERE s_last.score > s_first.score
ORDER BY c.student_id, c.subject;
