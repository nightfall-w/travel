-- MySQL dump 10.16  Distrib 10.1.29-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: travel
-- ------------------------------------------------------
-- Server version	5.6.43

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=82 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add crontab',7,'add_crontabschedule'),(20,'Can change crontab',7,'change_crontabschedule'),(21,'Can delete crontab',7,'delete_crontabschedule'),(22,'Can add interval',8,'add_intervalschedule'),(23,'Can change interval',8,'change_intervalschedule'),(24,'Can delete interval',8,'delete_intervalschedule'),(25,'Can add periodic task',9,'add_periodictask'),(26,'Can change periodic task',9,'change_periodictask'),(27,'Can delete periodic task',9,'delete_periodictask'),(28,'Can add periodic tasks',10,'add_periodictasks'),(29,'Can change periodic tasks',10,'change_periodictasks'),(30,'Can delete periodic tasks',10,'delete_periodictasks'),(31,'Can add task state',11,'add_taskmeta'),(32,'Can change task state',11,'change_taskmeta'),(33,'Can delete task state',11,'delete_taskmeta'),(34,'Can add saved group result',12,'add_tasksetmeta'),(35,'Can change saved group result',12,'change_tasksetmeta'),(36,'Can delete saved group result',12,'delete_tasksetmeta'),(37,'Can add task',13,'add_taskstate'),(38,'Can change task',13,'change_taskstate'),(39,'Can delete task',13,'delete_taskstate'),(40,'Can add worker',14,'add_workerstate'),(41,'Can change worker',14,'change_workerstate'),(42,'Can delete worker',14,'delete_workerstate'),(43,'Can add association',15,'add_association'),(44,'Can change association',15,'change_association'),(45,'Can delete association',15,'delete_association'),(46,'Can add code',16,'add_code'),(47,'Can change code',16,'change_code'),(48,'Can delete code',16,'delete_code'),(49,'Can add nonce',17,'add_nonce'),(50,'Can change nonce',17,'change_nonce'),(51,'Can delete nonce',17,'delete_nonce'),(52,'Can add user social auth',18,'add_usersocialauth'),(53,'Can change user social auth',18,'change_usersocialauth'),(54,'Can delete user social auth',18,'delete_usersocialauth'),(55,'Can add partial',19,'add_partial'),(56,'Can change partial',19,'change_partial'),(57,'Can delete partial',19,'delete_partial'),(58,'Can add 用户信息',20,'add_auth_profile'),(59,'Can change 用户信息',20,'change_auth_profile'),(60,'Can delete 用户信息',20,'delete_auth_profile'),(61,'Can add 旅游项目',21,'add_scheme'),(62,'Can change 旅游项目',21,'change_scheme'),(63,'Can delete 旅游项目',21,'delete_scheme'),(64,'Can add 相册',22,'add_scenic'),(65,'Can change 相册',22,'change_scenic'),(66,'Can delete 相册',22,'delete_scenic'),(67,'Can add 票务',23,'add_ticket'),(68,'Can change 票务',23,'change_ticket'),(69,'Can delete 票务',23,'delete_ticket'),(70,'Can add 评价',24,'add_score'),(71,'Can change 评价',24,'change_score'),(72,'Can delete 评价',24,'delete_score'),(73,'Can add 用户评论',25,'add_review'),(74,'Can change 用户评论',25,'change_review'),(75,'Can delete 用户评论',25,'delete_review'),(76,'Can add 行程',26,'add_journey'),(77,'Can change 行程',26,'change_journey'),(78,'Can delete 行程',26,'delete_journey'),(79,'Can add 酒店',27,'add_groggery'),(80,'Can change 酒店',27,'change_groggery'),(81,'Can delete 酒店',27,'delete_groggery');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_profile`
--

DROP TABLE IF EXISTS `auth_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_profile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `phone_number` varchar(11) NOT NULL,
  `head_photo` varchar(100) NOT NULL,
  `user_obj_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_obj_id` (`user_obj_id`),
  CONSTRAINT `auth_profile_user_obj_id_d582770d_fk_auth_user_id` FOREIGN KEY (`user_obj_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_profile`
--

LOCK TABLES `auth_profile` WRITE;
/*!40000 ALTER TABLE `auth_profile` DISABLE KEYS */;
INSERT INTO `auth_profile` VALUES (1,'18901942952','/media/head_portrait/9e286d0e-6450-11e9-b24a-000c2913cfcf.jepg',1);
/*!40000 ALTER TABLE `auth_profile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$36000$XsDtbQFDPCb7$+aJu1KZnJ9owOzUXZ5+AdNjBGhg2pLCxv4kFSjJgGNg=','2019-04-22 00:28:39.302195',0,'baojunw','','','',0,1,'2019-04-22 00:15:02.541036'),(2,'pbkdf2_sha256$36000$8eIgR2ZIKzSw$xHGMzVuuz1vM0J7vuoV/v3La0WqKHsHsUhWN9klKWQ4=','2019-04-22 21:48:26.733751',1,'admin','','','',1,1,'2019-04-22 21:47:58.385080');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `celery_taskmeta`
--

