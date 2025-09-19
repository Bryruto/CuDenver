CREATE TABLE "users"(
    "id" INTEGER,
    "f_name" TEXT,
    "l_name" TEXT,
    "username" TEXT,
    "password" TEXT,
    PRIMARY KEY ("id")
);

CREATE TABLE "schools"(
    "id" INTEGER,
    "name" TEXT,
    "type" TEXT,
    "location" TEXT,
    "founded" NUMERIC,
    PRIMARY KEY ("id")
);

CREATE TABLE "companies"(
    "id" INTEGER,
    "name" TEXT,
    "industry" TEXT,
    "loocation" NUMERIC,
    PRIMARY KEY ("id")
);

CREATE TABLE "following"(
    "followed" INTEGER,
    "follower" INTEGER,
    FOREIGN KEY ("followed") REFERENCES "users"("id"),
    FOREIGN KEY ("follower") REFERENCES "users"("id")
);

CREATE TABLE "affliation"(
    "user_id" INTEGER,
    "school_id" INTEGER,
    "companie_id" INTEGER,
    "start" NUMERIC,
    "end" NUMERIC,
    "title" TEXT,
    FOREIGN KEY ("user_id") REFERENCES "users" ("id"),
    FOREIGN KEY ("school_id") REFERENCES "school" ("id"),
    FOREIGN KEY ("companie_id") REFERENCES "companies" ("id")
);
