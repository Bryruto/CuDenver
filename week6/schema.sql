CREATE TABLE `users`(
    `id` INT UNSIGNED AUTO_INCREMENT,
    `frist_name` VARCHAR(16) NOT NULL,
    `last_name` VARCHAR(16) NOT NULL,
    `username` VARCHAR(16) NOT NULL,
    `password` VARCHAR(128) NOT NULL,
    PRIMARY KEY(`id`)
);

CREATE TABLE `schools` (
    `id` INT UNSIGNED AUTO_INCREMENT,
    `name` VARCHAR(30) NOT NULL,
    `type` ENUM('Primary','Secondary','Higher Education'),
    `location` VARCHAR(100) NOT NULL,
    `founded` YEAR NOT NULL,
    PRIMARY KEY(`id`)
);

CREATE TABLE `companies`(
    `id` INT UNSIGNED AUTO_INCREMENT,
    `name` VARCHAR(30) NOT NULL,
    `industry` ENUM('Technology','Education','Business'),
    `location` VARCHAR(100) NOT NULL,
    PRIMARY KEY(`id`)
);

CREATE TABLE `mutuals` (
    `user_id` INT UNSIGNED,
    `friend` INT UNSIGNED,
    FOREIGN KEY(`user_id`) REFERENCES `users`(`id`)
);

CREATE TABLE `school_affiliation`(
    `user_id`   INT UNSIGNED,
    `school_id` INT UNSIGNED,
    `start` DATETIME NOT NULL,
    `end` DATETIME,
    `degree` VARCHAR(30),
    FOREIGN KEY(`user_id`) REFERENCES `users`(`id`),
    FOREIGN KEY(`school_id`) REFERENCES `schools`(`id`)
);

CREATE TABLE `companies_affiliation`(
    `user_id` INT UNSIGNED,
    `company_id` INT UNSIGNED,
    `start` DATETIME NOT NULL,
    `end` DATETIME,
    FOREIGN KEY(`user_id`) REFERENCES `users`(`id`),
    FOREIGN KEY(`company_id`) REFERENCES `companies`(`id`)
);
