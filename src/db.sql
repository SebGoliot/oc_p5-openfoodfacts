DROP DATABASE `openfoodfacts`;
CREATE DATABASE IF NOT EXISTS  `openfoodfacts`;
USE `openfoodfacts`;

-- Categories table
CREATE TABLE IF NOT EXISTS `Categories` (
	`id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(127) NOT NULL,
	PRIMARY KEY (`id`)
);

-- Products table
CREATE TABLE IF NOT EXISTS `Products` (
	`id` INT UNSIGNED NOT NULL AUTO_INCREMENT ,
	`name` VARCHAR(127) NOT NULL,
	`category` INT UNSIGNED NOT NULL,
	`nutriscore` CHAR(1) NOT NULL,
	`stores` VARCHAR(255) NOT NULL,
	PRIMARY KEY (`id`),
	FOREIGN KEY (`category`) REFERENCES `Categories`(`id`)
);

-- Favorites table
CREATE TABLE IF NOT EXISTS `Favorites` (
	`id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`product_id` INT UNSIGNED NOT NULL,
	`substitued_id` INT UNSIGNED NOT NULL,
	PRIMARY KEY (`id`),
    FOREIGN KEY (`product_id`) REFERENCES `Products`(`id`),
    FOREIGN KEY (`substitued_id`) REFERENCES `Products`(`id`)
);
