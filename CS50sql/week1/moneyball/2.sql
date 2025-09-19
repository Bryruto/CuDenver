SELECT "year", "salary" FROM "salaries"
JOIN
"players" ON "players"."id" = "salaries"."player_id"
WHERE "first_name" = 'Cal' AND "last_name" LIKE '%ripken%'
ORDER BY "year" DESC;
