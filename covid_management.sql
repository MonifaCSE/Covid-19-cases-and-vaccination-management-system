-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 02, 2022 at 08:53 PM
-- Server version: 10.1.29-MariaDB
-- PHP Version: 7.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `covid management`
--

-- --------------------------------------------------------

--
-- Table structure for table `bed_allotment`
--

CREATE TABLE `bed_allotment` (
  `Allotment_no` int(50) NOT NULL,
  `Patient_id` int(50) NOT NULL,
  `Bed_id` int(50) NOT NULL,
  `Allotment_date` date NOT NULL,
  `Discharge_date` date NOT NULL,
  `Hospital_id` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bed_allotment`
--

INSERT INTO `bed_allotment` (`Allotment_no`, `Patient_id`, `Bed_id`, `Allotment_date`, `Discharge_date`, `Hospital_id`) VALUES
(6, 10, 1, '2021-12-07', '2021-12-14', 4),
(7, 2, 2, '2021-12-02', '2021-12-19', 4),
(8, 2, 4, '2021-12-31', '2022-01-05', 3),
(9, 3, 5, '2022-01-02', '2022-01-28', 3);

-- --------------------------------------------------------

--
-- Table structure for table `bed_list`
--

CREATE TABLE `bed_list` (
  `Bed_id` int(50) NOT NULL,
  `Bed_category` varchar(255) NOT NULL,
  `Cost` int(255) NOT NULL,
  `Status` varchar(255) NOT NULL,
  `Hospital_id` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bed_list`
--

INSERT INTO `bed_list` (`Bed_id`, `Bed_category`, `Cost`, `Status`, `Hospital_id`) VALUES
(1, 'ICU', 2000, 'Not Available', 4),
(2, 'ICU', 1000, 'Available', 4),
(3, 'CCU', 2000, 'Not Available', 3),
(4, 'Children', 2300, 'Available', 3);

-- --------------------------------------------------------

--
-- Table structure for table `covid_test`
--

CREATE TABLE `covid_test` (
  `id` int(50) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Address` varchar(255) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Phone` varchar(15) NOT NULL,
  `Age_group` varchar(260) NOT NULL,
  `Appointment_date` date NOT NULL,
  `Tested` varchar(255) NOT NULL,
  `Result` varchar(255) NOT NULL,
  `Hospital_id` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `covid_test`
--

INSERT INTO `covid_test` (`id`, `Name`, `Address`, `Email`, `Phone`, `Age_group`, `Appointment_date`, `Tested`, `Result`, `Hospital_id`) VALUES
(1, 'Monifa', 'Chawkbazar', 'monifa@gmail.com', '+8801791662431', '18-25', '2021-12-23', 'Yes', 'Negative', 3),
(4, 'Safa', 'Khulshi', 'rohan@gmail.com', '+8801791662411', '18-25', '2021-12-23', 'Yes', 'Negative', 3),
(6, 'Safa', 'Chawkbazar', 'monifa@gmail.com', '+8801791662431', '41-60', '2021-12-28', 'Yes', 'Positive', 3),
(10, 'Sumaiya', 'Jamal Khan', 'safa@gmail.com', '+8801791662431', '61-80', '2021-12-31', 'No', 'Result', 3),
(11, 'Ripa', 'Bahaddarhat', 'ripa@gmail.com', '+8801791662412', '61-80', '2021-12-31', 'No', 'Result', 3);

-- --------------------------------------------------------

--
-- Table structure for table `detail_patient`
--

CREATE TABLE `detail_patient` (
  `Patient_id` int(50) NOT NULL,
  `Patient_name` varchar(255) NOT NULL,
  `Phone` varchar(15) NOT NULL,
  `Relative_name` varchar(255) NOT NULL,
  `Relative_phone` varchar(15) NOT NULL,
  `Address` varchar(255) NOT NULL,
  `Ailment` varchar(255) NOT NULL,
  `Date` date NOT NULL,
  `Bed_id` int(50) NOT NULL,
  `PCondition` varchar(255) NOT NULL,
  `Doctor_name` varchar(255) NOT NULL,
  `Hospital_id` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `doctor`
--

CREATE TABLE `doctor` (
  `Doctor_id` int(50) NOT NULL,
  `Doctor_name` varchar(255) NOT NULL,
  `Address` varchar(255) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Phone` varchar(15) NOT NULL,
  `Shift` varchar(255) NOT NULL,
  `Status` varchar(255) NOT NULL,
  `Image` varchar(255) NOT NULL,
  `Hospital_id` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `doctor`
--

INSERT INTO `doctor` (`Doctor_id`, `Doctor_name`, `Address`, `Email`, `Phone`, `Shift`, `Status`, `Image`, `Hospital_id`) VALUES
(4, 'sumaiya', 'Bahaddarhat', 's@gmail.com', '+8801791662411', 'Night', 'Active', '2.jpg', 3),
(5, 'Ripa', 'Bahaddarhat', 'ripa@gmail.com', '+8801791662418', 'Day', 'Active', 'OS.png', 3),
(6, 'Monifa ', 'Chawkbazar', 'monifa@gmail.com', '+8801791662418', 'Day', 'Inactive', '1.jpg', 3),
(7, 'Nargis', 'Bahaddarhat', 'nar@gmail.com', '+8801791662411', 'Night', 'Active', 'user.png', 4),
(8, 'Safa', 'Chawkbazar', 'safa@gmail.com', '+8801791662441', 'Night', 'Active', 'user.png', 4);

-- --------------------------------------------------------

--
-- Table structure for table `doctor_salary`
--

CREATE TABLE `doctor_salary` (
  `sno` int(50) NOT NULL,
  `Doctor_id` int(50) NOT NULL,
  `Doctor_name` varchar(255) NOT NULL,
  `Paid_date` date NOT NULL,
  `Month` varchar(255) NOT NULL,
  `Salary` int(255) NOT NULL,
  `Hospital_id` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `doctor_salary`
--

INSERT INTO `doctor_salary` (`sno`, `Doctor_id`, `Doctor_name`, `Paid_date`, `Month`, `Salary`, `Hospital_id`) VALUES
(2, 4, 'sumaiya', '2022-01-01', '2022-01', 20000, 3);

-- --------------------------------------------------------

--
-- Table structure for table `doze1`
--

CREATE TABLE `doze1` (
  `ID` int(50) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Address` varchar(255) NOT NULL,
  `NID` varchar(255) NOT NULL,
  `Phone_number` varchar(15) NOT NULL,
  `Age_group` varchar(255) NOT NULL,
  `Allergies` varchar(255) NOT NULL,
  `Prior_ailments` varchar(255) NOT NULL,
  `Doze_name` varchar(255) NOT NULL,
  `Appointment_date` date NOT NULL,
  `Doze1` varchar(255) NOT NULL,
  `Hospital_id` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `doze1`
--

INSERT INTO `doze1` (`ID`, `Name`, `Address`, `NID`, `Phone_number`, `Age_group`, `Allergies`, `Prior_ailments`, `Doze_name`, `Appointment_date`, `Doze1`, `Hospital_id`) VALUES
(1, 'Monifa', 'Chawkbazar', '0192837', '+8801791662418', '18-25', 'No', 'No', 'Sinopharm', '2021-12-10', 'Taken', 3),
(3, 'Safa', 'Jamal Khan', '101010', '+8801791662411', '18-25', 'Yes', 'Yes', 'Vero Cell', '2021-12-01', 'Taken', 4),
(4, 'Arfat', 'Bahaddarhat', '987654', '+8801791662432', '18-25', 'No', 'Yes', 'Moderna', '2021-12-01', 'Taken', 3),
(5, 'Ripa', 'Bahaddarhat', '9869', '+8801791662411', '18-25', 'Yes', 'No', 'Vero Cell', '2021-12-08', 'Taken', 4),
(6, 'bfj', 'Khulshi', '0192837', '+8801791662431', '26-40', 'Yes', 'No', 'Pfizer', '2021-12-15', 'Taken', 3);

-- --------------------------------------------------------

--
-- Table structure for table `doze2`
--

CREATE TABLE `doze2` (
  `id` int(50) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Address` varchar(255) NOT NULL,
  `NID` varchar(255) NOT NULL,
  `Phone_number` varchar(15) NOT NULL,
  `Age_group` varchar(255) NOT NULL,
  `Allergies` varchar(255) NOT NULL,
  `Prior_ailments` varchar(255) NOT NULL,
  `Doze_name` varchar(255) NOT NULL,
  `Appointment1` date NOT NULL,
  `Doze1` varchar(255) NOT NULL,
  `Appointment2` date NOT NULL,
  `Doze2` varchar(255) NOT NULL,
  `Hospital_id` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `doze2`
--

INSERT INTO `doze2` (`id`, `Name`, `Address`, `NID`, `Phone_number`, `Age_group`, `Allergies`, `Prior_ailments`, `Doze_name`, `Appointment1`, `Doze1`, `Appointment2`, `Doze2`, `Hospital_id`) VALUES
(1, 'Monifa', 'Chawkbazar', '0192837', '+8801791662418', '18-25', 'No', 'No', 'Sinopharm', '2021-12-10', 'Taken', '2021-12-06', 'Taken', 3),
(3, 'Safa', 'Jamal Khan', '101010', '+8801791662411', '18-25', 'Yes', 'Yes', 'Vero Cell', '2021-12-01', 'Taken', '0000-00-00', '', 4),
(4, 'Arfat', 'Bahaddarhat', '987654', '+8801791662432', '18-25', 'No', 'Yes', 'Moderna', '2021-12-01', 'Taken', '2021-12-07', 'Taken', 3),
(5, 'Ripa', 'Bahaddarhat', '9869', '+8801791662411', '18-25', 'Yes', 'No', 'Vero Cell', '2021-12-08', 'Taken', '0000-00-00', '', 4),
(6, 'bfj', 'Khulshi', '0192837', '+8801791662431', '26-40', 'Yes', 'No', 'Pfizer', '2021-12-15', 'Taken', '2021-12-16', 'Taken', 3);

-- --------------------------------------------------------

--
-- Table structure for table `hospital`
--

CREATE TABLE `hospital` (
  `Hospital_id` int(50) NOT NULL,
  `Hospital_name` varchar(255) NOT NULL,
  `District` varchar(255) NOT NULL,
  `Address` varchar(255) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Password` varchar(255) NOT NULL,
  `Phone` varchar(15) NOT NULL,
  `Image` varchar(255) NOT NULL,
  `Ambulance` int(50) NOT NULL,
  `Oxygen` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hospital`
--

INSERT INTO `hospital` (`Hospital_id`, `Hospital_name`, `District`, `Address`, `Email`, `Password`, `Phone`, `Image`, `Ambulance`, `Oxygen`) VALUES
(2, 'Imperial Limited Hospital', 'Chittagong', 'Khulshi', 'ilh@gmail.com', 'ilh', '+8801791662411', 'ready-logo-1024x1001.png', 0, 0),
(3, 'Chittagong Medical College ', 'Chiitagong', 'Chawkbazar', 'cmc@gmail.com', 'cmc', '+8801791662418', 'Chittagong_Medical_University.jpg', 50, 100),
(4, 'Dhaka medical College', 'Dhaka', 'ddddd', 'dmc@gmail.com', 'dmc', '+8801791662411', 'dhaka-medical-college-logo-FAA03AA0BC-seeklogo.com.jpg', 0, 0),
(5, 'Parkview pvt hospital', 'Chittagong', 'Panchlaish', 'pv@gmail.com', 'pv', '+8801791662432', 'plain-black-09.jpg', 0, 0),
(6, 'Rajshahi Medical College', 'Rajshahi', 'malkmm', 'raj@gmail.com', 'raj', '+8801791662441', 'plain-black-09.jpg', 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `hospital_request`
--

CREATE TABLE `hospital_request` (
  `Request_id` int(50) NOT NULL,
  `Hospital_name` varchar(255) NOT NULL,
  `District` varchar(255) NOT NULL,
  `Address` varchar(255) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Password` varchar(255) NOT NULL,
  `Phone` varchar(15) NOT NULL,
  `Image` varchar(255) NOT NULL,
  `Approval` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hospital_request`
--

INSERT INTO `hospital_request` (`Request_id`, `Hospital_name`, `District`, `Address`, `Email`, `Password`, `Phone`, `Image`, `Approval`) VALUES
(1, 'ssssss', 'ssssssss', 'ddddddd', 'rohan@gmail.com', 'sss', '+8801791662432', 'plain-black-09.jpg', 'Approved'),
(3, 'd', 'd', 'd', 'safa@gmail.com', 'd', '+8801791662411', 'plain-black-09.jpg', 'Rejected'),
(4, 'kkkkkkk', 'Chittagong', 'Bahaddarhat', 'kkkk@gmail.com', 'kkk', '+8801791662441', 'plain-black-09.jpg', '');

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

CREATE TABLE `patient` (
  `Patient_id` int(50) NOT NULL,
  `Patient_name` varchar(255) NOT NULL,
  `Phone` varchar(15) NOT NULL,
  `Relative_name` varchar(255) NOT NULL,
  `Relative_phone` varchar(15) NOT NULL,
  `Address` varchar(255) NOT NULL,
  `Ailment` varchar(255) NOT NULL,
  `Date` date NOT NULL,
  `Bed_id` int(50) NOT NULL,
  `Doctor_name` varchar(255) NOT NULL,
  `Pcondition` varchar(255) NOT NULL,
  `Hospital_id` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `patient`
--

INSERT INTO `patient` (`Patient_id`, `Patient_name`, `Phone`, `Relative_name`, `Relative_phone`, `Address`, `Ailment`, `Date`, `Bed_id`, `Doctor_name`, `Pcondition`, `Hospital_id`) VALUES
(2, 'mm', '+8801791662418', 'm', ' +8801791662412', 'Chawkbazar', 'zz', '2021-12-28', 3, 'Ripa', 'Death', 3),
(3, 'dd', '+8801791662441', 'm', ' +8801791662412', 'Khulshi', 'zz', '2021-12-28', 4, 'Ripa', 'Recovering', 3),
(4, 'kk', '+8801791662411', 'm', '+8801791662412', 'Khulshi', 'zz', '2021-12-01', 2, 'sumaiya', 'Discharge', 4),
(6, 'mm', '+8801791662432', 'm', ' +8801791662412', 'Jamal Khan', 'zz', '2021-12-01', 6, 'Safa', 'Recovered', 4);

-- --------------------------------------------------------

--
-- Table structure for table `patient_payment`
--

CREATE TABLE `patient_payment` (
  `Payment_no` int(50) NOT NULL,
  `Patient_id` int(50) NOT NULL,
  `Patient_name` varchar(255) NOT NULL,
  `Total_amount` int(50) NOT NULL,
  `Deposit` int(50) NOT NULL,
  `Due_amount` int(50) NOT NULL,
  `Hospital_id` int(50) NOT NULL,
  `Hospital_name` varchar(260) NOT NULL,
  `Date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `patient_payment`
--

INSERT INTO `patient_payment` (`Payment_no`, `Patient_id`, `Patient_name`, `Total_amount`, `Deposit`, `Due_amount`, `Hospital_id`, `Hospital_name`, `Date`) VALUES
(5, 2, 'mm', 30000, 30000, 0, 3, 'Chittagong Medical College ', '2021-10-10'),
(6, 3, 'dd', 50000, 50000, 0, 3, 'Chittagong Medical College ', '2020-05-03'),
(8, 2, 'mm', 2000, 2000, 0, 3, 'Chittagong Medical College', '2020-10-10'),
(9, 4, 'kk', 30000, 30000, 0, 4, 'Dhaka Medical College', '2022-01-02');

-- --------------------------------------------------------

--
-- Table structure for table `patient_request`
--

CREATE TABLE `patient_request` (
  `sno` int(50) NOT NULL,
  `Patient_name` varchar(255) NOT NULL,
  `Phone` varchar(15) NOT NULL,
  `Relative_name` varchar(255) NOT NULL,
  `Relative_phone` varchar(15) NOT NULL,
  `Address` varchar(255) NOT NULL,
  `Ailment` varchar(255) NOT NULL,
  `Date` date NOT NULL,
  `Bed_id` int(50) NOT NULL,
  `Doctor_name` varchar(255) NOT NULL,
  `Approval` varchar(260) NOT NULL,
  `Hospital_id` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `patient_request`
--

INSERT INTO `patient_request` (`sno`, `Patient_name`, `Phone`, `Relative_name`, `Relative_phone`, `Address`, `Ailment`, `Date`, `Bed_id`, `Doctor_name`, `Approval`, `Hospital_id`) VALUES
(1, 'kkkkkkkkk', '+8801791662411', 'm', '+8801791662412', 'Khulshi', 'zz', '2021-12-23', 4, 'sumaiya', 'Accepted', 3);

-- --------------------------------------------------------

--
-- Table structure for table `receptionist`
--

CREATE TABLE `receptionist` (
  `Receptionist_id` int(50) NOT NULL,
  `Receptionist_name` varchar(255) NOT NULL,
  `Address` varchar(255) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Password` varchar(255) NOT NULL,
  `Phone` varchar(15) NOT NULL,
  `Shift` varchar(255) NOT NULL,
  `Status` varchar(255) NOT NULL,
  `Image` varchar(255) NOT NULL,
  `Hospital_id` int(50) NOT NULL,
  `Hospital_name` varchar(260) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `receptionist`
--

INSERT INTO `receptionist` (`Receptionist_id`, `Receptionist_name`, `Address`, `Email`, `Password`, `Phone`, `Shift`, `Status`, `Image`, `Hospital_id`, `Hospital_name`) VALUES
(2, 'Kirti', 'Chawkbazar', 'kirti@gmail.com', 'kirti', '+8801791662418', 'Day', 'Active', '2.jpg', 4, 'Dhaka Medical College'),
(3, 'Safa Marua', 'Chawkbazar', 'safa@gmail.com', 'safa', '+8801791662418', 'Day', 'Active', '2.jpg', 3, 'Chittagong Medical College');

-- --------------------------------------------------------

--
-- Table structure for table `receptionist_salary`
--

CREATE TABLE `receptionist_salary` (
  `sno` int(50) NOT NULL,
  `Receptionist_id` int(50) NOT NULL,
  `Receptionist_name` varchar(255) NOT NULL,
  `Paid_date` date NOT NULL,
  `Month` varchar(260) NOT NULL,
  `Salary` int(50) NOT NULL,
  `Hospital_id` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `receptionist_salary`
--

INSERT INTO `receptionist_salary` (`sno`, `Receptionist_id`, `Receptionist_name`, `Paid_date`, `Month`, `Salary`, `Hospital_id`) VALUES
(1, 3, 'Safa Marua', '2022-01-02', '2022-01', 4000, 3),
(2, 3, 'Safa Marua', '2022-01-02', '2022-02', 4000, 3);

-- --------------------------------------------------------

--
-- Table structure for table `superadmin`
--

CREATE TABLE `superadmin` (
  `id` int(50) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Password` varchar(255) NOT NULL,
  `Phone` varchar(15) NOT NULL,
  `Image` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `superadmin`
--

INSERT INTO `superadmin` (`id`, `Name`, `Email`, `Password`, `Phone`, `Image`) VALUES
(1, 'Monifa Sultana', 'monifa@gmail.com', '41', '+8801791662441', '1.jpg'),
(2, 'Ripa', 'ripa@gmail.com', '1234', '', ''),
(3, 'sumaiya', 'sumu@gmail.com', '1234', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `user_id` int(50) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Address` varchar(255) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`user_id`, `Name`, `Address`, `Email`, `Password`) VALUES
(2, 'Ripa', 'Coxbazar', 'ripa@gmail.com', '49'),
(6, 'SUMAIYA AKTHER KHAN', 'Feni', 'sumu@gmail.com', '48'),
(7, 'Monifa Sultana', 'Chawkbazar', 'monifa@gmail.com', '41');

-- --------------------------------------------------------

--
-- Table structure for table `vaccinated`
--

CREATE TABLE `vaccinated` (
  `id` int(50) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Address` varchar(255) NOT NULL,
  `NID` varchar(255) NOT NULL,
  `Phone_number` varchar(15) NOT NULL,
  `Age_group` varchar(255) NOT NULL,
  `Allergies` varchar(255) NOT NULL,
  `Prior_ailments` varchar(255) NOT NULL,
  `Doze_name` varchar(255) NOT NULL,
  `Appointment1` date NOT NULL,
  `Doze1` varchar(255) NOT NULL,
  `Appointment2` date NOT NULL,
  `Doze2` varchar(255) NOT NULL,
  `Vaccinated` varchar(255) NOT NULL,
  `Hospital_id` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vaccinated`
--

INSERT INTO `vaccinated` (`id`, `Name`, `Address`, `NID`, `Phone_number`, `Age_group`, `Allergies`, `Prior_ailments`, `Doze_name`, `Appointment1`, `Doze1`, `Appointment2`, `Doze2`, `Vaccinated`, `Hospital_id`) VALUES
(1, 'Monifa', 'Chawkbazar', '0192837', '+8801791662418', '18-25', 'No', 'No', 'Sinopharm', '2021-12-10', 'Taken', '2021-12-06', 'Taken', 'Vaccinated', 3),
(4, 'Arfat', 'Bahaddarhat', '987654', '+8801791662432', '18-25', 'No', 'Yes', 'Moderna', '2021-12-01', 'Taken', '2021-12-07', 'Taken', 'Vaccinated', 3),
(6, 'bfj', 'Khulshi', '0192837', '+8801791662431', '26-40', 'Yes', 'No', 'Pfizer', '2021-12-15', 'Taken', '2021-12-16', 'Taken', 'Vaccinated', 3);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bed_allotment`
--
ALTER TABLE `bed_allotment`
  ADD PRIMARY KEY (`Allotment_no`);

--
-- Indexes for table `bed_list`
--
ALTER TABLE `bed_list`
  ADD PRIMARY KEY (`Bed_id`);

--
-- Indexes for table `covid_test`
--
ALTER TABLE `covid_test`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `detail_patient`
--
ALTER TABLE `detail_patient`
  ADD PRIMARY KEY (`Patient_id`);

--
-- Indexes for table `doctor`
--
ALTER TABLE `doctor`
  ADD PRIMARY KEY (`Doctor_id`);

--
-- Indexes for table `doctor_salary`
--
ALTER TABLE `doctor_salary`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `doze1`
--
ALTER TABLE `doze1`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `doze2`
--
ALTER TABLE `doze2`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `hospital`
--
ALTER TABLE `hospital`
  ADD PRIMARY KEY (`Hospital_id`);

--
-- Indexes for table `hospital_request`
--
ALTER TABLE `hospital_request`
  ADD PRIMARY KEY (`Request_id`);

--
-- Indexes for table `patient`
--
ALTER TABLE `patient`
  ADD PRIMARY KEY (`Patient_id`);

--
-- Indexes for table `patient_payment`
--
ALTER TABLE `patient_payment`
  ADD PRIMARY KEY (`Payment_no`);

--
-- Indexes for table `patient_request`
--
ALTER TABLE `patient_request`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `receptionist`
--
ALTER TABLE `receptionist`
  ADD PRIMARY KEY (`Receptionist_id`);

--
-- Indexes for table `receptionist_salary`
--
ALTER TABLE `receptionist_salary`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `superadmin`
--
ALTER TABLE `superadmin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `vaccinated`
--
ALTER TABLE `vaccinated`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bed_allotment`
--
ALTER TABLE `bed_allotment`
  MODIFY `Allotment_no` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `bed_list`
--
ALTER TABLE `bed_list`
  MODIFY `Bed_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `covid_test`
--
ALTER TABLE `covid_test`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `detail_patient`
--
ALTER TABLE `detail_patient`
  MODIFY `Patient_id` int(50) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `doctor`
--
ALTER TABLE `doctor`
  MODIFY `Doctor_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `doctor_salary`
--
ALTER TABLE `doctor_salary`
  MODIFY `sno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `doze1`
--
ALTER TABLE `doze1`
  MODIFY `ID` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `hospital`
--
ALTER TABLE `hospital`
  MODIFY `Hospital_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `hospital_request`
--
ALTER TABLE `hospital_request`
  MODIFY `Request_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `patient`
--
ALTER TABLE `patient`
  MODIFY `Patient_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `patient_payment`
--
ALTER TABLE `patient_payment`
  MODIFY `Payment_no` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `patient_request`
--
ALTER TABLE `patient_request`
  MODIFY `sno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `receptionist`
--
ALTER TABLE `receptionist`
  MODIFY `Receptionist_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `receptionist_salary`
--
ALTER TABLE `receptionist_salary`
  MODIFY `sno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `superadmin`
--
ALTER TABLE `superadmin`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `user_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
