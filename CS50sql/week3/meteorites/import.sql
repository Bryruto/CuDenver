-- 1. Start fresh
DROP TABLE IF EXISTS meteorites_temp;
DROP TABLE IF EXISTS meteorites;

-- 2. Create temp staging table
CREATE TABLE meteorites_temp (
  name TEXT,
  id INTEGER,
  nametype TEXT,
  class TEXT,
  mass REAL,
  discovery TEXT,
  year TEXT,
  lat REAL,
  long REAL
);

-- 3. Import CSV into staging table (skip header)
.import --csv --skip 1 meteorites.csv meteorites_temp

-- 4. Clean empty-string values by converting to NULL
UPDATE meteorites_temp
SET
  mass  = NULLIF(mass, ''),
  year  = NULLIF(year, ''),
  lat   = NULLIF(lat, ''),
  long  = NULLIF(long, '');

-- 5. Round numerical values to 2 decimals
UPDATE meteorites_temp
SET
  mass = ROUND(mass, 2),
  lat  = ROUND(lat, 2),
  long = ROUND(long, 2);

-- 6. Remove any entries of nametype = 'Relict'
DELETE FROM meteorites_temp
WHERE nametype = 'Relict';

-- 7. Create final cleaned table with proper schema
CREATE TABLE meteorites (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  class TEXT,
  mass REAL,
  discovery TEXT,
  year INTEGER,
  lat REAL,
  long REAL
);

-- 8. Populate final table, ordered by year and then name
INSERT INTO meteorites (name, class, mass, discovery, year, lat, long)
SELECT
  name,
  class,
  mass,
  discovery,
  CAST(year AS INTEGER),
  lat,
  long
FROM meteorites_temp
ORDER BY year ASC, name ASC;

-- 9. Drop the temporary table
DROP TABLE meteorites_temp;
