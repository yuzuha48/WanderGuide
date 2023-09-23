-- MySQL dump 10.13  Distrib 8.0.22, for macos10.15 (x86_64)
--
-- Host: localhost    Database: trips_schema
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `days`
--

DROP TABLE IF EXISTS `days`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `days` (
  `id` int NOT NULL AUTO_INCREMENT,
  `day_theme` varchar(255) DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  `activity` text,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `trips_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_days_trips_idx` (`trips_id`),
  CONSTRAINT `fk_days_trips` FOREIGN KEY (`trips_id`) REFERENCES `trips` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=149 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `days`
--

LOCK TABLES `days` WRITE;
/*!40000 ALTER TABLE `days` DISABLE KEYS */;
INSERT INTO `days` VALUES (46,'Spend the day like a local!','Shimokitazawa','Roam the streets and check out as many thrift shops as you can','2023-05-23 18:05:11','2023-05-23 18:05:11',49),(47,'Embrace being a tourist','Shibuya','Walk through the famous Shibuya Crossing! Make sure you don\'t get lost in the sea of people','2023-05-23 18:05:11','2023-05-23 18:05:11',49),(48,'Day trip for a little history','Kamakura','Take a day trip to Kamakura - see the big Buddha & see some temples!','2023-05-23 18:05:11','2023-05-24 17:04:06',49),(49,'Visit the surfer\'s town','Haleiwa','Drive up to Hawaii\'s north shore - it\'s known for garlic shrimp, shaved ice, and big waves!','2023-05-23 18:32:12','2023-05-23 21:36:07',50),(50,'Take a hike','Diamond Head','Take a hike on Hawaii\'s famous volcano crater! See beautiful views of where Waikiki meets the Pacific Ocean','2023-05-23 18:32:12','2023-05-23 20:40:48',50),(55,'Go cafe-hopping','Ikseondong','You can\'t just go to one cafe when there\'s so many cute cafes in Seoul!','2023-05-23 19:37:50','2023-05-23 19:37:50',52),(56,'Eat street food!','Myeongdong','Try as much of the street food as you can! ','2023-05-23 19:37:50','2023-05-23 19:37:50',52),(58,'Relax by the lakes','Uptown','Walk around the lakes and find a good place to have a picnic! It\'s the perfect place to get some air and people watch at the same time!','2023-05-23 20:49:10','2023-05-23 20:49:10',54),(59,'Shop till you drop','Mall of America','Visit America\'s biggest mall - shop at all the best stores and ride a rollercoaster at the indoor amusement park??','2023-05-23 20:49:10','2023-05-23 20:49:10',54),(60,'Take in the downtown views','Stone Arch Bridge ','Take a stroll down Stone Arch Bridge during sunset and take in the beautiful views of the downtown skyline!','2023-05-23 20:49:10','2023-05-23 20:49:10',54),(61,'Live like a geisha ','Gion','Visit Kyoto\'s geisha district and experience what it\'s like to live like a geisha','2023-05-23 20:54:10','2023-05-23 20:54:10',55),(62,'Immerse yourself in a bamboo forest','Arashiyama Bamboo Forest','If you\'ve seen Instagram pictures in Kyoto, you\'ve definitely seen the beautiful bamboo grove! It\'s truly an immersive experience','2023-05-23 20:54:10','2023-05-23 20:54:10',55),(143,'Be a tourist!','Big Ben','You must see the Big Ben! As touristy as it is, it\'s really a beautiful building, especially in person!','2023-05-25 13:38:28','2023-05-25 13:39:26',80),(144,'Relax in the park','Hyde Park','Get away from the bustle of the city and take a relaxing stroll through Hyde Park!','2023-05-25 13:38:28','2023-05-25 13:38:28',80),(145,'Do a little shopping & admire the archicture','Soho','Beautiful architecture is all around you in London, but in Soho you can shop while admiring the store you shop in!','2023-05-25 13:38:28','2023-05-25 13:38:28',80),(146,'Embrace the city of love','Eiffel Tower','The Eiffel Tower has become a symbol of love! Go up to the top with your lover and take in the beautiful views of Paris ','2023-05-25 13:45:24','2023-05-25 13:45:24',81),(147,'Visit my favorite spot in the city','Montmartre','Montmartre is a town on a hill with lots of outdoor dining! It\'s so lively and I just love strolling around the area ','2023-05-25 13:45:24','2023-05-25 13:45:24',81),(148,'Visit the world\'s most famous art museums','The Louvre','When in Paris, you can\'t forget about the art museums! ','2023-05-25 13:45:24','2023-05-25 13:45:24',81);
/*!40000 ALTER TABLE `days` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-25 13:48:03
