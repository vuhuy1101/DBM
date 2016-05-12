-- phpMyAdmin SQL Dump
-- version 4.5.0.2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 09, 2016 at 07:54 PM
-- Server version: 10.0.17-MariaDB
-- PHP Version: 5.6.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Grocery`
--
CREATE DATABASE IF NOT EXISTS `GroceryDB` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
USE `GroceryDB`;

-- --------------------------------------------------------

--
-- Table structure for table `Product`
--

DROP TABLE IF EXISTS `Product`;
CREATE TABLE IF NOT EXISTS `Product` (
  `product_key` int(11) NOT NULL,
  `description` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `brand` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `subcategory` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `category` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `department` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`product_key`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `Product`
--

INSERT INTO `Product` (`product_key`, `description`, `brand`, `subcategory`, `category`, `department`) VALUES
(1, 'Lasagna', 'Cold Gourmet', 'Frozen Foods', 'Food', 'Grocery'),
(2, 'Beef Stew', 'Cold Gourmet', 'Frozen Foods', 'Food', 'Grocery'),
(3, 'Turkey Dinner', 'Frozen Bird', 'Frozen Foods', 'Food', 'Grocery'),
(4, 'Chicken Dinner', 'Frozen Bird', 'Frozen Foods', 'Food', 'Grocery'),
(5, 'Extra Nougat', 'Chewy Industries', 'Candy', 'Food', 'Grocery'),
(6, 'Lots of Nuts', 'Chewy Industries', 'Candy', 'Food', 'Grocery'),
(7, 'Sweet Tooth', 'Chewy Industries', 'Candy', 'Food', 'Grocery'),
(8, 'Fizzy Light', 'Big Can', 'Soft Drinks', 'Drinks', 'Grocery'),
(9, 'Fizzy Classic', 'Big Can', 'Soft Drinks', 'Drinks', 'Grocery'),
(10, 'Athletic Drink', 'Big Can', 'Soft Drinks', 'Drinks', 'Grocery'),
(11, 'Strong Cola', 'National Bottle', 'Soft Drinks', 'Drinks', 'Grocery'),
(12, 'Clear Refresher', 'National Bottle', 'Soft Drinks', 'Drinks', 'Grocery'),
(13, 'Paper Towels', 'Squeezable Inc', 'Cleaning Supplies', 'Supplies', 'Household'),
(14, 'Dry Tissues', 'Squeezable Inc', 'Cleaning Supplies', 'Supplies', 'Household'),
(15, 'Wet Wipes', 'Squeezable Inc', 'Cleaning Supplies', 'Supplies', 'Household'),
(16, 'Salty Corn', 'American Corn', 'Salty Snacks', 'Food', 'Grocery'),
(17, 'Dried Grits', 'American Corn', 'Salty Snacks', 'Food', 'Grocery'),
(18, 'Power Chips', 'American Corn', 'Salty Snacks', 'Food', 'Grocery'),
(19, 'Onion Slices', 'Western Vegetable', 'Salty Snacks', 'Food', 'Grocery'),
(20, 'Buffalo Jerky', 'Western Vegetable', 'Salty Snacks', 'Food', 'Grocery'),
(21, 'Lasagna', 'Cold Gourmet', 'Frozen Foods', 'Food', 'Grocery'),
(22, 'Beef Stew', 'Cold Gourmet', 'Frozen Foods', 'Food', 'Grocery'),
(23, 'Turkey Dinner', 'Frozen Bird', 'Frozen Foods', 'Food', 'Grocery'),
(24, 'Chicken Dinner', 'Frozen Bird', 'Frozen Foods', 'Food', 'Grocery'),
(25, 'Extra Nougat', 'Chewy Industries', 'Candy', 'Food', 'Grocery'),
(26, 'Lots of Nuts', 'Chewy Industries', 'Candy', 'Food', 'Grocery'),
(27, 'Sweet Tooth', 'Chewy Industries', 'Candy', 'Food', 'Grocery'),
(28, 'Fizzy Light', 'Big Can', 'Soft Drinks', 'Drinks', 'Grocery'),
(29, 'Fizzy Classic', 'Big Can', 'Soft Drinks', 'Drinks', 'Grocery'),
(30, 'Athletic Drink', 'Big Can', 'Soft Drinks', 'Drinks', 'Grocery');

-- --------------------------------------------------------

--
-- Table structure for table `Promotion`
--

DROP TABLE IF EXISTS `Promotion`;
CREATE TABLE IF NOT EXISTS `Promotion` (
  `promotion_key` int(11) NOT NULL,
  `promotion_name` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `promo_cost` double NOT NULL,
  `promo_begin_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `promo_end_date` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`promotion_key`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `Promotion`
