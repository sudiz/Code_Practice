select seller_id, num as num_items
from
(
select seller_id, dense_rank() over(order by num desc) as rnk, num
from
(
select Users.seller_id, count(distinct Orders.item_id) as num
from Users join Orders
on Users.seller_id=Orders.seller_id
join Items on Orders.item_id=Items.item_id
where item_brand!=favorite_brand
group by Users.seller_id
) temp
)temp1
where rnk=1
order by seller_id
