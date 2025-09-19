SELECT "salary" FROM "salaries"
JOIN
"performances" ON "performances"."player_id" = "salaries"."player_id"
WHERE "Salaries"."year" =2001 AND "performances"."year" =2001
ORDER BY "HR" DESC
LIMIT 1;
