-- ----------------------------------------------------------
-- Options
-- ----------------------------------------------------------
USE dbTruckBytes;

-- ----------------------------------------------------------
-- Drop Tables
-- ----------------------------------------------------------
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS EmployeesShifts;
DROP TABLE IF EXISTS TrucksShifts;
DROP TABLE IF EXISTS TrucksMenuItems;
DROP TABLE IF EXISTS TrucksKitchenSupplies;
DROP TABLE IF EXISTS MenuItemsFoods;
DROP TABLE IF EXISTS TrucksFoods;
DROP TABLE IF EXISTS SubMenusFoods;
DROP TABLE IF EXISTS Trucks;
DROP TABLE IF EXISTS MenuItems;
DROP TABLE IF EXISTS MenuItemsTypes;
DROP TABLE IF EXISTS SubMenus;
DROP TABLE IF EXISTS Shifts;
DROP TABLE IF EXISTS Employees;
DROP TABLE IF EXISTS EmployeeTypes;
DROP TABLE IF EXISTS Sales;
DROP TABLE IF EXISTS SalesPaymentTypes;
DROP TABLE IF EXISTS LoyaltyMembers;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS LoyaltyRewards;
DROP TABLE IF EXISTS Foods;
DROP TABLE IF EXISTS FoodTypes;
DROP TABLE IF EXISTS KitchenSupplies;
DROP TABLE IF EXISTS KitchenSupplyTypes;

-- ----------------------------------------------------------
-- Drop Views
-- ----------------------------------------------------------
DROP VIEW IF EXISTS VMenuItems;
DROP VIEW IF EXISTS VTruckName;
DROP VIEW IF EXISTS VSubMenuItems;
DROP VIEW IF EXISTS VSubMenuName;

-- ----------------------------------------------------------
-- Drop Provedures
-- ----------------------------------------------------------
DROP PROCEDURE IF EXISTS uspAddMenuItem;
DROP PROCEDURE IF EXISTS uspAddCompanyDetails;

-- ----------------------------------------------------------
-- Drop Functions
-- ----------------------------------------------------------
DROP FUNCTION IF EXISTS fnEmployeeLogin;

-- ----------------------------------------------------------
-- Create Tables
-- ----------------------------------------------------------
CREATE TABLE Trucks (
	intTruckID INT AUTO_INCREMENT,
	intTruckNumber INT NOT NULL,
	strTruckName VARCHAR(255) NOT NULL,
	imgCompanyLogo LONGBLOB,
	PRIMARY KEY (intTruckID)
);

CREATE TABLE SubMenus (
	intSubMenuID INT AUTO_INCREMENT,
	strSubMenuName VARCHAR(255) NOT NULL,
	PRIMARY KEY (intSubMenuID)
);

CREATE TABLE MenuItems (
	intMenuItemID INT AUTO_INCREMENT,
	strMenuItemName VARCHAR(255) NOT NULL,
	imgMenuItemImage LONGBLOB,
	intMenuItemTypeID INT NOT NULL,
	strDescription VARCHAR(100),
	dblPrice DECIMAL(10,2) NOT NULL,
	intSubMenuID INT,
	PRIMARY KEY (intMenuItemID)
);

CREATE TABLE MenuItemsTypes (
	intMenuItemTypeID INT AUTO_INCREMENT,
	strMenuItemType VARCHAR(50),
	PRIMARY KEY (intMenuItemTypeID)
);

CREATE TABLE TrucksMenuItems (
	intTruckMenuItemID INT AUTO_INCREMENT,
	intTruckID INT NOT NULL,
	intMenuItemID INT NOT NULL,
	PRIMARY KEY (intTruckMenuItemID)
);

CREATE TABLE Shifts (
	intShiftID INT AUTO_INCREMENT,
	dtmShiftDate DATETIME NOT NULL,
	PRIMARY KEY (intShiftID)
);

CREATE TABLE TrucksShifts (
	intTruckShiftID INT AUTO_INCREMENT,
	intShiftID INT NOT NULL,
	intTruckID INT NOT NULL,
	PRIMARY KEY (intTruckShiftID)
);

CREATE TABLE Employees (
	intEmployeeID INT AUTO_INCREMENT,
	strFirstName VARCHAR(50) NOT NULL,
	strLastName VARCHAR(255) NOT NULL,
	strUserName VARCHAR(255) NOT NULL,
	strPassword VARCHAR(255) NOT NULL,
	dblHourlyRate DECIMAL(5,2) NOT NULL,
	intEmployeeTypeID INT NOT NULL,
	strLicensedToDrive CHAR(1) NOT NULL,
	PRIMARY KEY (intEmployeeID)
);

