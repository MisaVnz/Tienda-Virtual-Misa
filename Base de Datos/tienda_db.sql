-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 27-06-2024 a las 23:49:54
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `tienda_db`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos_tienda`
--

CREATE TABLE `productos_tienda` (
  `Id` int(11) NOT NULL,
  `Nombre_Producto` varchar(100) NOT NULL,
  `Procesador` varchar(100) NOT NULL,
  `Memoria_RAM` varchar(100) NOT NULL,
  `Memoria_ROM` varchar(100) NOT NULL,
  `GPU` varchar(100) NOT NULL,
  `Pantalla` varchar(100) NOT NULL,
  `Sistema` varchar(100) NOT NULL,
  `Precio` int(11) NOT NULL,
  `Proveedor` varchar(100) NOT NULL,
  `Inventario` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `productos_tienda`
--

INSERT INTO `productos_tienda` (`Id`, `Nombre_Producto`, `Procesador`, `Memoria_RAM`, `Memoria_ROM`, `GPU`, `Pantalla`, `Sistema`, `Precio`, `Proveedor`, `Inventario`) VALUES
(1, 'Acer Nitro V ', 'Intel Core i5-13420H', '8 GB DDR5    ', '512 GB SSD     ', 'NVIDIA GeForce RTX 4050', '15.6 Pulgadas(144Hz)', 'Windows 11 Home', 773, 'Intel Corporation', 5),
(2, 'ASUS E1504FA ', 'AMD Ryzen 3 4.1Ghz', '8 GB DDR5  ', '128 GB SSD      ', 'Integrado', '15,6 Pulgadas(144Hz)', 'Windows 11 Home', 299, 'Advanced Micro Devices(AMD)', 4),
(3, 'HP Elitebook 650 G10', 'Intel Core i7-1355U ', '32 GB DDR4      ', '1 TB SSD     ', 'Intel Iris Xe  ', '15,6 Pulgadas(144Hz)', 'Windows 11 Pro', 926, 'Intel Corporation', 3),
(4, 'ASUS ROG Strix G16', 'Intel Core I7-11700 4.9Ghz', '16 GB DDR5          ', '1 TB SSD     ', 'NVIDIA GeForce RTX 4060', '16 Pulgadas(165Hz)', 'Windows 11 Home', 1309, 'Intel Corporation', 4),
(5, 'ASUS TUF Gaming A15  ', 'AMD Ryzen™ 5 7535HS   ', '8 GB DDR5    ', 'SSD Gen4 de 512GB     ', 'NVIDIA® GeForce RTX™ 2050    ', '15,6 Pulgadas(144Hz)   ', 'Windows 11 Home      ', 699, 'Advanced Micro Devices(AMD) ', 2),
(6, 'ASUS ROG Strix G15', 'AMD Ryzen 7 6800HS  ', '16 GB DDR5     ', '512 GB SSD     ', 'NVIDIA GeForce RTX 3050   ', '15,6 Pulgadas(144Hz)    ', 'Windows 11 Home   ', 876, 'Advanced Micro Devices(AMD)  ', 3),
(7, 'FUNYET DuetBook  ', 'Intel N95 de 12ª generación ', '16 GB DDR4  ', '512 GB SSD  ', 'Intel UHD Graphics  ', '16 Pulgadas(144Hz)  ', 'Windows 11 Pro   ', 350, 'Intel Corporation  ', 7),
(8, '2023 Laptop Inspiron15-3525', 'AMD Ryzen 5 5500U  ', '16 GB DDR4  ', '512 GB SSD  ', 'AMD Radeon  ', '15,6 Pulgadas(144Hz)', 'Windows 11 Home  ', 418, 'Advanced Micro Devices(AMD) ', 5),
(9, 'Laptop BiTECOOL  ', 'Intel Core i3-5005U  ', '16 GB DDR4  ', '512 GB SSD  ', 'Intel HD Graphics 5500', '15,6 Pulgadas(144Hz)  ', 'Windows 11 Pro  ', 300, 'Intel Corporation   ', 8),
(10, 'Lenovo ThinkPad X1Carbon Gen 11', 'Intel Core i7-1355U ', '16 GB DDR5 ', '512 GB SSD ', 'Intel Xe  ', '14 Pulgadas(144Hz) ', 'Windows 11 Pro  ', 1403, 'Intel Corporation  ', 6);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios_tienda`
--

CREATE TABLE `usuarios_tienda` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `usuario` varchar(50) NOT NULL,
  `contraseña` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `usuarios_tienda`
--

INSERT INTO `usuarios_tienda` (`id`, `nombre`, `apellido`, `usuario`, `contraseña`) VALUES
(1, 'Misael', 'Carmona', 'Misa_Vnz', 'Santa25'),
(2, 'Ingeniero', 'Manuel', 'Manuel', '20');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `productos_tienda`
--
ALTER TABLE `productos_tienda`
  ADD PRIMARY KEY (`Id`);

--
-- Indices de la tabla `usuarios_tienda`
--
ALTER TABLE `usuarios_tienda`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `usuario` (`usuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `productos_tienda`
--
ALTER TABLE `productos_tienda`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `usuarios_tienda`
--
ALTER TABLE `usuarios_tienda`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
