select id
from
(
    select id, lag(temperature,1,100) over(order by recordDate asc) as tem, temperature
    from Weather
) temp 
where temperature> tem