CREATE TABLE EmployeesShifts (
	intEmployeeShiftID INT AUTO_INCREMENT,
	intEmployeeID INT NOT NULL,
	intShiftID INT NOT NULL,
	dtmShiftStart DATETIME NOT NULL,
	dtmShiftEnd DATETIME NOT NULL,
	PRIMARY KEY (intEmployeeShiftID)
);

CREATE TABLE EmployeeTypes (
	intEmployeeTypeID INT AUTO_INCREMENT,
	strEmployeeType VARCHAR(255) NOT NULL,
	PRIMARY KEY (intEmployeeTypeID)
);

CREATE TABLE Orders (
	intOrderID INT AUTO_INCREMENT,
	intTruckID INT NOT NULL,
	intSaleID INT NOT NULL,
	intCustomerID INT,
	PRIMARY KEY (intOrderID)
);

CREATE TABLE Sales (
	intSaleID INT AUTO_INCREMENT,
	dblSaleAmount DECIMAL(10,2) NOT NULL,
	dtmDate DATETIME NOT NULL,
	intSalesPaymentTypeID INT NOT NULL,
	PRIMARY KEY (intSaleID)
);

CREATE TABLE SalesPaymentTypes (
	intSalesPaymentTypeID INT AUTO_INCREMENT,
	strSalesPaymentType VARCHAR(10) NOT NULL,
	PRIMARY KEY (intSalesPaymentTypeID)
);

CREATE TABLE Customers (
	intCustomerID INT AUTO_INCREMENT,
	strFirstName VARCHAR(50) NOT NULL,
	strLastName VARCHAR(255) NOT NULL,
	strUserName VARCHAR(255) NOT NULL,
	strEmail VARCHAR(255) NOT NULL,
	strPassword VARCHAR(255) NOT NULL,
	strPhoneNumber VARCHAR(12) NOT NULL,
	PRIMARY KEY (intCustomerID)
);

CREATE TABLE LoyaltyMembers (
	intLoyaltyMemberID INT AUTO_INCREMENT,
	intCustomerID INT NOT NULL,
	intLoyaltyRewardID INT,
	PRIMARY KEY (intLoyaltyMemberID)
);

CREATE TABLE LoyaltyRewards (
	intLoyaltyRewardID INT AUTO_INCREMENT,
	strLoyaltyRewardType VARCHAR(255) NOT NULL,
	PRIMARY KEY (intLoyaltyRewardID)
);

CREATE TABLE TrucksFoods (
	intTruckFoodID INT AUTO_INCREMENT,
	intTruckID INT NOT NULL,
	intFoodID INT NOT NULL,
	PRIMARY KEY (intTruckFoodID)
);

CREATE TABLE TrucksKitchenSupplies (
	intTruckKitchenSupplyID INT AUTO_INCREMENT,
	intTruckID INT NOT NULL,
	intKitchenSupplyID INT NOT NULL,
	PRIMARY KEY (intTruckKitchenSupplyID)
);

CREATE TABLE Foods (
	intFoodID INT AUTO_INCREMENT,
	strFoodName VARCHAR(255) NOT NULL,
	dblAmount DECIMAL(5,2) NOT NULL,
	dblPurchasePrice DECIMAL(5,2) NOT NULL,
	dblSellPrice DECIMAL(3,2) NOT NULL,
	intFoodTypeID INT NOT NULL,
	PRIMARY KEY (intFoodID)
);

CREATE TABLE FoodTypes (
	intFoodTypeID INT AUTO_INCREMENT,
	strFoodType VARCHAR(50) NOT NULL,
	PRIMARY KEY (intFoodTypeID)
);

CREATE TABLE SubMenusFoods (
	intSubMenuFoodID INT AUTO_INCREMENT,
	intSubMenuID INT NOT NULL,
	intFoodID INT NOT NULL,
	PRIMARY KEY (intSubMenuFoodID)
);

CREATE TABLE MenuItemsFoods (
	intMenuItemFoodID INT AUTO_INCREMENT,
	intMenuItemID INT NOT NULL,
	intFoodID INT NOT NULL,
	dblFoodWeight DECIMAL(5,2) NOT NULL,
	PRIMARY KEY (intMenuItemFoodID)
);

CREATE TABLE KitchenSupplies (
	intKitchenSupplyID INT AUTO_INCREMENT,
	strKitchenSupplyName VARCHAR(255) NOT NULL,
	intAmount INT NOT NULL,
	intKitchenSupplyTypeID INT NOT NULL,
	PRIMARY KEY (intKitchenSupplyID)
);

CREATE TABLE KitchenSupplyTypes (
	intKitchenSupplyTypeID INT AUTO_INCREMENT,
	strKitchenSupplyTypeName VARCHAR(255) NOT NULL,
	PRIMARY KEY (intKitchenSupplyTypeID)
);

