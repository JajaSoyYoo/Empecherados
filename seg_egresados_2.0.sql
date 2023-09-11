CREATE DATABASE  IF NOT EXISTS `seg_egresados` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `seg_egresados`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: seg_egresados
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
-- Table structure for table `d_general`
--

DROP TABLE IF EXISTS `d_general`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `d_general` (
  `CURP` varchar(18) NOT NULL,
  `Nombre` varchar(45) NOT NULL,
  `Apellido_P` varchar(45) NOT NULL,
  `Apellido_M` varchar(45) NOT NULL,
  `Correo` varchar(150) NOT NULL,
  `F_Nacimineto` date NOT NULL,
  `Codigo_Estudiante` int NOT NULL,
  `Lugar_nacimiento` varchar(100) NOT NULL,
  `Estado_Civil` varchar(45) NOT NULL,
  `Sexo` varchar(45) NOT NULL,
  `N_Celular` int NOT NULL,
  PRIMARY KEY (`Codigo_Estudiante`),
  KEY `correo_idx` (`Correo`),
  CONSTRAINT `correo` FOREIGN KEY (`Correo`) REFERENCES `usuarios` (`correo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `grado_estudios`
--

DROP TABLE IF EXISTS `grado_estudios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `grado_estudios` (
  `Codigo_grado` int NOT NULL,
  `Carrera` varchar(65) NOT NULL,
  `Nivel_estudio` varchar(45) NOT NULL,
  `Centro_Universitario` varchar(100) NOT NULL,
  `Nivel_Ingles` varchar(45) NOT NULL,
  `Ciclo_Escolar_Egresado` varchar(45) NOT NULL,
  `Otro_Idioma` varchar(45) NOT NULL,
  `Titulado` varchar(100) NOT NULL,
  `Fecha_Grado` date NOT NULL,
  `FK_Codigo_Estudiante` int NOT NULL,
  PRIMARY KEY (`Codigo_grado`),
  KEY `Codigo_Estudiante_idx` (`FK_Codigo_Estudiante`),
  CONSTRAINT `Codigo_Estudiante` FOREIGN KEY (`FK_Codigo_Estudiante`) REFERENCES `d_general` (`Codigo_Estudiante`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `info_laboral`
--

DROP TABLE IF EXISTS `info_laboral`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `info_laboral` (
  `Codigo_Inf_Laboral` int NOT NULL,
  `Compatibilidad_Estudios` varchar(100) DEFAULT NULL,
  `Tipo_Trabajo` varchar(45) DEFAULT NULL,
  `Nom_Empresa` varchar(100) DEFAULT NULL,
  `Puesto` varchar(100) DEFAULT NULL,
  `Sector` varchar(60) DEFAULT NULL,
  `Giro_Empresa` varchar(100) DEFAULT NULL,
  `tiempo_laborando` date DEFAULT NULL,
  `FKCodigo_Grado` int NOT NULL,
  PRIMARY KEY (`Codigo_Inf_Laboral`),
  KEY `Codigo_Grado_idx` (`FKCodigo_Grado`),
  CONSTRAINT `Codigo_Grado` FOREIGN KEY (`FKCodigo_Grado`) REFERENCES `grado_estudios` (`Codigo_grado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `correo` varchar(150) NOT NULL,
  `contraseña` varchar(45) NOT NULL,
  PRIMARY KEY (`correo`)
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

-- Dump completed on 2023-09-11  9:16:31
