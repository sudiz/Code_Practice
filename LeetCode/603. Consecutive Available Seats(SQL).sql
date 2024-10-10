select seat_id
from
(
select seat_id, free,lead(free)over(order by seat_id asc) as back, lag(free)over(order by seat_id asc) as forw
from Cinema
) temp
where free=1 and(back=1 or forw=1)
order by seat_id asc
