with tem1 as 
(
  select customer_id,sum(amount) as total_amount, count(1) as transaction_count, count(distinct category) as unique_categories,
  round(sum(amount)/count(1),2) as avg_transaction_amount, round((count(1)*10+sum(amount)/100),2) as loyalty_score
  from Transactions
  join Products
  on Transactions.product_id=Products.product_id
  group by customer_id
), 
temp2 as
(
    select customer_id,category
    from
    (
    select customer_id,category,rank() over(partition by customer_id order by cnt desc, transaction_date desc) as rnk
    from
    (
    select customer_id,category,count(1) as cnt,max(transaction_date) as transaction_date
    from Transactions
    join Products
    on Transactions.product_id=Products.product_id
    group by customer_id,category
    ) a
    ) b
    where rnk=1
    
)
select tem1.customer_id,total_amount, transaction_count, unique_categories,avg_transaction_amount,category as top_category, loyalty_score
from tem1
join temp2
on tem1.customer_id=temp2.customer_id
order by loyalty_score desc,customer_id
