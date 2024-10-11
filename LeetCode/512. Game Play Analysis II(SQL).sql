select player_id, device_id
from
(
select player_id, device_id, event_date, min(event_date) over(partition by player_id) as mn
from Activity
) temp
where event_date=mn
