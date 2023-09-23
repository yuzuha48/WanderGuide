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
-- Table structure for table `trips`
--

DROP TABLE IF EXISTS `trips`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trips` (
  `id` int NOT NULL AUTO_INCREMENT,
  `country` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `length_of_stay` int DEFAULT NULL,
  `cover_photo` varchar(255) DEFAULT NULL,
  `itinerary_description` text,
  `interests` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `users_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_trips_users1_idx` (`users_id`),
  CONSTRAINT `fk_trips_users1` FOREIGN KEY (`users_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=82 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trips`
--

LOCK TABLES `trips` WRITE;
/*!40000 ALTER TABLE `trips` DISABLE KEYS */;
INSERT INTO `trips` VALUES (49,'Japan','Tokyo',7,'f641f86d88a34b339e58fefd9e50519d.jpeg','Explore the best of Tokyo! Food, culture, & shopping!',NULL,'2023-05-23 17:59:29','2023-05-24 17:03:20',3),(50,'Hawaii','Honolulu',7,'021f538069aa4b28b9f30b0aa65ef15b.jpeg','The best beaches to see and poke to eat in Honolulu!',NULL,'2023-05-23 18:26:04','2023-05-23 21:17:28',3),(52,'Korea','Seoul',3,'8ef1e60263ab43e18835dde0592be4bb.jpeg','Everything you need to do in Seoul!',NULL,'2023-05-23 19:35:54','2023-05-24 17:47:59',2),(54,'Minnesota','Minneapolis',3,'429c45dcb250448d897221920c2358f4.jpeg','Everything there is to do in Minneapolis!',NULL,'2023-05-23 20:46:07','2023-05-24 17:23:09',3),(55,'Japan','Kyoto',3,'33d1643c4e124946893021a7e21d238c.jpeg','Everywhere you need to go in Japan\'s historic city',NULL,'2023-05-23 20:51:23','2023-05-23 20:51:23',2),(80,'U.K.','London',5,'cd0828594c7540f2ba9f3ce222503e5f.jpeg','The best things to do and see in London!',NULL,'2023-05-25 13:35:48','2023-05-25 13:39:20',2),(81,'France','Paris',5,'5c19a2f408c04976aa8e546f327a7f81.jpeg','All the things to do in Paris!',NULL,'2023-05-25 13:40:55','2023-05-25 13:40:55',3);
/*!40000 ALTER TABLE `trips` ENABLE KEYS */;
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
