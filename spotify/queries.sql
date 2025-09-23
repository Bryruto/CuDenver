-- In this SQL file, write (and comment!) the typical SQL queries users will run on your database

-- find the most popular artist rn
CREATE VIEW "most_popular" AS
SELECT "song","artist" FROM "songs"
ORDER BY "popularity" DESC
LIMIT 10;

-- make a play list for indie
CREATE VIEW "indie" AS
SELECT "song","artist" FROM "songs"
WHERE "genre" LIKE '%indie%'
ORDER BY "popularity" DESC
LIMIT 30;

-- make a playlist for rock
CREATE VIEW "rock" AS
SELECT "song","artist" FROM "songs"
WHERE "genre" LIKE '%rock%'
ORDER BY "popularity" DESC
LIMIT 30;

-- make a playlist for pop
CREATE VIEW "pop" AS
SELECT "song","artist" FROM "songs"
WHERE "genre" LIKE '%pop%'
ORDER BY "popularity" DESC
LIMIT 30;

--fav artist artist with the most songs
CREATE VIEW "fav_artist" AS
SELECT COUNT("artist") as 'amount' ,"artist" FROM "songs"
GROUP BY "artist"
ORDER BY "amount" DESC
LIMIT 5;

--metal
CREATE VIEW "metal" AS
SELECT "song","artist" FROM "songs"
WHERE "genre" LIKE '%metal%'
ORDER BY "popularity" DESC
LIMIT 30;

-- maybe do not need
CREATE INDEX "name" ON "lookup"("name");
CREATE INDEX "genre" ON "lookup"("genre");
CREATE INDEX "artists" ON "lookup"("artists");
CREATE INDEX "find" ON "lookup"("artists","genre");
