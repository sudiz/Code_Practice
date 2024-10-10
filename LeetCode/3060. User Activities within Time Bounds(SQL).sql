select distinct user_id
from
(
select user_id, session_start, session_end, session_type, 
lag(session_end) over(partition by user_id,session_type order by session_start) as last_time, 
lag(session_type) over(partition by user_id,session_type order by session_start) as last_type
from Sessions
) temp
where timestampdiff(second,last_time, session_start)<=43200
order by user_id
