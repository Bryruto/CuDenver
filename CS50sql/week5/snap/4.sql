select "username" from "users" where "id" = (
    select "to_user_id" from "messages" group by "to_user_id" order by count("to_user_id") DESC limit 1
    );
