
-- *** The Lost Letter **
SELECT "from_address_id" FROM "packages" WHERE "from_address_id" = (
    SELECT "id" FROM "addresses" WHERE "address" = '900 Somerville Avenue'
);

SELECT * FROM "packages"
FULL JOIN
"addresses" ON "addresses"."id"= "packages"."to_address_id" WHERE "from_address_id" = (
    SELECT "id" FROM "addresses" WHERE "address" = '900 Somerville Avenue'
);
-- *** The Devious Delivery ***
--Fiftyville.
--no “From” address.


SELECT "contents" FROM "packages" WHERE "from_address_id" IS NULL;


-- *** The Forgotten Gift ***
--to address 728 Maple Place.
--from 109 Tileston Street.
-- scans --packages --drivers

-- find what is inside the box
SELECT "contents" FROM "packages" WHERE "from_address_id" =(SELECT "id" FROM "addresses" WHERE "address" = '109 Tileston Street');
-- get the name of the driver that has the package

SELECT * FROM "addresses" WHERE "address" = '109 Tileston Street'--9873

SELECT * FROM "packages" WHERE "from_address_id" = 9873;-- packageid 9523

SELECT * FROM scans WHERE package_id = 9523 ORDER BY "timestamp" DESC LIMIT 1;--17

SELECT * FROM drivers WHERE id = 17;

SELECT "name" FROM "drivers" WHERE "id" = (
    SELECT "driver_id" FROM "scans" WHERE "package_id" = (
        SELECT "id" FROM "packages" WHERE "from_address_id" = (
            SELECT "id" FROM "addresses" WHERE "address" = '109 Tileston Street'
        )
    )
);
