select Name
from Candidate c,
    (select CandidateId, count(id) Rank
    from Vote
    group by CandidateId
    order by Rank Desc
    limit 1) a
where c.id = a.CandidateId