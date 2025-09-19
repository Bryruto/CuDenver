SELECT "first_name", "last_name","salary","HR" ,"performances"."year" AS 'year'
FROM "players"
JOIN "salaries" ON "players"."id" = "salaries"."player_id"
JOIN "performances" ON "performances"."year" = "salaries"."year" AND "performances"."player_id" = "salaries"."player_id"
ORDER BY "performances"."player_id" ASC, "year" DESC,"HR" DESC, "salary" DESC;