-- ----------------------------------------------------------
-- Foreign Keys
-- ----------------------------------------------------------

--	   Parent					Child					Link
-- -------------------------------------------------------------------------
--  1. Trucks					Orders					intTruckID
--  2. Customers				Orders					intCustomerID
--  3. Sales					Orders					intSaleID
--  4. SalesPaymentTypes		Sales					intSalePaymentTypeID
--  5. Trucks					TrucksFoods				intTruckID
--  6. Foods					TrucksFoods				intFoodID
--  7. Trucks					TrucksKitchenSupplies	intTruckID
--  8. KitchenSupplies			TrucksKitchenSupplies	intKitchenSupplyID
--  9. KitchenSupplyTypes		KitchenSupplies			intKitchenSupplyTypeID
-- 10. FoodTypes				Foods					intFoodTypeID
-- 11. Customers				LoyaltyMembers			intLoyaltyMemberID
-- 12. LoyaltyRewards			LoyaltyMembers			intLoyaltyRewardID
-- 13. EmployeeTypes			Employees				intEmployeeTypeID
-- 14. Employees				EmployeesShifts			intEmployeeID
-- 15. Shifts					EmployeesShifts			intShiftID
-- 16. Shifts					TrucksShifts			intShiftID
-- 17. Trucks					TrucksShifts			intTruckID
-- 18. MenuItems				TrucksMenuItems			intMenuItemID
-- 19. Trucks					TrucksMenuItems			intTruckID
-- 20. MenuItemsTypes			MenuItems				MenuItemTypeID
-- 21. Foods					MenuItemsFoods			intFoodID
-- 22. MenuItems				MenuItemsFoods			intMenuItemID
-- 23. SubMenus					MenuItems				intSubMenuID
-- 24. SubMenus					SubMenusFoods			intSubMenuID
-- 25. Foods					SubMenusFoods			intFoodID

-- 1.
ALTER TABLE Orders ADD CONSTRAINT Orders_Trucks_FK
FOREIGN KEY (intTruckID) REFERENCES Trucks (intTruckID);

-- 2.
ALTER TABLE Orders ADD CONSTRAINT Orders_Customers_FK
FOREIGN KEY (intCustomerID) REFERENCES Customers (intCustomerID);

-- 3.
ALTER TABLE Orders ADD CONSTRAINT Orders_Sales_FK
FOREIGN KEY (intSaleID) REFERENCES Sales (intSaleID);

-- 4.
ALTER TABLE Sales ADD CONSTRAINT Sales_SalesPaymentTypes_FK
FOREIGN KEY (intSalesPaymentTypeID) REFERENCES SalesPaymentTypes (intSalesPaymentTypeID);

-- 5.
ALTER TABLE TrucksFoods ADD CONSTRAINT TrucksFoods_Trucks_FK
FOREIGN KEY (intTruckID) REFERENCES Trucks (intTruckID);

-- 6.
ALTER TABLE TrucksFoods ADD CONSTRAINT TrucksFoods_Foods_FK
FOREIGN KEY (intFoodID) REFERENCES Foods (intFoodID);

-- 7.
ALTER TABLE TrucksKitchenSupplies ADD CONSTRAINT TrucksKitchenSupplies_Trucks_FK
FOREIGN KEY (intTruckID) REFERENCES Trucks (intTruckID);

-- 8.
ALTER TABLE TrucksKitchenSupplies ADD CONSTRAINT TrucksKitchenSupplies_KitchenSupplies_FK
FOREIGN KEY (intKitchenSupplyID) REFERENCES KitchenSupplies (intKitchenSupplyID);

-- 9.
ALTER TABLE KitchenSupplies ADD CONSTRAINT KitchenSupplies_KitchenSupplyTypes_FK
FOREIGN KEY (intKitchenSupplyTypeID) REFERENCES KitchenSupplyTypes (intKitchenSupplyTypeID);

-- 10.
ALTER TABLE Foods ADD CONSTRAINT Foods_FoodTypes_FK
FOREIGN KEY (intFoodTypeID) REFERENCES FoodTypes (intFoodTypeID);

-- 11.
ALTER TABLE LoyaltyMembers ADD CONSTRAINT LoyaltyMembers_Customers_FK
FOREIGN KEY (intCustomerID) REFERENCES Customers (intCustomerID);

-- 12.
ALTER TABLE LoyaltyMembers ADD CONSTRAINT LoyaltyMembers_LoyaltyRewards_FK
FOREIGN KEY (intLoyaltyRewardID) REFERENCES LoyaltyRewards (intLoyaltyRewardID);

-- 13.
ALTER TABLE Employees ADD CONSTRAINT Employees_EmployeeTypes_FK
FOREIGN KEY (intEmployeeTypeID) REFERENCES EmployeeTypes (intEmployeeTypeID);

