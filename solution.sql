select distinct
   a.*
from events a  join events b  join events c
where
   a.people_count >= 100
   and b.people_count >= 100
   and c.people_count >= 100
   and
   ( (a.id + 1 = b.id
      and b.id + 1 = c.id)
      or
      (b.id + 1 = a.id
         and a.id + 1 = c.id)
      or 
      (b.id + 1 = c.id
         and c.id + 1 = a.id)
   )
order by
   id;