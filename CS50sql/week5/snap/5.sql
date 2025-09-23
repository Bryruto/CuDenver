select "friend_id" from "friends" where "friend_id" IN (
    select "friend_id" from "friends" where "user_id" =(
        select "id" from "users" where "username" = 'lovelytrust487'
)
) and "friend_id" IN (
    select "friend_id" from "friends" where "user_id" =(
        select "id" from "users" where "username" = 'exceptionalinspiration482'
)
)group by "friend_id";
