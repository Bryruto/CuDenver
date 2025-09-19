SELECT "first_name","last_name",SUM("salary") / SUM("H") AS 'dollars per hit' FROM "players"
JOIN
"salaries" ON "salaries"."player_id" = "players"."id"
JOIN
"performances" ON "salaries"."year" = "performances"."year" AND "performances"."player_id" = "salaries"."player_id"
WHERE "H" >= 1 AND "salaries"."year" = 2001
GROUP BY "last_name","first_name"
ORDER BY "dollars per hit" ASC,"first_name","last_name"
LIMIT 10;
