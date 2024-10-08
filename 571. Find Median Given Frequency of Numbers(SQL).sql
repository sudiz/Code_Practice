select avg(num) as median
from
(
select num, frequency, sum(frequency) over() as total, (sum(frequency) over(order by num asc)) as cont
from Numbers
) temp
where ((cont-frequency)<=total/2) and (cont>=total/2)
