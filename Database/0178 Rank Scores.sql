Select S1.Score, count(distinct S2.Score) Rank
from Scores S1, Scores S2
where S1.Score <= S2.Score
group by S1.Id
order by S1.Score DESC