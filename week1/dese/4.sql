


SELECT "city",COUNT("type") AS 'amount of schools'
FROM "schools"
WHERE "type" = 'Public School'
GROUP BY "city"
ORDER BY "amount of schools" DESC,"city" ASC
LIMIT 10;
