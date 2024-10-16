select user_id,max(cnt) as max_7day_posts, count(*)/4 as avg_weekly_posts
from
(
select p1.user_id, p1.post_id,count( p2.post_id) as cnt
from Posts p1
join Posts p2
on p1.user_id=p2.user_id 
and p2.post_date between p1.post_date and date_add(p1.post_date,interval 6 day)
where p1.post_date between '2024-02-01' and '2024-02-28'
group by p1.user_id, p1.post_id
) temp
group by user_id
having count(*)<= 2*max(cnt)
order by user_id
