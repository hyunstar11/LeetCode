# Write your MySQL query statement below
Select name FROM Customer
WHERE IFNULL(referee_id, 0) != 2;