-- 14.
ALTER TABLE EmployeesShifts ADD CONSTRAINT EmployeesShifts_Employees_FK
FOREIGN KEY (intEmployeeID) REFERENCES Employees (intEmployeeID);

-- 15.
ALTER TABLE EmployeesShifts ADD CONSTRAINT EmployeesShifts_Shifts_FK
FOREIGN KEY (intShiftID) REFERENCES Shifts (intShiftID);

-- 16.
ALTER TABLE TrucksShifts ADD CONSTRAINT TrucksShifts_Shifts_FK
FOREIGN KEY (intShiftID) REFERENCES Shifts (intShiftID);

-- 17.
ALTER TABLE TrucksShifts ADD CONSTRAINT TrucksShifts_Trucks_FK
FOREIGN KEY (intTruckID) REFERENCES Trucks (intTruckID);

-- 18.
ALTER TABLE TrucksMenuItems ADD CONSTRAINT TrucksMenuItems_MenuItems_FK
FOREIGN KEY (intMenuItemID) REFERENCES MenuItems (intMenuItemID);

-- 19.
ALTER TABLE TrucksMenuItems ADD CONSTRAINT TrucksMenuItems_Trucks_FK
FOREIGN KEY (intTruckID) REFERENCES Trucks (intTruckID);

-- 20.
ALTER TABLE MenuItems ADD CONSTRAINT MenuItems_MenuItemsTypes_FK
FOREIGN KEY (intMenuItemTypeID) REFERENCES MenuItemsTypes (intMenuItemTypeID);

-- 21.
ALTER TABLE MenuItemsFoods ADD CONSTRAINT MenuItemsFoods_Foods_FK
FOREIGN KEY (intFoodID) REFERENCES Foods (intFoodID);

-- 22.
ALTER TABLE MenuItemsFoods ADD CONSTRAINT MenuItemsFoods_MenuItems_FK
FOREIGN KEY (intMenuItemID) REFERENCES MenuItems (intMenuItemID);

-- 23.
ALTER TABLE MenuItems ADD CONSTRAINT MenuItems_SubMenus_FK
FOREIGN KEY (intSubMenuID) REFERENCES SubMenus (intSubMenuID);

-- 24.
ALTER TABLE SubMenusFoods ADD CONSTRAINT SubMenusFoods_SubMenus_FK
FOREIGN KEY (intSubMenuID) REFERENCES SubMenus (intSubMenuID);

-- 25.
ALTER TABLE SubMenusFoods ADD CONSTRAINT SubMenusFoods_Foods_FK
FOREIGN KEY (intFoodID) REFERENCES Foods (intFoodID);


-- ----------------------------------------------------------
-- Create Views
-- ----------------------------------------------------------
-- View: VMenuItems
CREATE OR REPLACE VIEW VMenuItems AS
SELECT
    MI.intMenuItemID AS MenuItemID,
    MI.strMenuItemName AS MenuItemName,
    MI.imgMenuItemImage AS MenuItemImage,
    MI.strDescription AS MenuItemDescription,
    MI.dblPrice AS MenuItemPrice,
    MI.intMenuItemTypeID AS MenuType
FROM
    MenuItems AS MI;

-- View: VTruckName
CREATE OR REPLACE VIEW VTruckName AS
SELECT
    strTruckName AS TruckName
FROM
    Trucks;

-- View: VSubMenuItems
CREATE OR REPLACE VIEW VSubMenuItems AS
SELECT
	 F.intFoodID AS SubMenuItemID,
    F.strFoodName AS SubMenuItem,
    MI.intMenuItemID AS MenuItem
FROM
    MenuItems AS MI
JOIN SubMenus AS SM ON MI.intSubMenuID = SM.intSubMenuID
JOIN SubMenusFoods AS SMF ON SMF.intSubMenuID = SM.intSubMenuID
JOIN Foods AS F ON F.intFoodID = SMF.intFoodID;

-- View: VSubMenuName
CREATE OR REPLACE VIEW VSubMenuName AS
SELECT
    SM.strSubMenuName AS SubMenu,
    MI.intMenuItemID AS MenuItem
FROM
    SubMenus AS SM
JOIN MenuItems AS MI ON SM.intSubMenuID = MI.intSubMenuID;


-- ----------------------------------------------------------
-- Create Procedures
-- ----------------------------------------------------------
DELIMITER $$

-- Procedure: uspAddMenuItem
CREATE PROCEDURE uspAddMenuItem (
    IN strMenuItemNameIN VARCHAR(255),
    IN imgMenuItemImageIN BLOB,
    IN strDescriptionIN VARCHAR(1000),
    IN dblPriceIN DECIMAL(10,2),
    IN intMenuItemTypeIDIN INT
)
BEGIN
    INSERT INTO MenuItems (strMenuItemName, imgMenuItemImage, strDescription, dblPrice, intMenuItemTypeID)
    VALUES (strMenuItemNameIN, imgMenuItemImageIN, strDescriptionIN, dblPriceIN, intMenuItemTypeIDIN);
