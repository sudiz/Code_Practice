select name, ifnull(sum(rest),0) rest, ifnull(sum(paid),0) paid, ifnull(sum(canceled),0) canceled, 
ifnull(sum(refunded),0) refunded
from Product  
left join Invoice
on Product.product_id=Invoice.product_id
group by name
order by name