DROP TABLE IF EXISTS `celery_taskmeta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `celery_taskmeta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `task_id` varchar(255) NOT NULL,
  `status` varchar(50) NOT NULL,
  `result` longtext,
  `date_done` datetime(6) NOT NULL,
  `traceback` longtext,
  `hidden` tinyint(1) NOT NULL,
  `meta` longtext,
  PRIMARY KEY (`id`),
  UNIQUE KEY `task_id` (`task_id`),
  KEY `celery_taskmeta_hidden_23fd02dc` (`hidden`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `celery_taskmeta`
--

LOCK TABLES `celery_taskmeta` WRITE;
/*!40000 ALTER TABLE `celery_taskmeta` DISABLE KEYS */;
/*!40000 ALTER TABLE `celery_taskmeta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `celery_tasksetmeta`
--

DROP TABLE IF EXISTS `celery_tasksetmeta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `celery_tasksetmeta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `taskset_id` varchar(255) NOT NULL,
  `result` longtext NOT NULL,
  `date_done` datetime(6) NOT NULL,
  `hidden` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `taskset_id` (`taskset_id`),
  KEY `celery_tasksetmeta_hidden_593cfc24` (`hidden`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `celery_tasksetmeta`
--

LOCK TABLES `celery_tasksetmeta` WRITE;
/*!40000 ALTER TABLE `celery_tasksetmeta` DISABLE KEYS */;
/*!40000 ALTER TABLE `celery_tasksetmeta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2019-04-22 22:05:13.430955','1','【跟团游】0自费|五星豪华酒店+海景酒店|花海骑行+洱海游船+冰川大索道+民俗佳',1,'[{\"added\": {}}]',21,2),(2,'2019-04-22 22:06:37.687251','1','【跟团游】0自费|五星豪华酒店+海景酒店|花海骑行+洱海游船+冰川大索道+民俗佳',2,'[{\"changed\": {\"fields\": [\"is_delete\"]}}]',21,2),(3,'2019-04-22 22:11:04.043473','1','昆明佳华广场酒店',1,'[{\"added\": {}}]',27,2),(4,'2019-04-22 22:12:48.694596','2','昆明花之城豪生国际大酒店',1,'[{\"added\": {}}]',27,2),(5,'2019-04-22 22:15:23.315588','3','昆明铭春花园温泉度假酒店',1,'[{\"added\": {}}]',27,2),(6,'2019-04-22 22:15:26.581237','1','【跟团游】0自费|五星豪华酒店+海景酒店|花海骑行+洱海游船+冰川大索道+民俗佳',2,'[]',21,2),(7,'2019-04-22 22:22:40.953606','1','石林',1,'[{\"added\": {}}]',22,2),(8,'2019-04-22 22:22:53.803571','2','石林',1,'[{\"added\": {}}]',22,2),(9,'2019-04-22 22:23:06.412612','3','石林',1,'[{\"added\": {}}]',22,2),(10,'2019-04-22 22:23:16.932782','4','石林',1,'[{\"added\": {}}]',22,2),(11,'2019-04-22 22:25:52.999160','1','【跟团游】0自费|五星豪华酒店+海景酒店|花海骑行+洱海游船+冰川大索道+民俗佳',2,'[]',21,2),(12,'2019-04-22 22:27:34.275620','5','阿诗玛化身石',1,'[{\"added\": {}}]',22,2),(13,'2019-04-22 22:27:51.212442','6','阿诗玛化身石',1,'[{\"added\": {}}]',22,2),(14,'2019-04-22 22:28:07.741154','7','阿诗玛化身石',1,'[{\"added\": {}}]',22,2),(15,'2019-04-22 22:28:19.878566','8','阿诗玛化身石',1,'[{\"added\": {}}]',22,2),(16,'2019-04-22 22:59:36.099364','9','彝乡恋歌篝火盛宴',1,'[{\"added\": {}}]',22,2),(17,'2019-04-22 22:59:50.949087','10','彝乡恋歌篝火盛宴',1,'[{\"added\": {}}]',22,2),(18,'2019-04-22 23:00:52.256047','11','洱海游船',1,'[{\"added\": {}}]',22,2),(19,'2019-04-22 23:01:02.325139','12','洱海游船',1,'[{\"added\": {}}]',22,2),(20,'2019-04-22 23:01:10.421996','13','洱海游船',1,'[{\"added\": {}}]',22,2),(21,'2019-04-22 23:01:57.810868','14','花海骑行',1,'[{\"added\": {}}]',22,2),(22,'2019-04-22 23:02:08.115383','15','花海骑行',1,'[{\"added\": {}}]',22,2),(23,'2019-04-22 23:02:21.112807','16','花海骑行',1,'[{\"added\": {}}]',22,2),(24,'2019-04-22 23:02:28.613424','17','花海骑行',1,'[{\"added\": {}}]',22,2),(25,'2019-04-22 23:03:18.957196','18','洱海',1,'[{\"added\": {}}]',22,2),(26,'2019-04-22 23:03:27.515312','19','洱海',1,'[{\"added\": {}}]',22,2),(27,'2019-04-22 23:03:40.137284','20','洱海',1,'[{\"added\": {}}]',22,2),(28,'2019-04-22 23:04:17.514818','21','南诏风情岛',1,'[{\"added\": {}}]',22,2),(29,'2019-04-22 23:04:51.877565','22','花语牧场',1,'[{\"added\": {}}]',22,2),(30,'2019-04-22 23:05:06.205216','23','花语牧场',1,'[{\"added\": {}}]',22,2),(31,'2019-04-23 18:30:48.239799','4','【跟团游】0自费|五星豪华酒店+海景酒店|花海骑行+洱海游船+冰川大索道+民俗佳',1,'[{\"added\": {}}]',23,2),(32,'2019-04-23 18:32:07.298245','5','【跟团游】0自费|五星豪华酒店+海景酒店|花海骑行+洱海游船+冰川大索道+民俗佳',1,'[{\"added\": {}}]',23,2),(33,'2019-04-23 18:32:54.703107','6','【跟团游】0自费|五星豪华酒店+海景酒店|花海骑行+洱海游船+冰川大索道+民俗佳',1,'[{\"added\": {}}]',23,2),(34,'2019-04-23 18:42:00.534803','2','【跟团游】0自费|五星豪华酒店+海景酒店|花海骑行+洱海游船+冰川大索道+民俗佳',1,'[{\"added\": {}}]',26,2),(35,'2019-04-23 18:43:02.796439','2','【跟团游】0自费|五星豪华酒店+海景酒店|花海骑行+洱海游船+冰川大索道+民俗佳',2,'[{\"changed\": {\"fields\": [\"time\", \"day\"]}}]',26,2),(36,'2019-04-23 18:44:14.709646','3','【跟团游】0自费|五星豪华酒店+海景酒店|花海骑行+洱海游船+冰川大索道+民俗佳',1,'[{\"added\": {}}]',26,2),(37,'2019-04-23 18:50:43.630272','5','5',1,'[{\"added\": {}}]',24,2);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'djcelery','crontabschedule'),(8,'djcelery','intervalschedule'),(9,'djcelery','periodictask'),(10,'djcelery','periodictasks'),(11,'djcelery','taskmeta'),(12,'djcelery','tasksetmeta'),(13,'djcelery','taskstate'),(14,'djcelery','workerstate'),(27,'info','groggery'),(26,'info','journey'),(25,'info','review'),(22,'info','scenic'),(21,'info','scheme'),(24,'info','score'),(23,'info','ticket'),(6,'sessions','session'),(15,'social_django','association'),(16,'social_django','code'),(17,'social_django','nonce'),(19,'social_django','partial'),(18,'social_django','usersocialauth'),(20,'user','auth_profile');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-04-21 20:32:26.058210'),(2,'auth','0001_initial','2019-04-21 20:32:28.639027'),(3,'admin','0001_initial','2019-04-21 20:32:29.225775'),(4,'admin','0002_logentry_remove_auto_add','2019-04-21 20:32:29.293229'),(5,'contenttypes','0002_remove_content_type_name','2019-04-21 20:32:29.633977'),(6,'auth','0002_alter_permission_name_max_length','2019-04-21 20:32:29.849951'),(7,'auth','0003_alter_user_email_max_length','2019-04-21 20:32:30.100680'),(8,'auth','0004_alter_user_username_opts','2019-04-21 20:32:30.151116'),(9,'auth','0005_alter_user_last_login_null','2019-04-21 20:32:30.309187'),(10,'auth','0006_require_contenttypes_0002','2019-04-21 20:32:30.325147'),(11,'auth','0007_alter_validators_add_error_messages','2019-04-21 20:32:30.366101'),(12,'auth','0008_alter_user_username_max_length','2019-04-21 20:32:30.578435'),(13,'djcelery','0001_initial','2019-04-21 20:32:32.832537'),(14,'sessions','0001_initial','2019-04-21 20:32:33.002054'),(15,'default','0001_initial','2019-04-21 20:32:33.925131'),(16,'social_auth','0001_initial','2019-04-21 20:32:33.949047'),(17,'default','0002_add_related_name','2019-04-21 20:32:34.245478'),(18,'social_auth','0002_add_related_name','2019-04-21 20:32:34.261462'),(19,'default','0003_alter_email_max_length','2019-04-21 20:32:34.483340'),(20,'social_auth','0003_alter_email_max_length','2019-04-21 20:32:34.499662'),(21,'default','0004_auto_20160423_0400','2019-04-21 20:32:34.554176'),(22,'social_auth','0004_auto_20160423_0400','2019-04-21 20:32:34.564140'),(23,'social_auth','0005_auto_20160727_2333','2019-04-21 20:32:34.640520'),(24,'social_django','0006_partial','2019-04-21 20:32:34.817858'),(25,'social_django','0007_code_timestamp','2019-04-21 20:32:35.073642'),(26,'social_django','0008_partial_timestamp','2019-04-21 20:32:35.319653'),(27,'social_django','0003_alter_email_max_length','2019-04-21 20:32:35.345971'),(28,'social_django','0005_auto_20160727_2333','2019-04-21 20:32:35.362913'),(29,'social_django','0001_initial','2019-04-21 20:32:35.378090'),(30,'social_django','0002_add_related_name','2019-04-21 20:32:35.394453'),(31,'social_django','0004_auto_20160423_0400','2019-04-21 20:32:35.410552'),(32,'info','0001_initial','2019-04-21 20:54:04.756440'),(33,'user','0001_initial','2019-04-21 20:54:05.239001'),(34,'info','0002_scheme_scenic','2019-04-22 22:25:37.853776'),(35,'info','0003_auto_20190423_1830','2019-04-23 18:30:35.148521'),(36,'info','0004_auto_20190423_1835','2019-04-23 18:35:25.202344');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `djcelery_crontabschedule`
--

DROP TABLE IF EXISTS `djcelery_crontabschedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `djcelery_crontabschedule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `minute` varchar(64) NOT NULL,
  `hour` varchar(64) NOT NULL,
  `day_of_week` varchar(64) NOT NULL,
  `day_of_month` varchar(64) NOT NULL,
  `month_of_year` varchar(64) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `djcelery_crontabschedule`
--

LOCK TABLES `djcelery_crontabschedule` WRITE;
/*!40000 ALTER TABLE `djcelery_crontabschedule` DISABLE KEYS */;
/*!40000 ALTER TABLE `djcelery_crontabschedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `djcelery_intervalschedule`
--

DROP TABLE IF EXISTS `djcelery_intervalschedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `djcelery_intervalschedule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `every` int(11) NOT NULL,
  `period` varchar(24) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `djcelery_intervalschedule`
--

LOCK TABLES `djcelery_intervalschedule` WRITE;
/*!40000 ALTER TABLE `djcelery_intervalschedule` DISABLE KEYS */;
/*!40000 ALTER TABLE `djcelery_intervalschedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `djcelery_periodictask`
--

DROP TABLE IF EXISTS `djcelery_periodictask`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `djcelery_periodictask` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `task` varchar(200) NOT NULL,
  `args` longtext NOT NULL,
  `kwargs` longtext NOT NULL,
  `queue` varchar(200) DEFAULT NULL,
  `exchange` varchar(200) DEFAULT NULL,
  `routing_key` varchar(200) DEFAULT NULL,
  `expires` datetime(6) DEFAULT NULL,
  `enabled` tinyint(1) NOT NULL,
  `last_run_at` datetime(6) DEFAULT NULL,
  `total_run_count` int(10) unsigned NOT NULL,
  `date_changed` datetime(6) NOT NULL,
  `description` longtext NOT NULL,
  `crontab_id` int(11) DEFAULT NULL,
  `interval_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `djcelery_periodictas_crontab_id_75609bab_fk_djcelery_` (`crontab_id`),
  KEY `djcelery_periodictas_interval_id_b426ab02_fk_djcelery_` (`interval_id`),
  CONSTRAINT `djcelery_periodictas_crontab_id_75609bab_fk_djcelery_` FOREIGN KEY (`crontab_id`) REFERENCES `djcelery_crontabschedule` (`id`),
  CONSTRAINT `djcelery_periodictas_interval_id_b426ab02_fk_djcelery_` FOREIGN KEY (`interval_id`) REFERENCES `djcelery_intervalschedule` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `djcelery_periodictask`
--

LOCK TABLES `djcelery_periodictask` WRITE;
/*!40000 ALTER TABLE `djcelery_periodictask` DISABLE KEYS */;
/*!40000 ALTER TABLE `djcelery_periodictask` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `djcelery_periodictasks`
--

DROP TABLE IF EXISTS `djcelery_periodictasks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `djcelery_periodictasks` (
  `ident` smallint(6) NOT NULL,
  `last_update` datetime(6) NOT NULL,
  PRIMARY KEY (`ident`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `djcelery_periodictasks`
--

LOCK TABLES `djcelery_periodictasks` WRITE;
/*!40000 ALTER TABLE `djcelery_periodictasks` DISABLE KEYS */;
/*!40000 ALTER TABLE `djcelery_periodictasks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `djcelery_taskstate`
--

DROP TABLE IF EXISTS `djcelery_taskstate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `djcelery_taskstate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `state` varchar(64) NOT NULL,
  `task_id` varchar(36) NOT NULL,
  `name` varchar(200) DEFAULT NULL,
  `tstamp` datetime(6) NOT NULL,
  `args` longtext,
  `kwargs` longtext,
  `eta` datetime(6) DEFAULT NULL,
  `expires` datetime(6) DEFAULT NULL,
  `result` longtext,
  `traceback` longtext,
  `runtime` double DEFAULT NULL,
  `retries` int(11) NOT NULL,
  `hidden` tinyint(1) NOT NULL,
  `worker_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `task_id` (`task_id`),
  KEY `djcelery_taskstate_state_53543be4` (`state`),
  KEY `djcelery_taskstate_name_8af9eded` (`name`),
  KEY `djcelery_taskstate_tstamp_4c3f93a1` (`tstamp`),
  KEY `djcelery_taskstate_hidden_c3905e57` (`hidden`),
  KEY `djcelery_taskstate_worker_id_f7f57a05_fk_djcelery_workerstate_id` (`worker_id`),
  CONSTRAINT `djcelery_taskstate_worker_id_f7f57a05_fk_djcelery_workerstate_id` FOREIGN KEY (`worker_id`) REFERENCES `djcelery_workerstate` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `djcelery_taskstate`
--

LOCK TABLES `djcelery_taskstate` WRITE;
/*!40000 ALTER TABLE `djcelery_taskstate` DISABLE KEYS */;
/*!40000 ALTER TABLE `djcelery_taskstate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `djcelery_workerstate`
--

DROP TABLE IF EXISTS `djcelery_workerstate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `djcelery_workerstate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hostname` varchar(255) NOT NULL,
  `last_heartbeat` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `hostname` (`hostname`),
  KEY `djcelery_workerstate_last_heartbeat_4539b544` (`last_heartbeat`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `djcelery_workerstate`
--

LOCK TABLES `djcelery_workerstate` WRITE;
/*!40000 ALTER TABLE `djcelery_workerstate` DISABLE KEYS */;
/*!40000 ALTER TABLE `djcelery_workerstate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `groggery`
--

DROP TABLE IF EXISTS `groggery`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `groggery` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `image` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `groggery`
--

LOCK TABLES `groggery` WRITE;
/*!40000 ALTER TABLE `groggery` DISABLE KEYS */;
INSERT INTO `groggery` VALUES (1,'昆明佳华广场酒店','images/groggery/nw_FAPFqKUj8A.jpg'),(2,'昆明花之城豪生国际大酒店','images/groggery/51276001.jpg'),(3,'昆明铭春花园温泉度假酒店','images/groggery/timg.jpeg');
/*!40000 ALTER TABLE `groggery` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `journey`
--

DROP TABLE IF EXISTS `journey`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `journey` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time` time(6) NOT NULL,
  `day` int(11) NOT NULL,
  `visit_address` varchar(20) NOT NULL,
  `content` longtext NOT NULL,
  `cafe_id` int(11) NOT NULL,
  `scheme_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `journey_cafe_id_58a21065_fk_groggery_id` (`cafe_id`),
  KEY `journey_scheme_id_a70224a9_fk_scheme_id` (`scheme_id`),
  CONSTRAINT `journey_cafe_id_58a21065_fk_groggery_id` FOREIGN KEY (`cafe_id`) REFERENCES `groggery` (`id`),
  CONSTRAINT `journey_scheme_id_a70224a9_fk_scheme_id` FOREIGN KEY (`scheme_id`) REFERENCES `scheme` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `journey`
--

LOCK TABLES `journey` WRITE;
/*!40000 ALTER TABLE `journey` DISABLE KEYS */;
INSERT INTO `journey` VALUES (2,'09:00:00.000000',2,'石林，楚雄','❤【游览】9点前往游览石林国家地质公园，游览时间90分钟\r\n石林风景区又称为云南石林，位于云南省昆明市石林彝族自治县境内，面积350平方公里，景奇物丰，风情浓郁，石林是阿诗玛的故乡；石林形成于2.7亿年前，是世界喀斯特地貌的精华，拥有世界上喀斯特地貌演化历史久远、分布面积广、类型齐全、形态独特的古生代岩溶地貌群落，风景区由石林、黑松岩（乃古石林）、飞龙瀑（大叠水）、长湖、圭山、月湖、奇风洞等组成，以雄、奇、险、秀、幽、奥、旷著称，“阿诗玛”的美丽传说始终传颂着彝家女子至死不渝的爱情诗篇，令人荡气回肠。\r\n昆明—楚雄晚餐—入住酒店 \r\n❤【晚餐】途径楚雄享用特色晚餐，彝族长街宴，及享彝乡恋歌篝火盛宴。',1,1),(3,'12:00:00.000000',1,'昆明','根据航班时间乘机飞抵春城昆明，我社专业接机/高铁人员到机场/高铁站迎接您的到来,并送您入住酒店。温馨提示1、当您入住酒店后要注意休息，做好体力储备，尤其是初上高原的贵宾，请注意不要剧烈运动或过量饮酒，今天没有安排团体膳食，各位贵宾可自行品尝云南小吃。2、报名时请留下您在旅游期间使用的手机号码，方便导游用短信与您联络，确保在机场出站口第一时间能接到您。',2,1);
/*!40000 ALTER TABLE `journey` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `review`
--

DROP TABLE IF EXISTS `review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `review` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` longtext NOT NULL,
  `create` datetime(6) NOT NULL,
  `assist` bigint(20) NOT NULL,
  `oppose` bigint(20) NOT NULL,
  `scheme_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `review_scheme_id_676a0564_fk_scheme_id` (`scheme_id`),
  KEY `review_user_id_1520d914_fk_auth_user_id` (`user_id`),
  CONSTRAINT `review_scheme_id_676a0564_fk_scheme_id` FOREIGN KEY (`scheme_id`) REFERENCES `scheme` (`id`),
  CONSTRAINT `review_user_id_1520d914_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `review`
--

LOCK TABLES `review` WRITE;
/*!40000 ALTER TABLE `review` DISABLE KEYS */;
/*!40000 ALTER TABLE `review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scenic`
--

DROP TABLE IF EXISTS `scenic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scenic` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL,
  `image` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scenic`
--

LOCK TABLES `scenic` WRITE;
/*!40000 ALTER TABLE `scenic` DISABLE KEYS */;
INSERT INTO `scenic` VALUES (1,'石林','images/scenic/f6e06e0771ff9702.jpg'),(2,'石林','images/scenic/c248495c25e3b602.jpg'),(3,'石林','images/scenic/71371a297f298102.jpg'),(4,'石林','images/scenic/7cf2f0ddce5c1a02.jpg'),(5,'阿诗玛化身石','images/scenic/39381e457046ee02.jpg'),(6,'阿诗玛化身石','images/scenic/64cbae0850ebc202.jpg'),(7,'阿诗玛化身石','images/scenic/16aee64baccb9002.jpg'),(8,'阿诗玛化身石','images/scenic/a8488267577f1202.png'),(9,'彝乡恋歌篝火盛宴','images/scenic/3575f2a8-72c9-4460-9164-41f1323dff7e.jpeg'),(10,'彝乡恋歌篝火盛宴','images/scenic/44bff2ed-d112-4f10-a091-1d609cabdfab.jpeg'),(11,'洱海游船','images/scenic/07175f86-737a-4967-8cab-ffb824fd3e8d.jpg'),(12,'洱海游船','images/scenic/e9ec7c5a-5a45-45ba-b803-d5c2e037b8e0.jpg'),(13,'洱海游船','images/scenic/5a3844d3-14cf-4e63-9e74-9312223b6918.jpg'),(14,'花海骑行','images/scenic/3f5f71fd8bb49d02.jpg'),(15,'花海骑行','images/scenic/10cbb7918aee2302.jpg'),(16,'花海骑行','images/scenic/b1541a54-2fc2-4fb7-868b-6c36185c432e.jpg'),(17,'花海骑行','images/scenic/2554c43c-7dcd-4220-a708-8e75fe010350.jpg'),(18,'洱海','images/scenic/b1451f6f0c342ea6ffffffffc8d65eac.jpg'),(19,'洱海','images/scenic/afb2b552381abbfdffffffffc8d65eac.jpg'),(20,'洱海','images/scenic/6a863dac18d700acffffffffc8d65eac.jpg'),(21,'南诏风情岛','images/scenic/d8b0ef5c1697f4a0ba2c6238c0e95763.jpg'),(22,'花语牧场','images/scenic/eb3257d4-2ccb-4f85-a869-acbc6f348a1c.jpg'),(23,'花语牧场','images/scenic/bd11f5ff-72a4-4a78-a448-bd2598616536.jpg');
/*!40000 ALTER TABLE `scenic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scheme`
--

DROP TABLE IF EXISTS `scheme`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scheme` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL,
  `coordinate` varchar(50) NOT NULL,
  `originating` varchar(20) NOT NULL,
  `end_locale` varchar(20) NOT NULL,
  `through_time` int(11) NOT NULL,
  `day` int(11) NOT NULL,
  `night` int(11) NOT NULL,
  `create_date` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scheme`
--

LOCK TABLES `scheme` WRITE;
/*!40000 ALTER TABLE `scheme` DISABLE KEYS */;
INSERT INTO `scheme` VALUES (1,'【跟团游】0自费|五星豪华酒店+海景酒店|花海骑行+洱海游船+冰川大索道+民俗佳','25.0218700000,102.7218400000','厦门','昆明',6,6,5,'2019-04-22 22:05:13.371326',1);
/*!40000 ALTER TABLE `scheme` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scheme_favorites`
--

DROP TABLE IF EXISTS `scheme_favorites`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scheme_favorites` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `scheme_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `scheme_favorites_scheme_id_user_id_656b52ed_uniq` (`scheme_id`,`user_id`),
  KEY `scheme_favorites_user_id_164e6580_fk_auth_user_id` (`user_id`),
  CONSTRAINT `scheme_favorites_scheme_id_61490ec5_fk_scheme_id` FOREIGN KEY (`scheme_id`) REFERENCES `scheme` (`id`),
  CONSTRAINT `scheme_favorites_user_id_164e6580_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scheme_favorites`
--

LOCK TABLES `scheme_favorites` WRITE;
/*!40000 ALTER TABLE `scheme_favorites` DISABLE KEYS */;
INSERT INTO `scheme_favorites` VALUES (1,1,1),(2,1,2);
/*!40000 ALTER TABLE `scheme_favorites` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scheme_groggery`
--

DROP TABLE IF EXISTS `scheme_groggery`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scheme_groggery` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `scheme_id` int(11) NOT NULL,
  `groggery_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `scheme_groggery_scheme_id_groggery_id_deac7f20_uniq` (`scheme_id`,`groggery_id`),
  KEY `scheme_groggery_groggery_id_2200cf3f_fk_groggery_id` (`groggery_id`),
  CONSTRAINT `scheme_groggery_groggery_id_2200cf3f_fk_groggery_id` FOREIGN KEY (`groggery_id`) REFERENCES `groggery` (`id`),
  CONSTRAINT `scheme_groggery_scheme_id_dbda5693_fk_scheme_id` FOREIGN KEY (`scheme_id`) REFERENCES `scheme` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scheme_groggery`
--

LOCK TABLES `scheme_groggery` WRITE;
/*!40000 ALTER TABLE `scheme_groggery` DISABLE KEYS */;
INSERT INTO `scheme_groggery` VALUES (1,1,1),(2,1,2),(3,1,3);
/*!40000 ALTER TABLE `scheme_groggery` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scheme_scenic`
--

DROP TABLE IF EXISTS `scheme_scenic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scheme_scenic` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `scheme_id` int(11) NOT NULL,
  `scenic_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `scheme_scenic_scheme_id_scenic_id_1b888f5d_uniq` (`scheme_id`,`scenic_id`),
  KEY `scheme_scenic_scenic_id_42ddf0cd_fk_scenic_id` (`scenic_id`),
  CONSTRAINT `scheme_scenic_scenic_id_42ddf0cd_fk_scenic_id` FOREIGN KEY (`scenic_id`) REFERENCES `scenic` (`id`),
  CONSTRAINT `scheme_scenic_scheme_id_96457114_fk_scheme_id` FOREIGN KEY (`scheme_id`) REFERENCES `scheme` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scheme_scenic`
--

LOCK TABLES `scheme_scenic` WRITE;
/*!40000 ALTER TABLE `scheme_scenic` DISABLE KEYS */;
INSERT INTO `scheme_scenic` VALUES (1,1,1),(2,1,2),(3,1,3),(4,1,4);
/*!40000 ALTER TABLE `scheme_scenic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scheme_score`
--

DROP TABLE IF EXISTS `scheme_score`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scheme_score` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `scheme_id` int(11) NOT NULL,
  `score_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `scheme_score_scheme_id_score_id_52a943a5_uniq` (`scheme_id`,`score_id`),
  KEY `scheme_score_score_id_4062414b_fk_score_id` (`score_id`),
  CONSTRAINT `scheme_score_scheme_id_e517ac51_fk_scheme_id` FOREIGN KEY (`scheme_id`) REFERENCES `scheme` (`id`),
  CONSTRAINT `scheme_score_score_id_4062414b_fk_score_id` FOREIGN KEY (`score_id`) REFERENCES `score` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scheme_score`
--

LOCK TABLES `scheme_score` WRITE;
/*!40000 ALTER TABLE `scheme_score` DISABLE KEYS */;
/*!40000 ALTER TABLE `scheme_score` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `score`
--

DROP TABLE IF EXISTS `score`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `score` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `score_number` int(11) NOT NULL,
  `category` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `score`
--

LOCK TABLES `score` WRITE;
/*!40000 ALTER TABLE `score` DISABLE KEYS */;
INSERT INTO `score` VALUES (5,5,1);
/*!40000 ALTER TABLE `score` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `score_user`
--

DROP TABLE IF EXISTS `score_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `score_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `score_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `score_user_score_id_user_id_40bffd93_uniq` (`score_id`,`user_id`),
  KEY `score_user_user_id_6ae5d9db_fk_auth_user_id` (`user_id`),
  CONSTRAINT `score_user_score_id_a11e1160_fk_score_id` FOREIGN KEY (`score_id`) REFERENCES `score` (`id`),
  CONSTRAINT `score_user_user_id_6ae5d9db_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `score_user`
--

LOCK TABLES `score_user` WRITE;
/*!40000 ALTER TABLE `score_user` DISABLE KEYS */;
INSERT INTO `score_user` VALUES (5,5,1);
/*!40000 ALTER TABLE `score_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_auth_association`
--

DROP TABLE IF EXISTS `social_auth_association`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `social_auth_association` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `server_url` varchar(255) NOT NULL,
  `handle` varchar(255) NOT NULL,
  `secret` varchar(255) NOT NULL,
  `issued` int(11) NOT NULL,
  `lifetime` int(11) NOT NULL,
  `assoc_type` varchar(64) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `social_auth_association_server_url_handle_078befa2_uniq` (`server_url`,`handle`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_auth_association`
--

LOCK TABLES `social_auth_association` WRITE;
/*!40000 ALTER TABLE `social_auth_association` DISABLE KEYS */;
/*!40000 ALTER TABLE `social_auth_association` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_auth_code`
--

DROP TABLE IF EXISTS `social_auth_code`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `social_auth_code` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(254) NOT NULL,
  `code` varchar(32) NOT NULL,
  `verified` tinyint(1) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `social_auth_code_email_code_801b2d02_uniq` (`email`,`code`),
  KEY `social_auth_code_code_a2393167` (`code`),
  KEY `social_auth_code_timestamp_176b341f` (`timestamp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_auth_code`
--

LOCK TABLES `social_auth_code` WRITE;
/*!40000 ALTER TABLE `social_auth_code` DISABLE KEYS */;
/*!40000 ALTER TABLE `social_auth_code` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_auth_nonce`
--

DROP TABLE IF EXISTS `social_auth_nonce`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `social_auth_nonce` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `server_url` varchar(255) NOT NULL,
  `timestamp` int(11) NOT NULL,
  `salt` varchar(65) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `social_auth_nonce_server_url_timestamp_salt_f6284463_uniq` (`server_url`,`timestamp`,`salt`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_auth_nonce`
--

LOCK TABLES `social_auth_nonce` WRITE;
/*!40000 ALTER TABLE `social_auth_nonce` DISABLE KEYS */;
/*!40000 ALTER TABLE `social_auth_nonce` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_auth_partial`
--

DROP TABLE IF EXISTS `social_auth_partial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `social_auth_partial` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `token` varchar(32) NOT NULL,
  `next_step` smallint(5) unsigned NOT NULL,
  `backend` varchar(32) NOT NULL,
  `data` longtext NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `social_auth_partial_token_3017fea3` (`token`),
  KEY `social_auth_partial_timestamp_50f2119f` (`timestamp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_auth_partial`
--

LOCK TABLES `social_auth_partial` WRITE;
/*!40000 ALTER TABLE `social_auth_partial` DISABLE KEYS */;
/*!40000 ALTER TABLE `social_auth_partial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_auth_usersocialauth`
--

DROP TABLE IF EXISTS `social_auth_usersocialauth`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `social_auth_usersocialauth` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `provider` varchar(32) NOT NULL,
  `uid` varchar(255) NOT NULL,
  `extra_data` longtext NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `social_auth_usersocialauth_provider_uid_e6b5e668_uniq` (`provider`,`uid`),
  KEY `social_auth_usersocialauth_user_id_17d28448_fk_auth_user_id` (`user_id`),
  CONSTRAINT `social_auth_usersocialauth_user_id_17d28448_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_auth_usersocialauth`
--

LOCK TABLES `social_auth_usersocialauth` WRITE;
/*!40000 ALTER TABLE `social_auth_usersocialauth` DISABLE KEYS */;
/*!40000 ALTER TABLE `social_auth_usersocialauth` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticket`
--

DROP TABLE IF EXISTS `ticket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ticket` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `surplus` int(11) NOT NULL,
  `unit_price` int(11) NOT NULL,
  `scheme_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ticket_scheme_id_91258d79_fk_scheme_id` (`scheme_id`),
  CONSTRAINT `ticket_scheme_id_91258d79_fk_scheme_id` FOREIGN KEY (`scheme_id`) REFERENCES `scheme` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticket`
--

LOCK TABLES `ticket` WRITE;
/*!40000 ALTER TABLE `ticket` DISABLE KEYS */;
INSERT INTO `ticket` VALUES (4,'2019-04-30','2019-05-05',566,2299,1),(5,'2019-05-03','2019-04-08',567,2889,1),(6,'2019-05-01','2019-05-06',223,3899,1);
/*!40000 ALTER TABLE `ticket` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-24  0:09:27