END $$

-- Procedure: uspAddCompanyDetails
CREATE PROCEDURE uspAddCompanyDetails (
    IN intTruckNumberIN INT,
    IN strCompanyNameIN VARCHAR(255),
    IN imgCompanyLogoIN BLOB
)
BEGIN
    INSERT INTO Trucks (intTruckNumber, strTruckName, imgCompanyLogo)
    VALUES (intTruckNumberIN, strCompanyNameIN, imgCompanyLogoIN);
END $$

DELIMITER ;

-- ----------------------------------------------------------
-- Create Functions
-- ----------------------------------------------------------

DELIMITER $$

-- Function: fnEmployeeLogin
CREATE FUNCTION fnEmployeeLogin(
    strLastNameIN VARCHAR(255),
    strPasswordIN VARCHAR(255)
)
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE intUID INT;

    SELECT intEmployeeID
    INTO intUID
    FROM Employees
    WHERE strLastName = strLastNameIN
      AND strPassword = strPasswordIN
    LIMIT 1;

    RETURN intUID;
END $$

DELIMITER ;

-- ----------------------------------------------------------
-- Inserts
-- ----------------------------------------------------------

-- Disable foreign key checks during insert (optional)
SET FOREIGN_KEY_CHECKS=0;

-- Employee Types
INSERT INTO EmployeeTypes (strEmployeeType) VALUES
  ('cashier'),
  ('manager'),
  ('cook');

-- Employees
INSERT INTO Employees (strFirstName, strLastName, strUserName, strPassword, dblHourlyRate, intEmployeeTypeID, strLicensedToDrive) VALUES
  ('Cole', 'Whitaker', 'CW', 'test1', 20.50, 2, 'Y'),
  ('Adam', 'Broderick', 'AB', 'test1', 20.50, 2, 'Y'),
  ('Jason', 'Cope', 'JC', 'test1', 20.50, 2, 'Y'),
  ('Bruce', 'Wayne', 'BW', 'test1', 18.75, 3, 'N'),
  ('Clark', 'Kent', 'CK', 'test1', 18.75, 3, 'Y'),
  ('Oliver', 'Queen', 'OQ', 'test1', 18.75, 3, 'N'),
  ('Barry', 'Allen', 'BA', 'test1', 18.75, 1, 'Y'),
  ('Barbara', 'Gordon', 'BG', 'test1', 18.75, 1, 'N'),
  ('Harvey', 'Dent', 'HD', 'test1', 18.75, 1, 'Y');

-- Shifts
INSERT INTO Shifts (dtmShiftDate) VALUES
  ('2025-07-01'),
  ('2025-07-02'),
  ('2025-07-03');

-- EmployeesShifts
INSERT INTO EmployeesShifts (intEmployeeID, intShiftID, dtmShiftStart, dtmShiftEnd) VALUES
  (1, 1, '2025-07-01 08:00:00', '2025-07-01 16:00:00'),
  (4, 1, '2025-07-01 08:00:00', '2025-07-01 16:00:00'),
  (9, 1, '2025-07-01 08:00:00', '2025-07-01 16:00:00'),
  (2, 2, '2025-07-02 08:00:00', '2025-07-02 16:00:00'),
  (5, 2, '2025-07-02 08:00:00', '2025-07-02 16:00:00'),
  (7, 2, '2025-07-02 08:00:00', '2025-07-02 16:00:00'),
  (3, 3, '2025-07-03 08:00:00', '2025-07-03 16:00:00'),
  (6, 3, '2025-07-03 08:00:00', '2025-07-03 16:00:00'),
  (8, 3, '2025-07-03 08:00:00', '2025-07-03 16:00:00');

-- Trucks
INSERT INTO Trucks (intTruckNumber, strTruckName, imgCompanyLogo) VALUES
  (1, 'SuperTruck', NULL);

-- TrucksShifts
INSERT INTO TrucksShifts (intShiftID, intTruckID) VALUES
  (1, 1),
  (2, 1),
  (3, 1);

-- LoyaltyRewards
INSERT INTO LoyaltyRewards (strLoyaltyRewardType) VALUES
  ('10% off'),
  ('15% off'),
  ('1 free drink');

