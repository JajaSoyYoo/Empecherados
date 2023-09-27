CREATE DATABASE  IF NOT EXISTS `seg_egresados2` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `seg_egresados2`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: seg_egresados2
-- ------------------------------------------------------
-- Server version	8.0.34

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
-- Table structure for table `cordis`
--

DROP TABLE IF EXISTS `cordis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cordis` (
  `Correo_Cordinador` varchar(150) NOT NULL,
  `contra` varchar(60) NOT NULL,
  PRIMARY KEY (`Correo_Cordinador`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `general`
--

DROP TABLE IF EXISTS `general`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `general` (
  `Nombres` varchar(70) NOT NULL,
  `Apellido_P` varchar(70) NOT NULL,
  `Apellido_M` varchar(70) NOT NULL,
  `Sexo` varchar(45) NOT NULL,
  `Tel_Contacto` int NOT NULL,
  `Correo_Alumno` varchar(150) NOT NULL,
  `Codigo_Postal` int NOT NULL,
  `Pais` varchar(45) NOT NULL,
  `Estado` varchar(45) NOT NULL,
  `Ciudad` varchar(45) NOT NULL,
  `Colonia` varchar(45) NOT NULL,
  `Nacionalidad` varchar(45) NOT NULL,
  `F_Nacimiento` date NOT NULL,
  PRIMARY KEY (`Correo_Alumno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `grado_estudios`
--

DROP TABLE IF EXISTS `grado_estudios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `grado_estudios` (
  `Uni_procedencia` varchar(60) NOT NULL,
  `Carrera_Procedencial` varchar(45) NOT NULL,
  `Titulado` varchar(10) NOT NULL,
  `Ciclo_egreso` varchar(45) NOT NULL,
  `Nivel_ingles` varchar(45) NOT NULL,
  `Promedio` varchar(45) NOT NULL,
  `Correo_PK` varchar(150) NOT NULL,
  KEY `Correo_PK_idx` (`Correo_PK`),
  CONSTRAINT `Correo_PK` FOREIGN KEY (`Correo_PK`) REFERENCES `general` (`Correo_Alumno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `info_laboral`
--

DROP TABLE IF EXISTS `info_laboral`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `info_laboral` (
  `Trabajando` varchar(10) NOT NULL,
  `Direccion_trabajo` varchar(70) DEFAULT NULL,
  `Horario_Laboral` varchar(45) DEFAULT NULL,
  `Puesto_Trabajo` varchar(45) DEFAULT NULL,
  `info_laboralcol` varchar(45) DEFAULT NULL,
  `Sector` varchar(45) DEFAULT NULL,
  `Correo_PK_Info` varchar(150) NOT NULL,
  KEY `Correo_info_idx` (`Correo_PK_Info`),
  CONSTRAINT `Correo_info` FOREIGN KEY (`Correo_PK_Info`) REFERENCES `general` (`Correo_Alumno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-26 20:09:59
