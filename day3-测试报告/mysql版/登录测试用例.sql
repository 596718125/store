/*
SQLyog Enterprise v12.5.0 (64 bit)
MySQL - 5.6.24 : Database - hkr
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`hkr` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `hkr`;

/*Table structure for table `data_error` */

DROP TABLE IF EXISTS `data_error`;

CREATE TABLE `data_error` (
  `username` char(20) NOT NULL,
  `password` char(20) DEFAULT NULL,
  `expect` char(100) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `data_error` */

insert  into `data_error`(`username`,`password`,`expect`) values 
('admin','admin','账户名错误或密码错误!别瞎弄!'),
('jason','root','账户名错误或密码错误!别瞎弄!'),
('不再爱了','root123','账户名错误或密码错误!别瞎弄!');

/*Table structure for table `data_success` */

DROP TABLE IF EXISTS `data_success`;

CREATE TABLE `data_success` (
  `username` char(20) NOT NULL,
  `password` char(20) DEFAULT NULL,
  `expect` char(100) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `data_success` */

insert  into `data_success`(`username`,`password`,`expect`) values 
('jason','1234567','Student Login'),
('root','root','Student Login'),
('xiao','123456','Student Login');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