-- Customers
INSERT INTO Customers (strFirstName, strLastName, strUserName, strEmail, strPassword, strPhoneNumber) VALUES
  ('Hal', 'Jordan', 'GreenLantern', 'hjordan@gmail.com', 'test2', '513-111-1111'),
  ('Lex', 'Luthor', 'EvilGuy', 'lluthor@gmail.com', 'test2', '513-222-2222'),
  ('Jason', 'Todd', 'RedHood', 'jtodd@gmail.com', 'test2', '513-333-3333');

-- LoyaltyMembers
INSERT INTO LoyaltyMembers (intCustomerID, intLoyaltyRewardID) VALUES
  (1, NULL),
  (2, 2),
  (3, 3);

-- SalesPaymentTypes
INSERT INTO SalesPaymentTypes (strSalesPaymentType) VALUES
  ('cash'),
  ('card');

-- Sales
INSERT INTO Sales (dblSaleAmount, dtmDate, intSalesPaymentTypeID) VALUES
  (30.50, '2025-07-01 09:00:00', 1),
  (10.50, '2025-07-01 10:00:00', 1),
  (22.50, '2025-07-01 11:00:00', 2),
  (7.25, '2025-07-01 12:00:00', 1),
  (28.75, '2025-07-01 13:00:00', 2),
  (21.50, '2025-07-02 09:00:00', 1),
  (4.50, '2025-07-02 10:00:00', 1),
  (14.25, '2025-07-02 11:00:00', 1),
  (25.15, '2025-07-02 12:00:00', 2),
  (2.50, '2025-07-02 13:00:00', 1),
  (17.50, '2025-07-03 09:00:00', 2),
  (31.75, '2025-07-03 10:00:00', 2),
  (11.60, '2025-07-03 11:00:00', 1),
  (18.50, '2025-07-03 12:00:00', 2),
  (6.30, '2025-07-03 13:00:00', 1);

-- Orders
INSERT INTO Orders (intTruckID, intSaleID, intCustomerID) VALUES
  (1, 1, NULL),
  (1, 2, 1),
  (1, 3, NULL),
  (1, 4, NULL),
  (1, 5, 2),
  (1, 6, NULL),
  (1, 7, 3),
  (1, 8, 1),
  (1, 9, NULL),
  (1, 10, NULL),
  (1, 11, NULL),
  (1, 12, 2),
  (1, 13, NULL),
  (1, 14, NULL),
  (1, 15, 3);

-- KitchenSupplyTypes
INSERT INTO KitchenSupplyTypes (strKitchenSupplyTypeName) VALUES
  ('Utensils'),
  ('Cookingware'),
  ('Serving Containers'),
  ('Paper goods'),
  ('Cups'),
  ('Straws'),
  ('Plasticware');

-- KitchenSupplies
INSERT INTO KitchenSupplies (strKitchenSupplyName, intAmount, intKitchenSupplyTypeID) VALUES
  ('Tongs', 6, 1),
  ('Spatula', 4, 1),
  ('Slotted Turner', 4, 1),
  ('Chef Knife', 3, 1),
  ('Pizza Cutter', 2, 1),
  ('Pizza Peel', 1, 1),
  ('Sauce Pan', 2, 2),
  ('Stock Pot', 3, 2),
  ('Saute Pan', 3, 2),
  ('Pizza Box', 30, 3),
  ('Food Boat', 200, 3),
  ('Paper Towel Roll', 12, 4),
  ('Napkins', 500, 4),
  ('8oz Plastic Cups', 200, 5),
  ('12oz Plastic Cups', 150, 5),
  ('20oz Plastic Cups', 100, 5),
  ('7.75in Paper Wrapped Straw', 500, 6),
  ('Plastic Fork', 300, 7),
  ('Plastic Spoon', 100, 7),
  ('Plastic Knife', 200, 7);

-- TrucksKitchenSupplies
INSERT INTO TrucksKitchenSupplies (intTruckID, intKitchenSupplyID) VALUES
  (1, 1),
  (1, 2),
  (1, 3),
  (1, 4),
  (1, 5),
  (1, 6),
  (1, 7),
  (1, 8),
  (1, 9),
  (1, 10),
  (1, 11),
  (1, 12),
  (1, 13),
  (1, 14),
  (1, 15),
  (1, 16),
  (1, 17),
  (1, 18),
  (1, 19),
  (1, 20);

-- FoodTypes
INSERT INTO FoodTypes (strFoodType) VALUES
  ('Meats'),
  ('Veggies'),
  ('Drinks'),
  ('Breads'),
  ('Cheeses'),
  ('Seasonings'),
  ('Sauce'),
  ('Condiments'),
  ('Other');

-- SubMenus
INSERT INTO SubMenus (strSubMenuName) VALUES
  ('Burgers'),
  ('Tacos'),
  ('Pizzas'),
  ('Hotdogs');

