select u.name,
    sum(t.amount) as balance
    
from Transactions t 
    left join users u
    on (u.account=t.account)

group by t.account
having balance>=10000
