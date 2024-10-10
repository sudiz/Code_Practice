# Write your MySQL query statement below
select id, company, salary
from
(
select id, company, salary, count(1) over(partition by company) as number, row_number() over(partition by company order by salary asc, id asc) as rnk
from Employee
) temp
where (number%2=0 and (rnk=number/2 or rnk=number/2+1))
or (number%2=1 and rnk=(number+1)/2)
order by company asc, salary asc, id desc