-- Foods
INSERT INTO Foods (strFoodName, dblAmount, dblPurchasePrice, dblSellPrice, intFoodTypeID) VALUES
  ('Chicken', 20, 100, 1.88, 1),
  ('Ground Beef', 20, 60, 1.13, 1),
  ('Hamburger Patty', 10, 35, 3.50, 1),
  ('Hotdog', 10, 25, 1.50, 1),
  ('Shredded Lettuce', 10, 10, 0.10, 2),
  ('Lettuce Leaf', 10, 10, 0.15, 2),
  ('Diced Tomato', 10, 12, 0.11, 2),
  ('Sliced Tomato', 10, 12, 0.25, 2),
  ('Potatoes', 25, 30, 0.20, 2),
  ('Burger Bun', 30, 12, 0.50, 4),
  ('Hot Dog Bun', 4.8, 14, 0.40, 4),
  ('Tortilla', 6.25, 15, 0.30, 4),
  ('Cheddar Cheese', 5, 20, 0.75, 5),
  ('Mozzarella Cheese', 5, 18, 0.45, 5),
  ('Pizza Dough Ball', 20, 22, 1.50, 4),
  ('Pizza Sauce', 10, 10, 0.30, 7),
  ('Pepperoni', 5, 14, 0.60, 1),
  ('Sausage Crumble', 5, 16, 0.65, 1),
  ('Onions', 10, 8, 0.10, 2),
  ('Pickles', 5, 6, 0.10, 2),
  ('Ketchup', 3, 4, 0.10, 8),
  ('Mustard', 3, 4, 0.10, 8),
  ('Mayonnaise', 3, 4, 0.10, 8),
  ('Coca-Cola Syrup (5 gal box)', 640, 95, 0.25, 3),
  ('Dr. Pepper Syrup (5 gal box)', 640, 95, 0.25, 3),
  ('Lemonade Mix (1 gal)', 128, 8, 0.08, 3),
  ('Bottled Water (16.9oz)', 24, 10, 1.00, 3),
  ('Blue Powerade Mix (1 gal)', 128, 9, 0.10, 3);

-- SubMenusFoods
INSERT INTO SubMenusFoods (intSubMenuID, intFoodID) VALUES
  (1, 10),
  (1, 3),
  (1, 8),
  (1, 13),
  (1, 6),
  (1, 19),
  (1, 20),
  (1, 21),
  (1, 22),
  (1, 23),
  (2, 12),
  (2, 1),
  (2, 2),
  (2, 5),
  (2, 7),
  (2, 13),
  (2, 19),
  (3, 15),
  (3, 16),
  (3, 14),
  (3, 2),
  (3, 17),
  (3, 18),
  (3, 8),
  (3, 19),
  (4, 11),
  (4, 4),
  (4, 21),
  (4, 22);

-- TrucksFoods
INSERT INTO TrucksFoods (intTruckID, intFoodID) VALUES
  (1, 1),
  (1, 2),
  (1, 3),
  (1, 4),
  (1, 5),
  (1, 6),
  (1, 7),
  (1, 8),
  (1, 9),
  (1, 10),
  (1, 11),
  (1, 12),
  (1, 13),
  (1, 14),
  (1, 15),
  (1, 16),
  (1, 17),
  (1, 18),
  (1, 19),
  (1, 20),
  (1, 21),
  (1, 22),
  (1, 23),
  (1, 24),
  (1, 25),
  (1, 26),
  (1, 27);

-- MenuItemsTypes
INSERT INTO MenuItemsTypes (strMenuItemType) VALUES
  ('Mains'),
  ('Sides'),
  ('Drinks');

-- MenuItems
INSERT INTO MenuItems (strMenuItemName, imgMenuItemImage, intMenuItemTypeID, strDescription, dblPrice, intSubMenuID) VALUES
  ('Burger', NULL, 1, 'Burger with bun, patty, cheese, lettuce, tomato, onion, ketchup, mustard, and mayonnaise', 9.50, 1),
  ('Chicken Taco', NULL, 1, 'Taco with tortialla, chicken, lettuce, and tomato', 3.25, 2),
  ('Beef Taco', NULL, 1, 'Taco with tortilla, beef, lettuce, and tomato', 3.00, 2),
  ('Fries', NULL, 2, NULL, 1.50, NULL),
  ('Cheese Pizza', NULL, 1, 'Pizza with dough, sauce, and cheese', 7.00, 3),
  ('Veggie Pizza', NULL, 1, 'Pizza with dough, sauce, cheese, tomato, and onion', 9.00, 3),
  ('Sausage & Pepperoni Pizza', NULL, 1, 'Pizza with dough, sauce, cheese, sausage, and pepperoni', 11.00, 3),
  ('Hotdog', NULL, 1, 'Hotdog bun, hotdog, ketchup, and mustard', 3.50, 4),
  ('Coca-Cola', NULL, 3, NULL, 1.50, NULL),
  ('Dr. Pepper', NULL, 3, NULL, 1.50, NULL),
  ('Lemonade', NULL, 3, NULL, 1.75, NULL),
  ('Water', NULL, 3, NULL, 1.25, NULL),
  ('Blue Powerade', NULL, 3, NULL, 1.50, NULL);

