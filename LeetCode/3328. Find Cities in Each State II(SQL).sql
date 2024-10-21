select state, group_concat(city order by city separator ', ') cities, 
sum(if(left(city,1)=left(state,1),1,0)) as matching_letter_count # substring(city,1,1) or left(city,1)
from cities
group by state
having sum(if(left(city,1)=left(state,1),1,0))>0
and count(city)>2
order by matching_letter_count desc, state
