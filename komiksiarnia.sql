------------------------------------------
-- Projekt: Baza danych: `komiksiarnia` -- 
------------------------------------------

CREATE DATABASE IF NOT EXISTS `komiksiarnia` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `komiksiarnia`;

-- #####################################
-- Struktura tabeli dla tabeli `klienci`
-- #####################################

CREATE TABLE IF NOT EXISTS `klienci` (
  `idklienta` int(11) NOT NULL AUTO_INCREMENT,
  `imie` text COLLATE utf8_polish_ci NOT NULL,
  `nazwisko` text COLLATE utf8_polish_ci NOT NULL,
  `region` text COLLATE utf8_polish_ci NOT NULL,
  PRIMARY KEY (`idklienta`),
  KEY `id` (`idklienta`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci AUTO_INCREMENT=11 ;

-- #############################
-- Zrzut danych tabeli `klienci`
-- #############################

INSERT INTO `klienci` (`idklienta`, `imie`, `nazwisko`, `region`) VALUES
(1, 'Peter', 'Parker', 'Queens'),
(2, 'Edward', 'Brock', 'San Francisco'),
(3, 'Miguel', 'O Hara', 'Nowy York'),
(4, 'Wilson', 'Fisk', 'Manhattan'),
(5, 'Maxwell', 'Dillon', 'Endicott'),
(6, 'Felicia', 'Hardy', 'Harlem'),
(7, 'Adrian', 'Toomes', 'Nowy York'),
(8, 'Herman', 'Schultz', 'Harlem'),
(9, 'Aaron', 'Davis', 'Brooklyn'),
(10, 'Gwendolyne', 'Stacy', 'Queens');



-- ####################################
-- Struktura tabeli dla tabeli `komiks`
-- ####################################

CREATE TABLE IF NOT EXISTS `komiks` (
  `idkomiks` int(11) NOT NULL AUTO_INCREMENT,
  `imieautora` varchar(255) COLLATE utf8_polish_ci NOT NULL,
  `nazwiskoautora` varchar(255) COLLATE utf8_polish_ci NOT NULL,
  `tytul` varchar(255) COLLATE utf8_polish_ci NOT NULL,
  `cena` decimal(10,2) NOT NULL,
  `rok` int(11) NOT NULL,
  PRIMARY KEY (`idkomiks`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci AUTO_INCREMENT=6;

-- ############################
-- Zrzut danych tabeli `komiks`
-- ############################

INSERT INTO `komiks` (`idkomiks`, `imieautora`, `nazwiskoautora`, `tytul`, `cena`, `rok`) VALUES
(1, 'Stan', 'Lee', 'Amazing Fantasy #15', 1000000.00, 1962),
(2, 'Brian', 'Bendis', 'Ultimate Fallout #4', 550.00, 2011),
(3, 'Marv', 'Wolfman', 'The Amazing Spider-Man #194', 600.00, 1979),
(4, 'Tom', 'DeFalco', 'Amazing Spider-Man #252', 275.00, 1984),
(5, 'Brian', 'Bendis', 'Death of Spider-Man', 330.00, 2011);


-- ########################################################################################

-- ########################################
-- Struktura tabeli dla tabeli `zamowienia`
-- ########################################

CREATE TABLE IF NOT EXISTS `zamowienia` (
  `idzamowienia` int(11) NOT NULL AUTO_INCREMENT,
  `idklienta` int(11) NOT NULL,
  `idkomiks` int(11) NOT NULL,
  `data` date NOT NULL,
  `status` text COLLATE utf8_polish_ci NOT NULL,
  PRIMARY KEY (`idzamowienia`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci AUTO_INCREMENT=11 ;

-- ################################
-- Zrzut danych tabeli `zamowienia`
-- ################################

INSERT INTO `zamowienia` (`idzamowienia`, `idklienta`, `idkomiks`, `data`, `status`) VALUES
(1, 2, 4, '2019-10-08', 'oczekiwanie'),
(2, 7, 1, '2017-09-05', 'wyslano'),
(3, 9, 1, '2018-10-11', 'wyslano'),
(4, 2, 2, '2019-10-15', 'oczekiwanie'),
(5, 2, 5, '2020-08-12', 'oczekiwanie'),
(6, 3, 2, '2021-10-20', 'wyslano'),
(7, 4, 3, '2021-08-14', 'wyslano'),
(8, 8, 1, '2020-08-19', 'wyslano'),
(9, 3, 5, '2019-11-19', 'wyslano'),
(10, 9, 2, '2018-12-28', 'oczekiwanie');