--

INSERT INTO `Promotion` (`promotion_key`, `promotion_name`, `promo_cost`, `promo_begin_date`, `promo_end_date`) VALUES
(1, 'Blue Ribbon Discounts', 2000, '1994-10-01 07:00:00', '1994-10-15 07:00:00'),
(2, 'Red Carpet Closeout', 1000, '1995-10-01 07:00:00', '1995-10-15 07:00:00'),
(3, 'Ad Blitz', 7000, '1994-11-10 08:00:00', '1994-11-17 08:00:00'),
(4, 'Ads and Racks', 3000, '1995-11-11 08:00:00', '1995-11-18 08:00:00'),
(5, 'Shelf Talkers', 500, '1994-10-01 07:00:00', '1994-12-31 08:00:00'),
(6, 'POS Grabbers', 600, '1995-10-01 07:00:00', '1995-12-31 08:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `Sales_Fact`
--

DROP TABLE IF EXISTS `Sales_Fact`;
CREATE TABLE IF NOT EXISTS `Sales_Fact` (
  `time_key` int(11) NOT NULL,
  `product_key` int(11) NOT NULL,
  `promotion_key` int(11) NOT NULL,
  `store_key` int(11) NOT NULL,
  `dollar_sales` double NOT NULL,
  `unit_sales` int(11) NOT NULL,
  `customer_count` int(11) NOT NULL,
  PRIMARY KEY (`store_key`,`promotion_key`,`product_key`,`time_key`),
  KEY `fk_Sales_Fact_Product1_idx` (`product_key`),
  KEY `fk_Sales_Fact_Time1_idx` (`time_key`),
  KEY `fk_Sales_Fact_Promotion1_idx` (`promotion_key`),
  KEY `fk_Sales_Fact_Store_idx` (`store_key`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `Sales_Fact`
--

INSERT INTO `Sales_Fact` (`time_key`, `product_key`, `promotion_key`, `store_key`, `dollar_sales`, `unit_sales`, `customer_count`) VALUES
(3, 1, 1, 1, 116.63, 86, 59),
(7, 2, 1, 1, 56.24, 42, 34),
(6, 4, 1, 1, 132.72, 98, 52),
(6, 21, 1, 1, 3.47, 2, 2),
(10, 23, 1, 1, 170.96, 84, 49),
(42, 6, 3, 1, 34.21, 70, 43),
(43, 6, 3, 1, 45.54, 93, 75),
(45, 6, 3, 1, 0.16, 0, 0),
(41, 26, 3, 1, 43.45, 59, 46),
(46, 27, 3, 1, 71.6, 97, 89),
(12, 13, 5, 1, 21.87, 22, 12),
(29, 13, 5, 1, 92.67, 94, 82),
(40, 13, 5, 1, 37.57, 38, 30),
(58, 13, 5, 1, 75.76, 77, 71),
(61, 13, 5, 1, 77.35, 78, 66),
(75, 13, 5, 1, 48.64, 49, 40),
(11, 14, 5, 1, 48.72, 49, 36),
(26, 14, 5, 1, 36.43, 37, 33),
(28, 14, 5, 1, 31.53, 32, 16),
(42, 14, 5, 1, 24.13, 24, 15),
(70, 14, 5, 1, 35.12, 35, 28),
(74, 14, 5, 1, 26.76, 27, 14),
(83, 14, 5, 1, 86.33, 87, 44),
(19, 15, 5, 1, 63.55, 64, 46),
(65, 15, 5, 1, 20.34, 21, 16),
(66, 15, 5, 1, 89.75, 91, 89),
(73, 15, 5, 1, 42.25, 43, 24),
(77, 15, 5, 1, 82.75, 84, 79),
(79, 15, 5, 1, 63.2, 64, 58),
(92, 15, 5, 1, 67.75, 68, 54),
(9, 2, 1, 2, 95.99, 71, 64),
(5, 22, 1, 2, 56.11, 28, 27),
(6, 23, 1, 2, 1.36, 1, 0),
(4, 24, 1, 2, 98.45, 49, 27),
(43, 5, 3, 2, 30.03, 61, 37),
(42, 7, 3, 2, 39.32, 80, 62),
(46, 7, 3, 2, 8.15, 17, 11),
(42, 27, 3, 2, 11.08, 15, 12),
(31, 13, 5, 2, 35.02, 35, 31),
(37, 13, 5, 2, 46.65, 47, 31),
(82, 13, 5, 2, 50.48, 51, 42),
(1, 14, 5, 2, 77.7, 78, 69),
(7, 14, 5, 2, 39.59, 40, 20),
(31, 14, 5, 2, 66.33, 67, 41),
(47, 14, 5, 2, 97.2, 98, 64),
(58, 14, 5, 2, 67.59, 68, 50),
(63, 14, 5, 2, 81.52, 82, 47),
(90, 14, 5, 2, 7.93, 8, 5),
(10, 15, 5, 2, 3.64, 4, 3),
(10, 1, 1, 3, 38.46, 28, 18),
(15, 3, 1, 3, 11.98, 9, 6),
(10, 4, 1, 3, 5.9, 4, 4),
(13, 4, 1, 3, 114.95, 85, 68),
(14, 4, 1, 3, 112.38, 83, 69),
(9, 21, 1, 3, 120.85, 60, 49),
(4, 22, 1, 3, 145.73, 72, 57),
(10, 24, 1, 3, 75.08, 37, 36),
(44, 5, 3, 3, 33.3, 68, 56),
(30, 13, 5, 3, 47.25, 48, 31),
(77, 13, 5, 3, 27.96, 28, 24),
(80, 13, 5, 3, 50.84, 51, 51),
(83, 13, 5, 3, 82.1, 83, 60),
(5, 14, 5, 3, 34.29, 35, 29),
(15, 14, 5, 3, 66.47, 67, 56),
(25, 14, 5, 3, 29.61, 30, 19),
(30, 14, 5, 3, 53.28, 54, 30),
(64, 14, 5, 3, 81.88, 83, 60),
(20, 15, 5, 3, 16.99, 17, 13),
(23, 15, 5, 3, 53.51, 54, 39),
(35, 15, 5, 3, 58.89, 59, 31),
(14, 1, 1, 4, 10.91, 8, 8),
(8, 2, 1, 4, 21.13, 16, 10),
(8, 4, 1, 4, 101.58, 75, 39),
(14, 22, 1, 4, 140.47, 69, 53),
(46, 5, 3, 4, 32.47, 66, 43),
(41, 6, 3, 4, 17.03, 35, 20),
(48, 6, 3, 4, 11.99, 24, 16),
(45, 7, 3, 4, 48.47, 99, 66),
(44, 25, 3, 4, 58.04, 79, 68),
(10, 13, 5, 4, 60.39, 61, 49),
(21, 13, 5, 4, 61.95, 63, 46),
(87, 13, 5, 4, 37.74, 38, 24),
(92, 13, 5, 4, 21.73, 22, 20),
(41, 15, 5, 4, 89.87, 91, 58),
(50, 15, 5, 4, 13.24, 13, 10),
(71, 15, 5, 4, 14.99, 15, 10),
(80, 15, 5, 4, 76.61, 77, 51),
(3, 3, 1, 5, 8.61, 6, 3),
(8, 21, 1, 5, 60.76, 30, 26),
(12, 21, 1, 5, 195.75, 97, 95),
(4, 23, 1, 5, 50.1, 25, 13),
(14, 24, 1, 5, 147.04, 73, 69),
(48, 5, 3, 5, 39.69, 81, 76),
(79, 13, 5, 5, 5.85, 6, 3),
(85, 13, 5, 5, 58.16, 59, 42),
(8, 14, 5, 5, 24.67, 25, 20),
(20, 14, 5, 5, 37.92, 38, 29),
(22, 14, 5, 5, 79.81, 81, 51),
(23, 14, 5, 5, 47.28, 48, 37),
(37, 14, 5, 5, 30.08, 30, 24),
(50, 14, 5, 5, 44.81, 45, 34),
(24, 15, 5, 5, 0.86, 1, 1),
(28, 15, 5, 5, 17.15, 17, 12),
(34, 15, 5, 5, 25.91, 26, 15),
(60, 15, 5, 5, 70.39, 71, 37),
(6, 1, 1, 6, 87.59, 65, 41),
(12, 1, 1, 6, 22.01, 16, 11),
(15, 1, 1, 6, 51.23, 38, 36),
(11, 3, 1, 6, 113.19, 84, 46),
(14, 21, 1, 6, 113.81, 56, 31),
(2, 22, 1, 6, 80.39, 40, 27),
(5, 23, 1, 6, 190.19, 94, 82),
(11, 24, 1, 6, 28.08, 14, 12),
(47, 5, 3, 6, 43.1, 88, 71),
(47, 6, 3, 6, 4.86, 10, 8),
(46, 25, 3, 6, 18.81, 26, 17),
(5, 13, 5, 6, 29.18, 29, 20),
(26, 13, 5, 6, 26.47, 27, 19),
(41, 13, 5, 6, 92.89, 94, 91),
(49, 13, 5, 6, 59.24, 60, 45),
(71, 13, 5, 6, 25.97, 26, 17),
(72, 13, 5, 6, 77.17, 78, 71),
(86, 13, 5, 6, 42.86, 43, 32),
(89, 13, 5, 6, 19.67, 20, 11),
(6, 14, 5, 6, 16.92, 17, 14),
(33, 14, 5, 6, 81, 82, 82),
(33, 15, 5, 6, 74.44, 75, 75),
(40, 15, 5, 6, 15.58, 16, 13),
(42, 15, 5, 6, 71.08, 72, 52),
(78, 15, 5, 6, 39.15, 40, 25),
(84, 15, 5, 6, 32.02, 32, 21),
(1, 3, 1, 7, 112.21, 83, 77),
(1, 21, 1, 7, 89.14, 44, 22),
(12, 24, 1, 7, 59.61, 29, 28),
(45, 26, 3, 7, 53.6, 73, 56),
(46, 13, 5, 7, 2.26, 2, 1),
(60, 13, 5, 7, 44.18, 45, 39),
(78, 13, 5, 7, 42.97, 43, 33),
(88, 13, 5, 7, 84.59, 85, 76),
(66, 14, 5, 7, 43.26, 44, 24),
(85, 14, 5, 7, 56.67, 57, 46),
(16, 15, 5, 7, 83.62, 84, 68),
(17, 15, 5, 7, 33.92, 34, 19),
(36, 15, 5, 7, 43.5, 44, 37),
(74, 15, 5, 7, 63.37, 64, 48),
(81, 15, 5, 7, 26.66, 27, 26),
(11, 1, 1, 8, 128.25, 95, 66),
(7, 21, 1, 8, 163.41, 81, 47),
(10, 21, 1, 8, 109.74, 54, 40),
(6, 22, 1, 8, 76.17, 38, 22),
(11, 22, 1, 8, 172.41, 85, 76),
(8, 23, 1, 8, 45.84, 23, 12),
(9, 23, 1, 8, 193.81, 96, 86),
(48, 7, 3, 8, 45.55, 93, 51),
(44, 26, 3, 8, 69.11, 94, 80),
(45, 27, 3, 8, 61.11, 83, 80),
(1, 13, 5, 8, 76.92, 78, 56),
(22, 13, 5, 8, 86.49, 87, 82),
(45, 13, 5, 8, 82.3, 83, 67),
(53, 13, 5, 8, 16.47, 17, 16),
(66, 13, 5, 8, 38.27, 39, 31),
(91, 13, 5, 8, 82.99, 84, 67),
(2, 14, 5, 8, 26.02, 26, 21),
(36, 14, 5, 8, 48.89, 49, 32),
(41, 14, 5, 8, 91.11, 92, 46),
(44, 14, 5, 8, 59.34, 60, 48),
(48, 14, 5, 8, 38.47, 39, 28),
(59, 14, 5, 8, 67.96, 69, 48),
(38, 15, 5, 8, 56.33, 57, 44),
(44, 15, 5, 8, 43.42, 44, 24),
(82, 15, 5, 8, 61.15, 62, 54),
(88, 15, 5, 8, 55.64, 56, 40),
(90, 15, 5, 8, 29.95, 30, 29),
(13, 1, 1, 9, 44.1, 33, 20),
(6, 2, 1, 9, 77.58, 57, 30),
(6, 3, 1, 9, 85.99, 64, 49),
(2, 4, 1, 9, 41.23, 30, 20),
(7, 4, 1, 9, 78.45, 58, 49),
(44, 6, 3, 9, 31.72, 65, 34),
(45, 25, 3, 9, 8.07, 11, 6),
(43, 26, 3, 9, 5.22, 7, 6),
(11, 13, 5, 9, 22.87, 23, 14),
(17, 13, 5, 9, 11.9, 12, 10),
(20, 13, 5, 9, 81.95, 83, 82),
(23, 13, 5, 9, 44.6, 45, 32),
(28, 13, 5, 9, 47.83, 48, 41),
(62, 13, 5, 9, 75.78, 77, 74),
(14, 14, 5, 9, 87.91, 89, 57),
(82, 14, 5, 9, 83.42, 84, 56),
(39, 15, 5, 9, 96.52, 97, 68),
(49, 15, 5, 9, 13.58, 14, 12),
(75, 15, 5, 9, 0.1, 0, 0),
(1, 2, 1, 10, 114.89, 85, 48),
(14, 2, 1, 10, 76.33, 56, 37),
(15, 2, 1, 10, 117.11, 87, 85),
(2, 21, 1, 10, 194.2, 96, 60),
(3, 21, 1, 10, 122.06, 60, 43),
(5, 21, 1, 10, 187.07, 92, 60),
(5, 24, 1, 10, 172.77, 85, 51),
(7, 24, 1, 10, 72.51, 36, 19),
(13, 24, 1, 10, 96.84, 48, 44),
(15, 24, 1, 10, 168.96, 83, 55),
(59, 13, 5, 10, 86.28, 87, 65),
(65, 13, 5, 10, 71.86, 73, 47),
(90, 13, 5, 10, 97.8, 99, 87),
(17, 14, 5, 10, 77.87, 79, 51),
(34, 14, 5, 10, 69.82, 71, 49),
(35, 14, 5, 10, 57.66, 58, 41),
(45, 14, 5, 10, 79.88, 81, 65),
(54, 14, 5, 10, 24.02, 24, 20),
(78, 14, 5, 10, 85.98, 87, 59),
(92, 14, 5, 10, 53.59, 54, 41),
(3, 15, 5, 10, 2.85, 3, 1),
(43, 15, 5, 10, 61.45, 62, 40),
(87, 15, 5, 10, 60.95, 62, 33);

-- --------------------------------------------------------

--
-- Table structure for table `Store`
--

DROP TABLE IF EXISTS `Store`;
CREATE TABLE IF NOT EXISTS `Store` (
  `store_key` int(11) NOT NULL,
  `store_number` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `street_address` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `city` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `county` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `state` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `zip` int(11) NOT NULL,
  `district` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `region` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`store_key`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `Store`
--

INSERT INTO `Store` (`store_key`, `store_number`, `street_address`, `city`, `county`, `state`, `zip`, `district`, `region`) VALUES
(1, '1', '999 Main Street', 'New York', 'New York', 'NY', 91089, 'New York', 'Eastern'),
(2, '2', '73 Main Street', 'Chicago', 'Cook', 'IL', 14594, 'Cook', 'Mid West'),
(3, '3', '1 Main Street', 'Atlanta', 'Fulton', 'GA', 54315, 'Fulton', 'South East'),
(4, '4', '575 Main Street', 'Los Angeles', 'Los Angeles', 'CA', 52944, 'Los Angeles', 'Pacific'),
(5, '5', '123 Main Street', 'San Francisco', 'San Francisco', 'CA', 86969, 'San Francisco', 'Pacific'),
(6, '6', '353 Main Street', 'Philadelphia', 'Philadelphia', 'PA', 51458, 'Philadelphia', 'Eastern'),
(7, '7', '839 Main Street', 'Pittsburgh', 'Allegheny', 'PA', 91949, 'Allegheny', 'Eastern'),
(8, '8', '651 Main Street', 'New Orleans', 'Orleans', 'LA', 61163, 'Orleans', 'South West'),
(9, '9', '912 Main Street', 'Seattle', 'King', 'WA', 5764, 'King', 'Pacific'),
(10, '10', '752 Main Street', 'Dallas', 'Dallas', 'TX', 34876, 'Dallas', 'South West');

-- --------------------------------------------------------

--
-- Table structure for table `Time`
--

DROP TABLE IF EXISTS `Time`;
CREATE TABLE IF NOT EXISTS `Time` (
  `time_key` int(11) NOT NULL,
  `date` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `day_of_week` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `day_number_in_month` int(11) NOT NULL,
  `month` int(11) NOT NULL,
  `quarter` int(11) NOT NULL,
  `fiscal_period` varchar(5) COLLATE utf8_unicode_ci NOT NULL,
  `year` int(11) NOT NULL,
  `holiday_flag` varchar(1) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`time_key`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `Time`
--

INSERT INTO `Time` (`time_key`, `date`, `day_of_week`, `day_number_in_month`, `month`, `quarter`, `fiscal_period`, `year`, `holiday_flag`) VALUES
(1, '1994-10-01 0:00:00', 'Saturday', 1, 34638, 4, '4Q94', 1994, 'N'),
(2, '1994-10-02 0:00:00', 'Sunday', 2, 34638, 4, '4Q94', 1994, 'N'),
(3, '1994-10-03 0:00:00', 'Monday', 3, 34638, 4, '4Q94', 1994, 'N'),
(4, '1994-10-04 0:00:00', 'Tuesday', 4, 34638, 4, '4Q94', 1994, 'N'),
(5, '1994-10-05 0:00:00', 'Wednesday', 5, 34638, 4, '4Q94', 1994, 'N'),
(6, '1994-10-06 0:00:00', 'Thursday', 6, 34638, 4, '4Q94', 1994, 'N'),
(7, '1994-10-07 0:00:00', 'Friday', 7, 34638, 4, '4Q94', 1994, 'N'),
(8, '1994-10-08 0:00:00', 'Saturday', 8, 34638, 4, '4Q94', 1994, 'N'),
(9, '1994-10-09 0:00:00', 'Sunday', 9, 34638, 4, '4Q94', 1994, 'N'),
(10, '1994-10-10 0:00:00', 'Monday', 10, 34638, 4, '4Q94', 1994, 'N'),
(11, '1994-10-11 0:00:00', 'Tuesday', 11, 34638, 4, '4Q94', 1994, 'Y'),
(12, '1994-10-12 0:00:00', 'Wednesday', 12, 34638, 4, '4Q94', 1994, 'N'),
(13, '1994-10-13 0:00:00', 'Thursday', 13, 34638, 4, '4Q94', 1994, 'N'),
(14, '1994-10-14 0:00:00', 'Friday', 14, 34638, 4, '4Q94', 1994, 'N'),
(15, '1994-10-15 0:00:00', 'Saturday', 15, 34638, 4, '4Q94', 1994, 'N'),
(16, '1994-10-16 0:00:00', 'Sunday', 16, 34638, 4, '4Q94', 1994, 'N'),
(17, '1994-10-17 0:00:00', 'Monday', 17, 34638, 4, '4Q94', 1994, 'N'),
(18, '1994-10-18 0:00:00', 'Tuesday', 18, 34638, 4, '4Q94', 1994, 'N'),
(19, '1994-10-19 0:00:00', 'Wednesday', 19, 34638, 4, '4Q94', 1994, 'N'),
(20, '1994-10-20 0:00:00', 'Thursday', 20, 34638, 4, '4Q94', 1994, 'N'),
(21, '1994-10-21 0:00:00', 'Friday', 21, 34638, 4, '4Q94', 1994, 'N'),
(22, '1994-10-22 0:00:00', 'Saturday', 22, 34638, 4, '4Q94', 1994, 'N'),
(23, '1994-10-23 0:00:00', 'Sunday', 23, 34638, 4, '4Q94', 1994, 'N'),
(24, '1994-10-24 0:00:00', 'Monday', 24, 34638, 4, '4Q94', 1994, 'N'),
(25, '1994-10-25 0:00:00', 'Tuesday', 25, 34638, 4, '4Q94', 1994, 'N'),
(26, '1994-10-26 0:00:00', 'Wednesday', 26, 34638, 4, '4Q94', 1994, 'N'),
(27, '1994-10-27 0:00:00', 'Thursday', 27, 34638, 4, '4Q94', 1994, 'N'),
(28, '1994-10-28 0:00:00', 'Friday', 28, 34638, 4, '4Q94', 1994, 'N'),
(29, '1994-10-29 0:00:00', 'Saturday', 29, 34638, 4, '4Q94', 1994, 'N'),
(30, '1994-10-30 0:00:00', 'Sunday', 30, 34638, 4, '4Q94', 1994, 'N'),
(31, '1994-10-31 0:00:00', 'Monday', 31, 34638, 4, '4Q94', 1994, 'Y'),
(32, '1994-11-01 0:00:00', 'Tuesday', 1, 34668, 4, '4Q94', 1994, 'N'),
(33, '1994-11-02 0:00:00', 'Wednesday', 2, 34668, 4, '4Q94', 1994, 'N'),
(34, '1994-11-03 0:00:00', 'Thursday', 3, 34668, 4, '4Q94', 1994, 'N'),
(35, '1994-11-04 0:00:00', 'Friday', 4, 34668, 4, '4Q94', 1994, 'N'),
(36, '1994-11-05 0:00:00', 'Saturday', 5, 34668, 4, '4Q94', 1994, 'N'),
(37, '1994-11-06 0:00:00', 'Sunday', 6, 34668, 4, '4Q94', 1994, 'N'),
(38, '1994-11-07 0:00:00', 'Monday', 7, 34668, 4, '4Q94', 1994, 'N'),
(39, '1994-11-08 0:00:00', 'Tuesday', 8, 34668, 4, '4Q94', 1994, 'N'),
(40, '1994-11-09 0:00:00', 'Wednesday', 9, 34668, 4, '4Q94', 1994, 'N'),
(41, '1994-11-10 0:00:00', 'Thursday', 10, 34668, 4, '4Q94', 1994, 'N'),
(42, '1994-11-11 0:00:00', 'Friday', 11, 34668, 4, '4Q94', 1994, 'N'),
(43, '1994-11-12 0:00:00', 'Saturday', 12, 34668, 4, '4Q94', 1994, 'N'),
(44, '1994-11-13 0:00:00', 'Sunday', 13, 34668, 4, '4Q94', 1994, 'N'),
(45, '1994-11-14 0:00:00', 'Monday', 14, 34668, 4, '4Q94', 1994, 'N'),
(46, '1994-11-15 0:00:00', 'Tuesday', 15, 34668, 4, '4Q94', 1994, 'N'),
(47, '1994-11-16 0:00:00', 'Wednesday', 16, 34668, 4, '4Q94', 1994, 'N'),
(48, '1994-11-17 0:00:00', 'Thursday', 17, 34668, 4, '4Q94', 1994, 'N'),
(49, '1994-11-18 0:00:00', 'Friday', 18, 34668, 4, '4Q94', 1994, 'N'),
(50, '1994-11-19 0:00:00', 'Saturday', 19, 34668, 4, '4Q94', 1994, 'N'),
(51, '1994-11-20 0:00:00', 'Sunday', 20, 34668, 4, '4Q94', 1994, 'N'),
(52, '1994-11-21 0:00:00', 'Monday', 21, 34668, 4, '4Q94', 1994, 'N'),
(53, '1994-11-22 0:00:00', 'Tuesday', 22, 34668, 4, '4Q94', 1994, 'N'),
(54, '1994-11-23 0:00:00', 'Wednesday', 23, 34668, 4, '4Q94', 1994, 'N'),
(55, '1994-11-24 0:00:00', 'Thursday', 24, 34668, 4, '4Q94', 1994, 'Y'),
(56, '1994-11-25 0:00:00', 'Friday', 25, 34668, 4, '4Q94', 1994, 'N'),
(57, '1994-11-26 0:00:00', 'Saturday', 26, 34668, 4, '4Q94', 1994, 'N'),
(58, '1994-11-27 0:00:00', 'Sunday', 27, 34668, 4, '4Q94', 1994, 'N'),
(59, '1994-11-28 0:00:00', 'Monday', 28, 34668, 4, '4Q94', 1994, 'N'),
(60, '1994-11-29 0:00:00', 'Tuesday', 29, 34668, 4, '4Q94', 1994, 'N'),
(61, '1994-11-30 0:00:00', 'Wednesday', 30, 34668, 4, '4Q94', 1994, 'N'),
(62, '1994-12-01 0:00:00', 'Thursday', 1, 34699, 4, '4Q94', 1994, 'N'),
(63, '1994-12-02 0:00:00', 'Friday', 2, 34699, 4, '4Q94', 1994, 'N'),
(64, '1994-12-03 0:00:00', 'Saturday', 3, 34699, 4, '4Q94', 1994, 'N'),
(65, '1994-12-04 0:00:00', 'Sunday', 4, 34699, 4, '4Q94', 1994, 'N'),
(66, '1994-12-05 0:00:00', 'Monday', 5, 34699, 4, '4Q94', 1994, 'N'),
(67, '1994-12-06 0:00:00', 'Tuesday', 6, 34699, 4, '4Q94', 1994, 'N'),
(68, '1994-12-07 0:00:00', 'Wednesday', 7, 34699, 4, '4Q94', 1994, 'N'),
(69, '1994-12-08 0:00:00', 'Thursday', 8, 34699, 4, '4Q94', 1994, 'N'),
(70, '1994-12-09 0:00:00', 'Friday', 9, 34699, 4, '4Q94', 1994, 'N'),
(71, '1994-12-10 0:00:00', 'Saturday', 10, 34699, 4, '4Q94', 1994, 'N'),
(72, '1994-12-11 0:00:00', 'Sunday', 11, 34699, 4, '4Q94', 1994, 'N'),
(73, '1994-12-12 0:00:00', 'Monday', 12, 34699, 4, '4Q94', 1994, 'N'),
(74, '1994-12-13 0:00:00', 'Tuesday', 13, 34699, 4, '4Q94', 1994, 'N'),
(75, '1994-12-14 0:00:00', 'Wednesday', 14, 34699, 4, '4Q94', 1994, 'N'),
(76, '1994-12-15 0:00:00', 'Thursday', 15, 34699, 4, '4Q94', 1994, 'N'),
(77, '1994-12-16 0:00:00', 'Friday', 16, 34699, 4, '4Q94', 1994, 'N'),
(78, '1994-12-17 0:00:00', 'Saturday', 17, 34699, 4, '4Q94', 1994, 'N'),
(79, '1994-12-18 0:00:00', 'Sunday', 18, 34699, 4, '4Q94', 1994, 'N'),
(80, '1994-12-19 0:00:00', 'Monday', 19, 34699, 4, '4Q94', 1994, 'N'),
(81, '1994-12-20 0:00:00', 'Tuesday', 20, 34699, 4, '4Q94', 1994, 'N'),
(82, '1994-12-21 0:00:00', 'Wednesday', 21, 34699, 4, '4Q94', 1994, 'N'),
(83, '1994-12-22 0:00:00', 'Thursday', 22, 34699, 4, '4Q94', 1994, 'N'),
(84, '1994-12-23 0:00:00', 'Friday', 23, 34699, 4, '4Q94', 1994, 'N'),
(85, '1994-12-24 0:00:00', 'Saturday', 24, 34699, 4, '4Q94', 1994, 'N'),
(86, '1994-12-25 0:00:00', 'Sunday', 25, 34699, 4, '4Q94', 1994, 'Y'),
(87, '1994-12-26 0:00:00', 'Monday', 26, 34699, 4, '4Q94', 1994, 'N'),
(88, '1994-12-27 0:00:00', 'Tuesday', 27, 34699, 4, '4Q94', 1994, 'N'),
(89, '1994-12-28 0:00:00', 'Wednesday', 28, 34699, 4, '4Q94', 1994, 'N'),
(90, '1994-12-29 0:00:00', 'Thursday', 29, 34699, 4, '4Q94', 1994, 'N'),
(91, '1994-12-30 0:00:00', 'Friday', 30, 34699, 4, '4Q94', 1994, 'N'),
(92, '1994-12-31 0:00:00', 'Saturday', 31, 34699, 4, '4Q94', 1994, 'N');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Sales_Fact`
--
ALTER TABLE `Sales_Fact`
  ADD CONSTRAINT `fk_Sales_Fact_Product` FOREIGN KEY (`product_key`) REFERENCES `Product` (`product_key`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Sales_Fact_Promotion` FOREIGN KEY (`promotion_key`) REFERENCES `Promotion` (`promotion_key`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Sales_Fact_Store` FOREIGN KEY (`store_key`) REFERENCES `Store` (`store_key`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Sales_Fact_Time` FOREIGN KEY (`time_key`) REFERENCES `Time` (`time_key`) ON DELETE NO ACTION ON UPDATE NO ACTION;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
