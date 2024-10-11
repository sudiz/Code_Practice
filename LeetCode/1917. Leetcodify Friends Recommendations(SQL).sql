select user1 as user_id, user2 as recommended_id
from
(
select distinct l1.user_id as user1, l2.user_id as user2
from Listens l1 
join Listens l2
on l1.day=l2.day and l1.song_id=l2.song_id and l1.user_id!=l2.user_id
group by l1.day, l1.user_id,l2.user_id
having count(distinct l1.song_id)>2
) temp left join Friendship
on (user1=user1_id and user2=user2_id) or (user1=user2_id and user2=user1_id)
where user1_id is null
order by user_id
