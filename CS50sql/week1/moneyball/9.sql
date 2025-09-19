SELECT "name",ROUND(AVG("salary"),2) AS 'average' FROM "teams"
JOIN
"salaries" ON "salaries"."team_id" = "teams"."id"
WHERE "salaries"."year"  = 2001
GROUP BY "name"
ORDER BY "average" ASC
LIMIT 5;
