

SELECT "first_name", "last_name"
FROM "players"
    JOIN "salaries" ON "salaries"."player_id" = "players"."id"
   JOIN "performances" ON "salaries"."year" = "performances"."year" AND "performances"."player_id" = "salaries"."player_id"
    WHERE "performances"."year" = 2001 AND "performances"."player_id" IN (
        SELECT "performances"."player_id" FROM "performances"
        JOIN "salaries" ON "salaries"."year" = "performances"."year" AND "performances"."player_id" = "salaries"."player_id"
        WHERE "performances"."year" = 2001 AND "performances"."H" > 0
        ORDER BY "salaries"."salary" / "performances"."H"
        LIMIT 10
    ) AND "performances"."player_id" IN (
        SELECT "performances"."player_id" FROM "performances"
       JOIN "salaries" ON "salaries"."year" = "performances"."year" AND "performances"."player_id" = "salaries"."player_id"
        WHERE "performances"."year" = 2001 AND "performances"."RBI" > 0
       ORDER BY "salaries"."salary" / "performances"."RBI"
     LIMIT 10
   )
    ORDER BY "players"."id"LIMIT 10;



