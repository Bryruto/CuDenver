-- Keep a log of any SQL queries you execute as you solve the mystery.

--took place on July 28, 2024
--took place on Humphrey Street.

CREATE TABLE crime_scene_reports (
    id INTEGER,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    street TEXT,
    description TEXT,
    PRIMARY KEY(id)
);
CREATE TABLE interviews (
    id INTEGER,
    name TEXT,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    transcript TEXT,
    PRIMARY KEY(id)
);
CREATE TABLE atm_transactions (
    id INTEGER,
    account_number INTEGER,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    atm_location TEXT,
    transaction_type TEXT,
    amount INTEGER,
    PRIMARY KEY(id)
);
CREATE TABLE bank_accounts (
    account_number INTEGER,
    person_id INTEGER,
    creation_year INTEGER,
    FOREIGN KEY(person_id) REFERENCES people(id)
);
CREATE TABLE airports (
    id INTEGER,
    abbreviation TEXT,
    full_name TEXT,
    city TEXT,
    PRIMARY KEY(id)
);
CREATE TABLE flights (
    id INTEGER,
    origin_airport_id INTEGER,
    destination_airport_id INTEGER,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    hour INTEGER,
    minute INTEGER,
    PRIMARY KEY(id),
    FOREIGN KEY(origin_airport_id) REFERENCES airports(id),
    FOREIGN KEY(destination_airport_id) REFERENCES airports(id)
);
CREATE TABLE passengers (
    flight_id INTEGER,
    passport_number INTEGER,
    seat TEXT,
    FOREIGN KEY(flight_id) REFERENCES flights(id)
);
CREATE TABLE phone_calls (
    id INTEGER,
    caller TEXT,
    receiver TEXT,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    duration INTEGER,
    PRIMARY KEY(id)
);
CREATE TABLE people (
    id INTEGER,
    name TEXT,
    phone_number TEXT,
    passport_number INTEGER,
    license_plate TEXT,
    PRIMARY KEY(id)
);
CREATE TABLE bakery_security_logs (
    id INTEGER,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    hour INTEGER,
    minute INTEGER,
    activity TEXT,
    license_plate TEXT,
    PRIMARY KEY(id)
);

airports              crime_scene_reports   people
atm_transactions      flights               phone_calls
bakery_security_logs  interviews
bank_accounts         passengers



SELECT street FROM crime_scene_reports WHERE day = 28 AND month = 7 AND year = 2024;-- check for address

SELECT * FROM crime_scene_reports WHERE street = 'Humphrey Street';-- see all crimes around that time


--10:15am at the Humphrey Street bakery
--Interviews were conducted today with three witnesses who were present at the time –
--each of their interview transcripts mentions the bakery.

--see what was in bakery and what i could get
SELECT * FROM bakery_security_logs WHERE year = 2024 AND month = 7 AND day = 28;

SELECT name ,transcript FROM interviews WHERE transcript LIKE '%bakery%';

-- maybe -- look at name on plate
5P2BI95
SELECT name FROM people WHERE license_plate = '5P2BI95' OR license_plate = '94KL13X'
OR license_plate = '4328GD8' OR license_plate = '6P58WS2' OR license_plate = 'G412CB7';
94KL13X
4328GD8
6P58WS2
G412CB7
maybe

--ATM on Leggett Street and saw the thief there withdrawing some money.
SELECT account_number FROM atm_transactions WHERE atm_location LIKE '%Leggett Street%'
AND year = 2024 AND day = 28 AND month = 7 AND transaction_type = 'withdraw';
| account_number |
+----------------+
| 28500762       |
| 28296815       |
| 76054385       |
| 49610011       |
| 16153065       |
| 25506511       |
| 81061156       |
| 26013199       |
+----------------+
-- look at name on numbers
SELECT name FROM people WHERE id =(
SELECT person_id FROM bank_accounts WHERE account_number =(
    SELECT account_number FROM atm_transactions WHERE atm_location LIKE '%Leggett Street%'
AND year = 2024 AND day = 28 AND month = 7 AND transaction_type = 'withdraw'
));

--earliest flight out of Fiftyville tomorrow 29th


-- phone to purchase the flight ticket  less than a minute
--Accomplice purchased flight tickets
SELECT * FROM phone_calls WHERE caller = '(389) 555-5198' OR receiver = '(389) 555-5198';



SELECT phone_number FROM people WHERE name LIKE 'Luca';--(389) 555-5198

+---------+
|  name   |--
Suspects
+---------+
| Vanessa |
| Barry   |
| Sofia   |
| Luca    |
| Bruce   |//////
+---------+


THEIF is LUCA
--(609) 555-5876
SELECT name FROM people WHERE phone_number = '(609) 555-5876'--Kathryn

-- find passport number
SELECT passport_number,name FROM people WHERE name = 'Kathryn' OR name = 'Luca';
+-----------------+---------+
| passport_number |  name   |
+-----------------+---------+
| 8496433585      | Luca    |
| 6121106406      | Kathryn |
+-----------------+---------+

-- get the plane
SELECT * FROM airports WHERE city = 'Fiftyville';--id 8

--look at flifghts

SELECT flight_id FROM passengers WHERE passport_number = 8496433585;
SELECT destination_airport_id FROM flights WHERE id IN (
    SELECT flight_id FROM passengers WHERE passport_number = 8496433585
);
+-----------+
| flight_id |
+-----------+
| 11        |
| 36        |
| 48        |
+-----------+
SELECT destination_airport_id FROM flights WHERE id IN (
    SELECT flight_id FROM passengers WHERE passport_number = 6121106406
);
SELECT flight_id FROM passengers WHERE passport_number = 6121106406;
+-----------+
| flight_id |
+-----------+
| 34        |
+-----------+
SELECT 11 36 48

SELECT "id" FROM flights WHERE "origin_airport_id" = (
    SELECT "id" FROM airports WHERE city = 'Fiftyville'
)AND day = 29 AND month = 7 AND year = 2024;

+----+
| id |
+----+
| 18 |
| 23 |
| 36 |
| 43 |
| 53 |
+----+

SELECT 5 12 4 8

--earliest flight out of Fiftyville tomorrow 29th

SELECT hour,minute,destination_airport_id FROM flights WHERE origin_airport_id = (
SELECT id FROM airports WHERE city = 'Fiftyville')AND month = 7 AND day =29 ORDER BY hour,minute;


SELECT city FROM airports WHERE id =8;
Delhi
Fiftyville
