select customer_id,consecutive_start,consecutive_end
from
(
select customer_id,transaction_date as consecutive_start, count(1) over(partition by customer_id order by transaction_date) as cnt, lead(transaction_date) over(partition by customer_id order by transaction_date) as consecutive_end
from
(
select customer_id,transaction_date,if(amount>famount1 and datediff(transaction_date,fday1)=1,1,0) as flag0, 
if(amount<bamount1 and datediff(bday1,transaction_date)=1,1,0) as flag1
from
(
select customer_id, transaction_date, amount,
lag(transaction_date,1) over(partition by customer_id order by transaction_date) as fday1,
lag(transaction_date,2) over(partition by customer_id order by transaction_date) as fday2,
lead(transaction_date,1) over(partition by customer_id order by transaction_date) as bday1,
lead(transaction_date,2) over(partition by customer_id order by transaction_date) as bday2,
lag(amount,1) over(partition by customer_id order by transaction_date) as famount1,
lag(amount,2) over(partition by customer_id order by transaction_date) as famount2,
lead(amount,1) over(partition by customer_id order by transaction_date) as bamount1,
lead(amount,2) over(partition by customer_id order by transaction_date) as bamount2
from Transactions
) temp1
where (amount>famount1 and famount1>famount2 and datediff(transaction_date,fday2)=2) or
(bamount1>amount and amount>famount1 and datediff(bday1,fday1)=2) or 
(bamount2>bamount1 and bamount1>amount and datediff(bday2,transaction_date)=2)
) temp2
where flag0=0 or flag1=0
) temp3
where cnt%2=1
order by customer_id
