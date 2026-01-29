# Write your MySQL query statement below
SELECT e.name FROM Employee e 
JOIN Employee e2 ON e.id=e2.managerId 
GROUP BY e2.managerId HAVING COUNT(e2.managerId)>=5

