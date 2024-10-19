select round(avg(cnt)*100,2) average_daily_percent
from
(
select action_date, count(distinct Removals.post_id)/count(distinct Actions.post_id) as cnt
from Actions left join Removals
on Actions.post_id=Removals.post_id
where extra='spam'
group by action_date
) temp
