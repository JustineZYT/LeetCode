## Delete query from a table
Delete t1 
FROM Person AS t1, Person AS t2
Where t1.Email=t2.Email and t1.Id > t2.Id