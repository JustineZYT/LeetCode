select distinct Email
from Person
group by Email
having count(ID)>1