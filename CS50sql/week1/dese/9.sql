
SELECT "name" FROM "expenditures"
JOIN
"districts" ON "expenditures"."district_id" = "districts"."id"
ORDER BY "pupils" ASC LIMIT 1;
