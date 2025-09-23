-- In this SQL file, write (and comment!) the schema of your database, including the CREATE TABLE, CREATE INDEX, CREATE VIEW, etc. statements that compose it
sqlite3 spot.db

CREATE TABLE "songs"(
    "id" INTEGER,
    "song" TEXT,
    "popularity" INT,
    "artist" TEXT,
    "genre" TEXT,
    PRIMARY KEY("id")
);


