# Write your MySQL query statement below
-- Write your PostgreSQL query statement below
SELECT id, movie, description, rating FROM Cinema 
WHERE id % 2 = 1 and description NOT LIKE '%boring'
ORDER BY rating DESC