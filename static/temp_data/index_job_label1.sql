-- phpMyAdmin SQL Dump
-- version 4.6.6
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: 2018-11-13 09:52:31
-- 服务器版本： 5.6.30
-- PHP Version: 7.1.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `recruit4`
--

-- --------------------------------------------------------

--
-- 表的结构 `index_job_label1`
--
--
-- 转存表中的数据 `index_job_label1`
--

INSERT INTO `index_job_label1` (`id`, `name`) VALUES
(1, 'IT互联网'),
(2, '市场商务'),
(3, '电子电气'),
(4, '人事行政'),
(5, '外语外贸'),
(6, '财经法务'),
(7, '媒体设计'),
(8, '教育咨询'),
(9, '其他类型');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `index_job_label1`
--
ALTER TABLE `index_job_label1`
  ADD PRIMARY KEY (`id`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `index_job_label1`
--
ALTER TABLE `index_job_label1`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
