CREATE TABLE "ingredients"(
    "id" INTEGER,
    "ingredient" TEXT,
    "size" TEXT,
    "cost" REAL,
    PRIMARY KEY ("id")
);

CREATE TABLE "donuts"(
    "id" INTEGER,
    "name" TEXT,
    "gluten_free" TEXT CHECK ("gluten_free" IN ('YES','NO')),
    "ingredient_id" INTEGER,
    FOREIGN KEY ("ingredient_id") REFERENCES "ingredients" ("id"),
    PRIMARY KEY ("id")
);

CREATE TABLE "orders"(
    "order_id" INTEGER,
    "donuts_ordered" INTEGER,
    "customer_id" INTEGER,
    FOREIGN KEY ("donuts_ordered") REFERENCES "donuts" ("id"),
    PRIMARY KEY ("order_id")
);

CREATE TABLE "customers"(
    "id" INTEGER,
    "f_name" TEXT,
    "l_name" TEXT,
    "history_id" INTEGER,
    "order_id" INTEGER,
    FOREIGN KEY ("order_id") REFERENCES "customers" ("order_id"),
    PRIMARY KEY ("id")
);

CREATE TABLE "history"(
    "order_id" INTEGER,
    "customer_id" INTEGER,
    FOREIGN KEY ("order_id") REFERENCES "customers" ("order_id"),
    FOREIGN KEY ("customer_id") REFERENCES "customers" ("id")
);

