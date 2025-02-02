-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 31, 2025 at 09:46 PM
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
  `language` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `course`
--

INSERT INTO `course` (`id`, `name`, `course_image_url`, `language`) VALUES
(1, 'English language', 'http://127.0.0.1:5000/uploads/course/english.png', 'english'),
(2, 'French language', 'http://127.0.0.1:5000/uploads/course/french.png', 'french'),
(15, 'Serbian Language', 'http://127.0.0.1:5000/uploads/course/serbia-4613152_1280.jpg', 'serbian');

-- --------------------------------------------------------

--
-- Table structure for table `current_courses`
--

CREATE TABLE `current_courses` (
  `id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `price` int(11) NOT NULL,
  `start_at` timestamp NOT NULL,
  `end_at` timestamp NOT NULL,
  `level` varchar(200) NOT NULL,
  `location` varchar(200) NOT NULL,
  `max_members` int(11) NOT NULL,
  `lessons` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `current_courses`
--

INSERT INTO `current_courses` (`id`, `course_id`, `user_id`, `price`, `start_at`, `end_at`, `level`, `location`, `max_members`, `lessons`) VALUES
(1, 1, 3, 150, '2025-04-05 22:00:00', '2025-04-25 22:00:00', 'advanced', 'Classroom 30', 20, 20),
(2, 2, 6, 140, '2025-02-26 23:00:00', '2025-03-12 23:00:00', 'intermediate', 'classroom 34', 40, 25),
(3, 1, 7, 120, '2025-03-18 23:00:00', '2025-04-29 22:00:00', 'advanced', 'classroom 101', 2, 20),
(4, 2, 8, 150, '2025-01-18 16:13:40', '2025-01-18 16:13:40', 'beginner', 'classroom 104', 15, 20),
(5, 2, 9, 100, '2025-03-31 22:00:00', '2025-04-25 22:00:00', 'advanced', 'classroom 100', 15, 40),
(21, 13, 8, 1, '2025-03-16 12:55:00', '2025-04-26 22:00:00', 'beginner', 'Serbian ', 20, 0),
(22, 13, 3, 1, '2025-01-08 12:00:00', '2025-01-19 23:00:00', 'advanced', 'Serbian ', 20, 9),
(23, 13, 7, 1, '2025-03-26 14:21:00', '2025-04-15 22:00:00', 'beginner', 'Serbian ', 20, 12),
(26, 15, 9, 1, '2025-04-21 19:07:00', '2025-05-24 22:00:00', 'beginner', 'Classroom 30', 25, 10);

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
(1, 'Marko', 'Markovic', 'marko.markovic@example.com', 345679567, '', 'http://127.0.0.1:5000/uploads/user/anonymous.png', 'scrypt:32768:8:1$m2u8QWXosxBjorhX$d501353545e39192e59ebc9ea03aada31e43900f907a3c6fd693aa39669c9de726733b3827fe9fc83626b08d94df40e1e241234b42cca80c92b4562304dda706', 'user'),
(2, 'Ana', 'Anić', 'ana.anic@example.com', 987654321, '', 'http://127.0.0.1:5000/uploads/user/anaanic2.jpg', 'scrypt:32768:8:1$Zgc2DKlDIM4cS20K$e8abe3007829bdf1e6b63618b9fff98385a16b671d87dbe5ad11f3fafd6be17071340f30db5d4ac0cb9778d0c8fded26548b9f6c465a4517ee340664e63a7002', 'admin'),
(3, 'Petar', 'Petrović', 'petar.petrovic@example.com', 123456789, 'Petar Petrović is an experienced English language teacher with over 10 years of experience in teaching. He is passionate about helping students improve their language skills and develop a love for learning.', 'http://127.0.0.1:5000/uploads/user/petarpetrovic3.jpg', 'scrypt:32768:8:1$BAroIgn7LFP8gMm6$749603d7695b3ca58d5c86e58061889bb047f788f9f89f3165780d927589a3ed0edb2cd1e8880f6cc740aef0caf5494dfc17c4fd1506d2048202080996452cac', 'professor'),
(4, 'Mila', 'Milic', 'mila.milic@example.com', 34567993, '', 'http://127.0.0.1:5000/uploads/user/milamilic4.jpg', 'scrypt:32768:8:1$ujnOe1Pu3Nw7runQ$27233a4f9778d193251b118d4698b1eaf04d8b5009549b8fc25870b62ef3a5c6fc4fbe9ec20c34023134d5a6fed86cfe5d7ff5d3d1be36917d96e3362b686c4d', 'user'),
(5, 'Jovan', 'Jovanović', 'jovan.jovanovic@example.com', 987654321, '', 'http://127.0.0.1:5000/uploads/user/anonymous.png', 'scrypt:32768:8:1$BiUtdQz2jwcl0e3i$f7b6b26f3be36d2ed622113fb056aeece39035abd46f8a136002580571cae76c4e195c43434b8325c5fb278ab865c0ed4e748bb87c220a05fe2c7f1dd1f9a864', 'admin'),
(6, 'Ivan', 'Ivić', 'ivan.ivic@example.com', 555123456, 'Ivan Ivić is a dedicated professor of French language, passionate about teaching and helping students understand the nuances of the French language and culture.', 'http://127.0.0.1:5000/uploads/user/ivanivic6.jpg', 'scrypt:32768:8:1$IMQYGPN8jiUycaNM$20f8abc2cd689e1b7264ebe8160e11fade2cb8af3969d67c2cc88845d5812b6d97ca7127959cd2f0f556475b8fe57aa48900dad15f92e3de357927534f94f9d4', 'professor'),
(7, 'Sara', 'Šarić', 'sara.saric@example.com', 654321987, 'Sara Šarić is a dedicated professor of English, passionate about teaching language skills and fostering a love for literature among her students.', 'http://127.0.0.1:5000/uploads/user/sarasaric7.jpg', 'scrypt:32768:8:1$kJ1gDJ7Nl0pKbLYq$8e85865eb926de4d5c2a9365ec00d98a525650b58dcfc57a1cbde03dbcea5b777c9528393215a5a18432c6c53002550a8021715dff8ff810e7163acc4f246328', 'professor'),
(8, 'Jovana', 'Donova', 'jovana.donova@example.com', 321654987, 'Jovana Donova is an enthusiastic French teacher, dedicated to helping students improve their language skills and explore the richness of French literature.', 'http://127.0.0.1:5000/uploads/user/jovanadonova8.jpg', 'scrypt:32768:8:1$56WBdQYzjorFquUc$066a29611fd79cd3307492566e0a9e186f2cdb90766e7dc13337e43b7edccdac3bfab02b29eee54fd5e944e14c64fc68b37a807e43f198d0824fc8c65d5388be', 'professor'),
(9, 'Mila', 'Ilić', 'mila.ilic@example.com', 123987654, 'Mila Ilić is a passionate professor of French language, dedicated to teaching students the complexities of the French language and culture.', 'http://127.0.0.1:5000/uploads/user/milailic9.jpg', 'scrypt:32768:8:1$hdtjfjS7arO8lRjI$1ae0b2f482d56a3349f73dcfd70533ec6f259a621d90c74c09b90a907dc004287fb1a389605af2172190bce59c3f6456f6a91c81aa4b6e46f167c5d1da52e05d', 'professor'),
(12, 'Bojana', 'Bojanovic', 'bojana.bojanovic@example.com', 0, '', 'http://127.0.0.1:5000/uploads/user/bojana12.jpeg', 'scrypt:32768:8:1$yUsBzg2OjWWO8cwr$d7d663f3e5c1f6a7b9f836afbda4ca8cca938cda872fb3b966812e7b43af6378ec8d0480bfc4f988983d0b183b30e36007bf5e2770b1eb877df172fa370062af', 'user'),
(13, 'Jovana', 'Tomic', 'jovana.tomic@example.com', 381, '', 'http://127.0.0.1:5000/uploads/user/anonymous.png', 'scrypt:32768:8:1$4dWCuSHc4OkSw40W$1a292c141a4aca6c1561b84f14ead063c4242dff54515490ae095a93caf571ed0ab1622544d34d46f04930b964495f91c9db33cfdb03b4fcb06a8143f86eaa6c', 'user'),
(14, 'Gordana', 'Prokic', 'gordana.prokic@example.com', 2147483647, '', 'http://127.0.0.1:5000/uploads/user/gordanaprokic14.jpg', 'scrypt:32768:8:1$T1lDeiCegEnrnfzO$60091a607e667a41cbc22cdd8e91c9e8967aad680e897a23334aea9a573283b3fd81eb466ff776afb5637a37c568780f80a4fe9b94ef27496b6fc12acb58b66a', 'user'),
(15, 'Aleksandar', 'Stefanov', 'aleksandar.stefanov@example.com', 2147483647, '', 'http://127.0.0.1:5000/uploads/user/anonymous.png', 'scrypt:32768:8:1$icTdVj7SYBxUiRs4$a686af7060e66657a2f71623585dc1c498d378a2e82bf3bce8c8b975208992011683ae9ba7517a61205f1f343faec839f95a27f0a81859146ca6b1adac9c513d', 'user');

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
(24, 4, 1),
(5, 5, 1),
(17, 12, 1),
(21, 12, 2);

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
  ADD KEY `fk_user` (`user_id`),
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
  ADD UNIQUE KEY `unique_user_course` (`user_id`,`course_id`),
  ADD KEY `fk_course` (`course_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `course`
--
ALTER TABLE `course`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `current_courses`
--
ALTER TABLE `current_courses`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;

--
-- AUTO_INCREMENT for table `user_course`
--
ALTER TABLE `user_course`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
