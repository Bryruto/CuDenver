CREATE TABLE "passengers"(
    "id" INTEGER,
    "f_name" TEXT,
    "l_name" TEXT,
    "age" INTEGER CHECK("age" != 0),
    PRIMARY KEY ("id")
);

CREATE TABLE "check_in"(
    "id" INTEGER,
    "time_in" NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "flight_id" INTEGER,
    "passenger_id" INTEGER,
    FOREIGN KEY ("passenger_id") REFERENCES "passengers" ("id")
    FOREIGN KEY ("flight_id") REFERENCES "flights" ("id")
    PRIMARY KEY ("id")
);

CREATE TABLE "airlines"(
    "id" INTEGER,
    "name" TEXT,
    "concoures" TEXT NOT NULL CHECK("concoures" IN ('A','B','C','D','E','F','T')),
    "flight_id" INTEGER,
    FOREIGN KEY ("flight_id") REFERENCES "flights" ("id")
    PRIMARY KEY ("id")
);

CREATE TABLE "flights"(
    "id" INTEGER,
    "fight_number" INTEGER,
    "airline_id" INTEGER,
    "departing" TEXT,
    "heading" TEXT,
    "leave_time" NUMERIC,
    "arrival_time" NUMERIC,
    FOREIGN KEY ("airline_id") REFERENCES "airlines" ("id")
    PRIMARY KEY ("id")
);
