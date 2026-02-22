-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 22, 2026 at 09:59 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

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
(1, 'english language', 'english.png', 'english'),
(2, 'french language', 'french.png', 'french'),
(15, 'spanish language', 'spanish.png', 'spanish'),
(44, 'serbian languagee', '0a149355-709a-4278-992a-fb8f155e0a93.jpg', 'serbiann');

-- --------------------------------------------------------

--
-- Table structure for table `current_courses`
--

CREATE TABLE `current_courses` (
  `id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `price` int(11) NOT NULL,
  `start_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `end_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `level` varchar(200) NOT NULL,
  `location` varchar(200) NOT NULL,
  `max_members` int(11) NOT NULL,
  `lessons` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `current_courses`
--

INSERT INTO `current_courses` (`id`, `course_id`, `user_id`, `price`, `start_at`, `end_at`, `level`, `location`, `max_members`, `lessons`) VALUES
(2, 2, 6, 140, '2025-11-21 02:00:00', '2027-05-12 22:00:00', 'intermediate', 'classroom 34', 40, 25),
(5, 2, 9, 100, '2026-02-05 06:00:00', '2026-09-25 22:00:00', 'advanced', 'classroom 100', 17, 40),
(21, 13, 8, 1, '2025-03-16 12:55:00', '2025-04-26 22:00:00', 'beginner', 'Serbian ', 20, 0),
(22, 13, 3, 1, '2025-01-08 12:00:00', '2025-01-19 23:00:00', 'advanced', 'Serbian ', 20, 9),
(23, 13, 7, 1, '2025-03-26 14:21:00', '2025-04-15 22:00:00', 'beginner', 'Serbian ', 20, 12),
(26, 15, 9, 100, '2025-12-28 03:09:00', '2026-04-09 22:00:00', 'beginner', 'Classroom 30', 25, 10),
(33, 15, 7, 120, '2026-01-12 07:00:00', '2026-03-15 23:00:00', 'advanced', 'classroom 104', 20, 40),
(36, 15, 3, 140, '2026-01-26 16:25:00', '2026-01-30 23:00:00', 'beginner', 'classroom 101', 4, 10),
(37, 2, 8, 12, '2026-03-31 19:42:00', '2026-07-26 22:00:00', 'intermediate', 'Classroom 30', 20, 12),
(38, 1, 8, 120, '2026-02-28 23:00:00', '2026-04-09 22:00:00', 'beginner', 'Niš', 15, 20),
(40, 2, 3, 120, '2026-02-28 21:05:00', '2026-03-24 23:00:00', 'intermediate', 'classroom 34', 4, 12),
(41, 44, 9, 140, '2026-02-23 00:28:00', '2026-04-26 22:00:00', 'advanced', 'classroom 101', 12, 12);

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
(1, 'Marko', 'Markovic', 'marko.markovic@example.com', 0, '', 'http://127.0.0.1:5000/uploads/user/anonymous.png', 'scrypt:32768:8:1$m2u8QWXosxBjorhX$d501353545e39192e59ebc9ea03aada31e43900f907a3c6fd693aa39669c9de726733b3827fe9fc83626b08d94df40e1e241234b42cca80c92b4562304dda706', 'user'),
(2, 'Ana', 'Anić', 'ana.anic@example.com', 987654321, '', 'http://127.0.0.1:5000/uploads/user/anaanic2.jpg', 'scrypt:32768:8:1$Zgc2DKlDIM4cS20K$e8abe3007829bdf1e6b63618b9fff98385a16b671d87dbe5ad11f3fafd6be17071340f30db5d4ac0cb9778d0c8fded26548b9f6c465a4517ee340664e63a7002', 'admin'),
(3, 'Petar', 'Petrović', 'petar.petrovic@example.com', 123456789, 'Petar Petrović is an experienced English language teacher with over 10 years of experience in teaching. He is passionate about helping students improve their language skills and develop a love for learning.', 'http://127.0.0.1:5000/uploads/user/petarpetrovic3.jpg', 'scrypt:32768:8:1$BAroIgn7LFP8gMm6$749603d7695b3ca58d5c86e58061889bb047f788f9f89f3165780d927589a3ed0edb2cd1e8880f6cc740aef0caf5494dfc17c4fd1506d2048202080996452cac', 'professor'),
(4, 'Mila', 'Milic', 'mila.milic@example.com', 0, '', 'http://127.0.0.1:5000/uploads/user/milamilic4.jpg', 'scrypt:32768:8:1$ujnOe1Pu3Nw7runQ$27233a4f9778d193251b118d4698b1eaf04d8b5009549b8fc25870b62ef3a5c6fc4fbe9ec20c34023134d5a6fed86cfe5d7ff5d3d1be36917d96e3362b686c4d', 'user'),
(5, 'Jovan', 'Jovanovic', 'jovan.jovanovic@example.com', 0, '', 'http://127.0.0.1:5000/uploads/user/anonymous.png', 'scrypt:32768:8:1$BiUtdQz2jwcl0e3i$f7b6b26f3be36d2ed622113fb056aeece39035abd46f8a136002580571cae76c4e195c43434b8325c5fb278ab865c0ed4e748bb87c220a05fe2c7f1dd1f9a864', 'admin'),
(6, 'Ivana', 'Ivić', 'ivan.ivic@example.com', 555123456, 'Ivana Ivić is a dedicated professor of French language, passionate about teaching and helping students understand the nuances of the French language and culture.', 'http://127.0.0.1:5000/uploads/user/download.jpg', 'scrypt:32768:8:1$IMQYGPN8jiUycaNM$20f8abc2cd689e1b7264ebe8160e11fade2cb8af3969d67c2cc88845d5812b6d97ca7127959cd2f0f556475b8fe57aa48900dad15f92e3de357927534f94f9d4', 'professor'),
(7, 'Sara', 'Šarić', 'sara.saric@example.com', 654321987, 'Sara Šarić is a dedicated professor of English, passionate about teaching language skills and fostering a love for literature among her students.', 'http://127.0.0.1:5000/uploads/user/sarasaric7.jpg', 'scrypt:32768:8:1$kJ1gDJ7Nl0pKbLYq$8e85865eb926de4d5c2a9365ec00d98a525650b58dcfc57a1cbde03dbcea5b777c9528393215a5a18432c6c53002550a8021715dff8ff810e7163acc4f246328', 'professor'),
(8, 'Jovana', 'Donova', 'jovana.donova@example.com', 321654987, 'Jovana Donova is an enthusiastic French teacher, dedicated to helping students improve their language skills and explore the richness of French literature.', 'http://127.0.0.1:5000/uploads/user/jovanadonova8.jpg', 'scrypt:32768:8:1$56WBdQYzjorFquUc$066a29611fd79cd3307492566e0a9e186f2cdb90766e7dc13337e43b7edccdac3bfab02b29eee54fd5e944e14c64fc68b37a807e43f198d0824fc8c65d5388be', 'professor'),
(9, 'Mila', 'Ilić', 'mila.ilic@example.com', 123987654, 'Mila Ilić is a passionate professor of French language, dedicated to teaching students the complexities of the French language and culture.', 'http://127.0.0.1:5000/uploads/user/milailic9.jpg', 'scrypt:32768:8:1$hdtjfjS7arO8lRjI$1ae0b2f482d56a3349f73dcfd70533ec6f259a621d90c74c09b90a907dc004287fb1a389605af2172190bce59c3f6456f6a91c81aa4b6e46f167c5d1da52e05d', 'professor'),
(13, 'Jovana', 'Tomic', 'jovana.tomic@example.com', 381, '', 'http://127.0.0.1:5000/uploads/user/anonymous.png', 'scrypt:32768:8:1$4dWCuSHc4OkSw40W$1a292c141a4aca6c1561b84f14ead063c4242dff54515490ae095a93caf571ed0ab1622544d34d46f04930b964495f91c9db33cfdb03b4fcb06a8143f86eaa6c', 'user'),
(14, 'Gordana', 'Prokic', 'gordana.prokic@example.com', 2147483647, '', 'http://127.0.0.1:5000/uploads/user/gordanaprokic14.jpg', 'scrypt:32768:8:1$T1lDeiCegEnrnfzO$60091a607e667a41cbc22cdd8e91c9e8967aad680e897a23334aea9a573283b3fd81eb466ff776afb5637a37c568780f80a4fe9b94ef27496b6fc12acb58b66a', 'user'),
(48, 'Jovanna', 'Milic', 'test@mail.com', 381, 'undefined', 'http://127.0.0.1:5000/uploads/user/download48.jpg', 'scrypt:32768:8:1$JxAE2Ml67dqVhjZ3$c982ba2c98c41643c98d43b2dab2268a58221f7d048b7514b2af7854d3215c6ce77857ec6ad0ea8369f04c5e26a818d7ccb7dcfe5bf64ac7d2af2846adfd7f2a', 'admin'),
(50, 'Mila', 'Last name test', 'm@gmail.com', 381333, 'undefined', 'http://127.0.0.1:5000/uploads/user/anonymous.png', 'scrypt:32768:8:1$iZ4ptYYSwJTiLeAR$ba13e2151f1e1871c01492ccdb2473b9f0c25b029be97168eb70d1d48c1970a8bae037f7ceeff9fa6d8b00c3ea74958df8c7d06fff056634ffc6cc567908aa96', 'user'),
(51, 'Anci ', 'Vl', 'andrijana@example.com', 611234567, NULL, 'http://127.0.0.1:5000/uploads/user/anonymous.png', 'scrypt:32768:8:1$RbmKyJZvoXucyDre$1c54572efff64b46f2925e83ce4ea301937337876024ee4e20151439ee356807af3ce5919f66bc240507711b00cba7c187cef738c9dcd15a3abf1f6fb4452fb3', 'user'),
(52, '', 'Vl', 'andrijana2@example.com', 611234567, NULL, 'http://127.0.0.1:5000/uploads/user/anonymous.png', 'scrypt:32768:8:1$ZcD4kEcXOJIOBRkn$10f984fa97368109c4dca7d799a986f73ae6b097510ca423bdc22915267da84881b9886ce86dec6746625361d2c569bae602d930a115f63d3beab04517cdbb47', 'user'),
(53, 'Ana', 'Vl', 'andrijana23@example.com', 611234567, 'some info', 'http://127.0.0.1:5000/uploads/user/2e288bff-a4c3-4b47-9efd-91f958576dba.png', 'scrypt:32768:8:1$sm2j8uaxYCeMWikA$30c1114a667429eb9bfba930a1e63b0b9a5f9109286b9efe4869141bbd356af266b58a2924139e72e0e9ee225cad06e4a59be43cfa7785d061b39297a9ee827c', 'professor');

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT for table `current_courses`
--
ALTER TABLE `current_courses`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=56;

--
-- AUTO_INCREMENT for table `user_course`
--
ALTER TABLE `user_course`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
