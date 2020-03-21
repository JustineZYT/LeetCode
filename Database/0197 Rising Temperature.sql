select t1.Id Id
from Weather t1, Weather t2
where DATEDIFF(t1.RecordDate, t2.RecordDate) = 1
    and t1.Temperature > t2.Temperature