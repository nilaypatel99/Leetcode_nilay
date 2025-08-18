WITH start_time AS (
    SELECT machine_id, process_id, MIN(timestamp) AS start_time
    FROM Activity
    WHERE activity_type = 'start'
    GROUP BY machine_id, process_id
),
end_time AS (
    SELECT machine_id, process_id, MAX(timestamp) AS end_time
    FROM Activity
    WHERE activity_type = 'end'
    GROUP BY machine_id, process_id
),
processing AS (
    SELECT 
        s.machine_id,
        s.process_id,
        e.end_time - s.start_time AS processing_time
    FROM start_time s
    JOIN end_time e
      ON s.machine_id = e.machine_id
     AND s.process_id = e.process_id
)
SELECT 
    machine_id,
    ROUND(AVG(processing_time),3) AS processing_time
FROM processing
GROUP BY machine_id;
