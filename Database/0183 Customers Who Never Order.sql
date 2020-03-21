select Name Customers
from Customers
where Id not in (
    Select CustomerId
    from Orders
)
