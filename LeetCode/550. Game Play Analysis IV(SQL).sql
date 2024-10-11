select round(count(distinct a1.player_id)/count(temp.player_id),2) as fraction
from
(
select player_id, min(event_date) as event_date
from Activity
group by player_id
) temp
left join Activity a1
on temp.player_id=a1.player_id
and datediff(a1.event_date,temp.event_date)=1
