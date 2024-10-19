select user_id, page_id, count(1) as friends_likes
from
(
select if(user_id=user1_id, user2_id, user1_id) as user_id, page_id
from
(
select page_id ,user1_id,user2_id,user_id
from Likes join Friendship
on Likes.user_id=Friendship.user1_id or
Likes.user_id=Friendship.user2_id
group by page_id,user1_id,user2_id
having count(1)=1
) temp
) temp1
group by user_id, page_id
