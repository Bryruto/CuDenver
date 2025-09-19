CREATE VIEW june_vacancies AS SELECT "listings"."id","property_type","host_name",count("available") AS 'days_vacant'
FROM "listings"
JOIN "availabilities" ON "availabilities"."listing_id" = "listings"."id"
WHERE "available" = 'TRUE' AND "date" LIKE '2023-06%'
GROUP BY "listings"."id";