INSERT INTO MenuItemsFoods (intMenuItemID, intFoodID, dblFoodWeight) VALUES
    -- Burger (MenuItemID 1)
    (1, 3, 0.25),        -- Hamburger Patty (4 oz)
    (1, 10, 0.25),       -- Burger Bun (~0.25 lb)
    (1, 6, 0.05),        -- Lettuce Leaf (0.75 oz)
    (1, 8, 0.06),        -- Sliced Tomato (1 oz)
    (1, 13, 0.06),       -- Cheddar Cheese (1 oz)
    (1, 20, 0.03),       -- Pickles (0.5 oz)
    (1, 21, 0.02),       -- Ketchup (0.25 oz)
    (1, 22, 0.02),       -- Mustard (0.25 oz)
    (1, 23, 0.02),       -- Mayonnaise (0.25 oz)

    -- Chicken Taco (MenuItemID 2)
    (2, 1, 0.13),        -- Chicken (2 oz)
    (2, 12, 0.25),       -- Tortilla (~0.25 lb)
    (2, 5, 0.031),       -- Shredded Lettuce (0.5 oz)
    (2, 7, 0.031),       -- Diced Tomato (0.5 oz)
    (2, 13, 0.05),       -- Cheddar Cheese (0.75 oz)

    -- Beef Taco (MenuItemID 3)
    (3, 2, 0.13),        -- Ground Beef (2 oz)
    (3, 12, 0.25),       -- Tortilla (~0.25 lb)
    (3, 5, 0.031),       -- Shredded Lettuce (0.5 oz)
    (3, 7, 0.031),       -- Diced Tomato (0.5 oz)
    (3, 13, 0.05),       -- Cheddar Cheese (0.75 oz)

    -- Fries (MenuItemID 4)
    (4, 9, 0.31),        -- Potatoes (5 oz)

    -- Cheese Pizza (MenuItemID 5)
    (5, 15, 0.25),       -- Pizza Dough Ball (~0.25 lb)
    (5, 16, 0.19),       -- Pizza Sauce (3 oz)
    (5, 14, 0.19),       -- Mozzarella Cheese (3 oz)

    -- Veggie Pizza (MenuItemID 6)
    (6, 15, 0.25),       -- Pizza Dough Ball (~0.25 lb)
    (6, 16, 0.19),       -- Pizza Sauce (3 oz)
    (6, 14, 0.16),       -- Mozzarella Cheese (2.5 oz)
    (6, 7, 0.06),        -- Diced Tomato (1 oz)
    (6, 19, 0.06),       -- Onions (1 oz)

    -- Sausage & Pepperoni Pizza (MenuItemID 7)
    (7, 15, 0.25),       -- Pizza Dough Ball (~0.25 lb)
    (7, 16, 0.19),       -- Pizza Sauce (3 oz)
    (7, 14, 0.19),       -- Mozzarella Cheese (3 oz)
    (7, 17, 0.13),       -- Pepperoni (2 oz)
    (7, 18, 0.13),       -- Sausage Crumble (2 oz)

    -- Hotdog (MenuItemID 8)
    (8, 11, 0.25),       -- Hot Dog Bun (~0.25 lb)
    (8, 4, 0.15),        -- Hotdog (~0.15 lb)
    (8, 21, 0.02),       -- Ketchup (0.25 oz)
    (8, 22, 0.02),       -- Mustard (0.25 oz)

    -- Coca-Cola (MenuItemID 9)
    (9, 24, 0.75),       -- Coca-Cola Syrup (12 oz)

    -- Dr. Pepper (MenuItemID 10)
    (10, 25, 0.75),      -- Dr. Pepper Syrup (12 oz)

    -- Lemonade (MenuItemID 11)
    (11, 26, 0.5),       -- Lemonade Mix (8 oz)

    -- Water (MenuItemID 12)
    (12, 27, 1.00),      -- Bottled Water (16 oz bottle)

    -- Blue Powerade (MenuItemID 13)
    (13, 28, 1.25);      -- Blue Powerade Mix (20 oz)

INSERT INTO TrucksMenuItems (intTruckID, intMenuItemID) VALUES
    (1, 1),
    (1, 2),
    (1, 3),
    (1, 4),
    (1, 5),
    (1, 6),
    (1, 7),
    (1, 8),
    (1, 9),
    (1, 10),
    (1, 11),
    (1, 12),
    (1, 13);