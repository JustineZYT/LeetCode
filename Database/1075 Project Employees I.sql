## Round to 2 digits
select project_id, round(avg(experience_years),2) average_years
from(
    select project_id, p.employee_id, experience_years
    from Project p
    left join Employee e
    on p.employee_id = e.employee_id
    ) a
group by project_id