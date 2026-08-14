# Write your MySQL query statement below
SELECT visited_on, amount, round(amount/7,2) as average_amount from(
    select distinct visited_on,
sum(amount) over (
    order by visited_on
    RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW) 
as amount
from customer) as wt
where datediff (visited_on, (select min(visited_on) from customer)) >=6