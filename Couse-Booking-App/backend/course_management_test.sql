-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 16, 2024 at 08:55 PM
-- Server version: 11.5.2-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `course_management_test`
--

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

CREATE TABLE `course` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `course_image_url` varchar(200) NOT NULL,
  `max_members` int(11) NOT NULL,
  `language` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `course`
--

INSERT INTO `course` (`id`, `name`, `course_image_url`, `max_members`, `language`) VALUES
(1, 'English language', 'url_slike_engleski.jpg', 30, 'english'),
(2, 'Serbian language', 'url_slike_srpski.jpg', 30, 'serbian'),
(3, 'Bulgarian language', 'url_slike_francuski.jpg', 30, 'bulgarian');

-- --------------------------------------------------------

--
-- Table structure for table `current_courses`
--

CREATE TABLE `current_courses` (
  `id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `price` int(11) NOT NULL,
  `duration` int(11) NOT NULL,
  `start_at` timestamp NOT NULL,
  `end_at` timestamp NOT NULL,
  `status` varchar(200) NOT NULL,
  `level` varchar(200) NOT NULL,
  `location` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `current_courses`
--

INSERT INTO `current_courses` (`id`, `course_id`, `user_id`, `price`, `duration`, `start_at`, `end_at`, `status`, `level`, `location`) VALUES
(1, 1, 3, 100, 30, '2025-01-20 08:00:00', '2024-12-20 12:00:00', 'active', 'Beginner', 'classroom 101'),
(2, 2, 6, 150, 60, '2024-01-19 23:00:00', '2024-03-19 23:00:00', 'active', 'Intermediate', 'classroom 103'),
(3, 3, 7, 120, 30, '2024-03-02 23:00:00', '2024-04-01 22:00:00', 'pending', 'Advanced', 'classroom 101'),
(4, 2, 6, 150, 30, '2024-01-22 23:00:00', '2024-02-22 23:00:00', 'active', 'Beginner', 'classroom 104'),
(5, 1, 3, 100, 30, '2024-02-25 23:00:00', '2024-03-25 23:00:00', 'active', 'Advanced', 'classroom 100');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `first_name` varchar(200) NOT NULL,
  `last_name` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `phone_number` int(11) DEFAULT NULL,
  `biography` text DEFAULT NULL,
  `user_image_url` varchar(200) DEFAULT NULL,
  `password_hash` varchar(300) NOT NULL,
  `rola` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `first_name`, `last_name`, `email`, `phone_number`, `biography`, `user_image_url`, `password_hash`, `rola`) VALUES
(1, 'Marko', 'Marković', 'marko.markovic@example.com', 641234567, NULL, 'url_slike_1.jpg', 'hash_lozinke_1', 'user'),
(2, 'Ana', 'Anić', 'ana.anic@example.com', 659876543, NULL, 'url_slike_2.jpg', 'hash_lozinke_2', 'admin'),
(3, 'Petar', 'Petrović', 'petar.petrovic@example.com', 635554444, 'Profesor engleskog jezika sa iskustvom od 10 godina.', 'url_slike_3.jpg', 'hash_lozinke_3', 'professor'),
(4, 'Mila', 'Milić', 'mila.milic@example.com', 614443333, NULL, NULL, 'hash_lozinke_4', 'user'),
(5, 'Jovan', 'Jovanović', 'jovan.jovanovic@example.com', 693332222, NULL, 'url_slike_5.jpg', 'hash_lozinke_5', 'admin'),
(6, 'Ivan', 'Ivić', 'ivan.ivic@example.com', 622221111, 'Profesor srpskog jezika, specijalizovan za poslovnu komunikaciju.', 'url_slike_6.jpg', 'hash_lozinke_6', 'professor'),
(7, 'Sara', 'Sarić', 'sara.saric@example.com', 601119999, 'Profesorka englskog jezika sa fokusom na konverzacijske veštine.', 'url_slike_7.jpg', 'hash_lozinke_7', 'professor');

-- --------------------------------------------------------

--
-- Table structure for table `user_course`
--

CREATE TABLE `user_course` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user_course`
--

INSERT INTO `user_course` (`id`, `user_id`, `course_id`) VALUES
(1, 1, 1),
(2, 2, 3),
(3, 4, 2),
(4, 4, 1),
(5, 5, 1),
(6, 4, 5),
(7, 3, 5),
(8, 3, 4),
(9, 1, 5),
(10, 3, 1),
(11, 2, 5);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `course`
--
ALTER TABLE `course`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `current_courses`
--
ALTER TABLE `current_courses`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_professor` (`user_id`),
  ADD KEY `fk_course_c` (`course_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_course`
--
ALTER TABLE `user_course`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_user` (`user_id`),
  ADD KEY `fk_course` (`course_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `course`
--
ALTER TABLE `course`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `current_courses`
--
ALTER TABLE `current_courses`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `user_course`
--
ALTER TABLE `user_course`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `current_courses`
--
ALTER TABLE `current_courses`
  ADD CONSTRAINT `fk_course_c` FOREIGN KEY (`course_id`) REFERENCES `course` (`id`);

--
-- Constraints for table `user_course`
--
ALTER TABLE `user_course`
  ADD CONSTRAINT `fk_course` FOREIGN KEY (`course_id`) REFERENCES `current_courses` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
