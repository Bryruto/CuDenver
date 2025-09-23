select "to_user_id" from "messages" where "from_user_id" IN (
    select "id" from "users" where "username" = 'creativewisdom377'
)group by "to_user_id" order by count("to_user_id") DESC limit 3;
