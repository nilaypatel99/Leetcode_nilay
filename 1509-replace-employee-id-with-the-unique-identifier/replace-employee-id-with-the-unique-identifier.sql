# Write your MySQL query statement below
SELECT unique_id,name FROM Employees e
LEFT JOIN EmployeeUNI e1 ON e.id=e1.id