/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 80023
Source Host           : localhost:3306
Source Database       : registration_system

Target Server Type    : MYSQL
Target Server Version : 80023
File Encoding         : 65001

Date: 2022-12-14 21:50:24
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for achievement_cuber_222
-- ----------------------------
DROP TABLE IF EXISTS `achievement_cuber_222`;
CREATE TABLE `achievement_cuber_222` (
  `id` int NOT NULL AUTO_INCREMENT,
  `t1` float DEFAULT NULL,
  `t2` float DEFAULT NULL,
  `t3` float DEFAULT NULL,
  `t4` float DEFAULT NULL,
  `t5` float DEFAULT NULL,
  `best` float DEFAULT NULL,
  `ao5` float DEFAULT NULL,
  `competition_options` varchar(10) DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  `match_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `match_id` (`match_id`),
  CONSTRAINT `achievement_cuber_222_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `achievement_cuber_222_ibfk_3` FOREIGN KEY (`match_id`) REFERENCES `competition_information` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for achievement_cuber_333
-- ----------------------------
DROP TABLE IF EXISTS `achievement_cuber_333`;
CREATE TABLE `achievement_cuber_333` (
  `id` int NOT NULL AUTO_INCREMENT,
  `t1` float DEFAULT NULL,
  `t2` float DEFAULT NULL,
  `t3` float DEFAULT NULL,
  `t4` float DEFAULT NULL,
  `t5` float DEFAULT NULL,
  `best` float DEFAULT NULL,
  `ao5` float DEFAULT NULL,
  `competition_options` varchar(10) DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  `match_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `match_id` (`match_id`),
  CONSTRAINT `achievement_cuber_333_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `achievement_cuber_333_ibfk_3` FOREIGN KEY (`match_id`) REFERENCES `competition_information` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=141 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for achievement_cuber_oh
-- ----------------------------
DROP TABLE IF EXISTS `achievement_cuber_oh`;
CREATE TABLE `achievement_cuber_oh` (
  `id` int NOT NULL AUTO_INCREMENT,
  `t1` float DEFAULT NULL,
  `t2` float DEFAULT NULL,
  `t3` float DEFAULT NULL,
  `t4` float DEFAULT NULL,
  `t5` float DEFAULT NULL,
  `best` float DEFAULT NULL,
  `ao5` float DEFAULT NULL,
  `competition_options` varchar(10) DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  `match_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `match_id` (`match_id`),
  CONSTRAINT `achievement_cuber_oh_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `achievement_cuber_oh_ibfk_3` FOREIGN KEY (`match_id`) REFERENCES `competition_information` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for achievement_cuber_py
-- ----------------------------
DROP TABLE IF EXISTS `achievement_cuber_py`;
CREATE TABLE `achievement_cuber_py` (
  `id` int NOT NULL AUTO_INCREMENT,
  `t1` float DEFAULT NULL,
  `t2` float DEFAULT NULL,
  `t3` float DEFAULT NULL,
  `t4` float DEFAULT NULL,
  `t5` float DEFAULT NULL,
  `best` float DEFAULT NULL,
  `ao5` float DEFAULT NULL,
  `competition_options` varchar(10) DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  `match_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `match_id` (`match_id`),
  CONSTRAINT `achievement_cuber_py_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `achievement_cuber_py_ibfk_3` FOREIGN KEY (`match_id`) REFERENCES `competition_information` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for achievement_cuber_sk
-- ----------------------------
DROP TABLE IF EXISTS `achievement_cuber_sk`;
CREATE TABLE `achievement_cuber_sk` (
  `id` int NOT NULL AUTO_INCREMENT,
  `t1` float DEFAULT NULL,
  `t2` float DEFAULT NULL,
  `t3` float DEFAULT NULL,
  `t4` float DEFAULT NULL,
  `t5` float DEFAULT NULL,
  `best` float DEFAULT NULL,
  `ao5` float DEFAULT NULL,
  `competition_options` varchar(10) DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  `match_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `match_id` (`match_id`),
  CONSTRAINT `achievement_cuber_sk_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `achievement_cuber_sk_ibfk_3` FOREIGN KEY (`match_id`) REFERENCES `competition_information` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for achievement_table
-- ----------------------------
DROP TABLE IF EXISTS `achievement_table`;
CREATE TABLE `achievement_table` (
  `id` int NOT NULL AUTO_INCREMENT,
  `address` varchar(150) NOT NULL,
  `match_name` varchar(200) NOT NULL,
  `match_time` date NOT NULL,
  `match_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `match_id` (`match_id`),
  CONSTRAINT `achievement_table_ibfk_1` FOREIGN KEY (`match_id`) REFERENCES `competition_information` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for alembic_version
-- ----------------------------
DROP TABLE IF EXISTS `alembic_version`;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for competition_information
-- ----------------------------
DROP TABLE IF EXISTS `competition_information`;
CREATE TABLE `competition_information` (
  `id` int NOT NULL AUTO_INCREMENT,
  `match_time` date NOT NULL,
  `address` varchar(300) NOT NULL,
  `number_of_applicants` varchar(4) NOT NULL,
  `project_opening` varchar(500) NOT NULL,
  `registration_fee` varchar(4) DEFAULT NULL,
  `registration_end_time` date NOT NULL,
  `match_name` varchar(200) NOT NULL,
  `details` text,
  `enter_status` int DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  `item_registration_free` varchar(4) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `competition_information_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=88 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for home_banner
-- ----------------------------
DROP TABLE IF EXISTS `home_banner`;
CREATE TABLE `home_banner` (
  `id` int NOT NULL AUTO_INCREMENT,
  `image_route` text,
  `add_time` datetime DEFAULT NULL,
  `index` int DEFAULT NULL,
  `match_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `match_id` (`match_id`),
  CONSTRAINT `home_banner_ibfk_1` FOREIGN KEY (`match_id`) REFERENCES `competition_information` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for index_article
-- ----------------------------
DROP TABLE IF EXISTS `index_article`;
CREATE TABLE `index_article` (
  `id` int NOT NULL AUTO_INCREMENT,
  `release_time` date NOT NULL,
  `title` varchar(120) NOT NULL,
  `user_id` int DEFAULT NULL,
  `content` text NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `index_article_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for oder_info
-- ----------------------------
DROP TABLE IF EXISTS `oder_info`;
CREATE TABLE `oder_info` (
  `id` int NOT NULL AUTO_INCREMENT,
  `oder_id` int DEFAULT NULL,
  `add_time` datetime DEFAULT NULL,
  `amount` varchar(10) DEFAULT NULL,
  `match_id` int DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `add_time` (`add_time`),
  KEY `user_id` (`user_id`),
  KEY `match_id` (`match_id`),
  CONSTRAINT `oder_info_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `oder_info_ibfk_2` FOREIGN KEY (`match_id`) REFERENCES `competition_information` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for player_information
-- ----------------------------
DROP TABLE IF EXISTS `player_information`;
CREATE TABLE `player_information` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(5) NOT NULL,
  `mobile` varchar(11) NOT NULL,
  `registration_items` varchar(50) NOT NULL,
  `match_id` int DEFAULT NULL,
  `add_time` datetime DEFAULT NULL,
  `birthday` date NOT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `match_id` (`match_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `player_information_ibfk_1` FOREIGN KEY (`match_id`) REFERENCES `competition_information` (`id`),
  CONSTRAINT `player_information_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=170 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `name` varchar(20) NOT NULL,
  `status` int DEFAULT NULL,
  `is_super` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `sex` varchar(16) DEFAULT NULL,
  `hash_password` varchar(512) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for user_confidentiality
-- ----------------------------
DROP TABLE IF EXISTS `user_confidentiality`;
CREATE TABLE `user_confidentiality` (
  `id` int NOT NULL AUTO_INCREMENT,
  `confidentiality_question` text,
  `confidentiality_answer` text,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `user_confidentiality_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for user_login_history
-- ----------------------------
DROP TABLE IF EXISTS `user_login_history`;
CREATE TABLE `user_login_history` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(64) NOT NULL,
  `ip` varchar(32) DEFAULT NULL,
  `ua` varchar(512) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `user_login_history_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=240 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for user_profile
-- ----------------------------
DROP TABLE IF EXISTS `user_profile`;
CREATE TABLE `user_profile` (
  `id` int NOT NULL AUTO_INCREMENT,
  `avatar` varchar(256) DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `user_profile_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8;
