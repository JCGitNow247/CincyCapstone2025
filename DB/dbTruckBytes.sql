----------------------------------------------------------------------------
-- Options
----------------------------------------------------------------------------
USE dbTruckBytes
SET NOCOUNT ON

----------------------------------------------------------------------------
-- Drop Tables
----------------------------------------------------------------------------
IF OBJECT_ID('Orders')					IS NOT NULL DROP TABLE Orders
IF OBJECT_ID('EmployeesShifts')			IS NOT NULL DROP TABLE EmployeesShifts
IF OBJECT_ID('TrucksShifts')			IS NOT NULL DROP TABLE TrucksShifts
IF OBJECT_ID('TrucksMenuItems')			IS NOT NULL DROP TABLE TrucksMenuItems
IF OBJECT_ID('TrucksKitchenSupplies')	IS NOT NULL DROP TABLE TrucksKitchenSupplies
IF OBJECT_ID('MenuItemsFoods')			IS NOT NULL DROP TABLE MenuItemsFoods
IF OBJECT_ID('TrucksFoods')				IS NOT NULL DROP TABLE TrucksFoods
IF OBJECT_ID('SubMenusFoods')			IS NOT NULL DROP TABLE SubMenusFoods
IF OBJECT_ID('Trucks')					IS NOT NULL DROP TABLE Trucks
IF OBJECT_ID('MenuItems')				IS NOT NULL DROP TABLE MenuItems
IF OBJECT_ID('MenuItemsTypes')			IS NOT NULL DROP TABLE MenuItemsTypes
IF OBJECT_ID('SubMenus')				IS NOT NULL DROP TABLE SubMenus
IF OBJECT_ID('Shifts')					IS NOT NULL DROP TABLE Shifts
IF OBJECT_ID('Employees')				IS NOT NULL DROP TABLE Employees
IF OBJECT_ID('EmployeeTypes')			IS NOT NULL DROP TABLE EmployeeTypes
IF OBJECT_ID('Sales')					IS NOT NULL DROP TABLE Sales
IF OBJECT_ID('SalesPaymentTypes')		IS NOT NULL DROP TABLE SalesPaymentTypes
IF OBJECT_ID('LoyaltyMembers')			IS NOT NULL DROP TABLE LoyaltyMembers
IF OBJECT_ID('Customers')				IS NOT NULL DROP TABLE Customers
IF OBJECT_ID('LoyaltyRewards')			IS NOT NULL DROP TABLE LoyaltyRewards
IF OBJECT_ID('Foods')					IS NOT NULL DROP TABLE Foods
IF OBJECT_ID('FoodTypes')				IS NOT NULL DROP TABLE FoodTypes
IF OBJECT_ID('KitchenSupplies')			IS NOT NULL DROP TABLE KitchenSupplies
IF OBJECT_ID('KitchenSupplyTypes')		IS NOT NULL DROP TABLE KitchenSupplyTypes

----------------------------------------------------------------------------
-- Drop Views
----------------------------------------------------------------------------
IF OBJECT_ID('VMenuItems')				IS NOT NULL DROP VIEW VMenuItems
IF OBJECT_ID('VTruckName')				IS NOT NULL DROP VIEW VTruckName
IF OBJECT_ID('VSubMenuItems')			IS NOT NULL DROP VIEW VSubMenuItems
IF OBJECT_ID('VSubMenuName')			IS NOT NULL DROP VIEW VSubMenuName

----------------------------------------------------------------------------
-- Drop Procedures
----------------------------------------------------------------------------

IF OBJECT_ID('uspAddMenuItem')			IS NOT NULL DROP PROCEDURE uspAddMenuItem
IF OBJECT_ID('uspAddCompanyDetails')	IS NOT NULL DROP PROCEDURE uspAddCompanyDetails

----------------------------------------------------------------------------
-- Drop Functions
----------------------------------------------------------------------------
IF OBJECT_ID('fnEmployeeLogin')			IS NOT NULL DROP FUNCTION fnEmployeeLogin


----------------------------------------------------------------------------
-- Create Tables
----------------------------------------------------------------------------
CREATE TABLE Trucks
(
	intTruckID					INTEGER IDENTITY,
	intTruckNumber				INTEGER				NOT NULL,
	strTruckName				VARCHAR(255)		NOT NULL,
	imgCompanyLogo				VARBINARY(MAX),
	CONSTRAINT Trucks_PK PRIMARY KEY (intTruckID)
)

CREATE TABLE SubMenus
(
	intSubMenuID				INTEGER IDENTITY,
	strSubMenuName				VARCHAR(255)		NOT NULL,
	CONSTRAINT SubMenus_PK PRIMARY KEY (intSubMenuID)
)

CREATE TABLE MenuItems
(
	intMenuItemID				INTEGER IDENTITY,
	strMenuItemName				VARCHAR(255)		NOT NULL,
	imgMenuItemImage			VARBINARY(MAX),
	intMenuItemTypeID			INTEGER				NOT NULL,
	strDescription				VARCHAR(100),
	dblPrice					DECIMAL(10,2)		NOT NULL,
	intSubMenuID				INTEGER,
	CONSTRAINT MenuItems_PK PRIMARY KEY (intMenuItemID)
)

CREATE TABLE MenuItemsTypes
(
	intMenuItemTypeID			INTEGER IDENTITY,
	strMenuItemType				VARCHAR(50),
	CONSTRAINT MenuItemsTypes_PK PRIMARY KEY (intMenuItemTypeID)
)

CREATE TABLE TrucksMenuItems
(
	intTruckMenuItemID			INTEGER IDENTITY,
	intTruckID					INTEGER				NOT NULL,
	intMenuItemID				INTEGER				NOT NULL,
	CONSTRAINT TrucksMenuItems_PK PRIMARY KEY (intTruckMenuItemID)
)

CREATE TABLE Shifts
(
	intShiftID					INTEGER IDENTITY,
	dtmShiftDate				DATETIME			NOT NULL,
	CONSTRAINT Shifts_PK PRIMARY KEY (intShiftID)
)

CREATE TABLE TrucksShifts
(
	intTruckShiftID				INTEGER IDENTITY,
	intShiftID					INTEGER				NOT NULL,
	intTruckID					INTEGER				NOT NUll,
	CONSTRAINT TrucksShifts_PK PRIMARY KEY (intTruckShiftID)
)

CREATE TABLE Employees
(
	intEmployeeID				INTEGER IDENTITY,
	strFirstName				VARCHAR(50)			NOT NULL,
	strLastName					VARCHAR(255)		NOT NULL,
	strUserName					VARCHAR(255)		NOT NULL,
	strPassword					VARCHAR(255)		NOT NULL,
	dblHourlyRate				DECIMAL(5,2)		NOT NULL,
	intEmployeeTypeID			INTEGER				NOT NULL,
	strLicensedToDrive			VARCHAR(1)			NOT NULL,
	CONSTRAINT Employees_PK PRIMARY KEY (intEmployeeID)
)

CREATE TABLE EmployeesShifts
(
	intEmployeeShiftID			INTEGER IDENTITY,
	intEmployeeID				INTEGER				NOT NULL,
	intShiftID					INTEGER				NOT NULL,
	dtmShiftStart				DATETIME			NOT NULL,
	dtmShiftEnd					DATETIME			NOT NULL,
	CONSTRAINT EmployeesShifts_PK PRIMARY KEY (intEmployeeShiftID)
)

CREATE TABLE EmployeeTypes
(
	intEmployeeTypeID			INTEGER IDENTITY,
	strEmployeeType				VARCHAR(255)		NOT NULL,
	CONSTRAINT EmployeeTypes_PK PRIMARY KEY (intEmployeeTypeID)
)

CREATE TABLE Orders
(
	intOrderID					INTEGER IDENTITY,
	intTruckID					INTEGER				NOT NULL,
	intSaleID					INTEGER				NOT NULL,
	intCustomerID				INTEGER,
	CONSTRAINT Orders_PK PRIMARY KEY (intOrderID)
)

CREATE TABLE Sales
(
	intSaleID					INTEGER IDENTITY,
	dblSaleAmount				DECIMAL(10, 2)		NOT NULL,
	dtmDate						DATETIME			NOT NULL,
	intSalesPaymentTypeID		INTEGER				NOT NULL,
	CONSTRAINT Sales_PK PRIMARY KEY (intSaleID)
)

CREATE TABLE SalesPaymentTypes
(
	intSalesPaymentTypeID		INTEGER IDENTITY,
	strSalesPaymentType			VARCHAR(10)			NOT NULL,
	CONSTRAINT SalesPaymentType_PK PRIMARY KEY (intSalesPaymentTypeID)
)

CREATE TABLE Customers
(
	intCustomerID				INTEGER IDENTITY,
	strFirstName				VARCHAR(50)			NOT NULL,
	strLastName					VARCHAR(255)		NOT NULL,
	strUserName					VARCHAR(255)		NOT NULL,
	strEmail					VARCHAR(255)		NOT NULL,
	strPassword					VARCHAR(255)		NOT NULL,
	strPhoneNumber				VARCHAR(12)			NOT NULL,
	CONSTRAINT Customers_PK PRIMARY KEY (intCustomerID)
)

CREATE TABLE LoyaltyMembers
(
	intLoyaltyMemberID			INTEGER IDENTITY,
	intCustomerID				INTEGER				NOT NULL,
	intLoyaltyRewardID			INTEGER,
	CONSTRAINT LoyaltyMembers_PK PRIMARY KEY (intLoyaltyMemberID)
)

CREATE TABLE LoyaltyRewards
(
	intLoyaltyRewardID			INTEGER IDENTITY,
	strLoyaltyRewardType		VARCHAR(255)		NOT NULL,
	CONSTRAINT LoyaltyRewards_PK PRIMARY KEY (intLoyaltyRewardID)
)

CREATE TABLE TrucksFoods
(
	intTruckFoodID				INTEGER IDENTITY,
	intTruckID					INTEGER				NOT NULL,
	intFoodID					INTEGER				NOT NULL,
	CONSTRAINT TrucksFoods_PK PRIMARY KEY ( intTruckFoodID )
)

CREATE TABLE TrucksKitchenSupplies
(
	intTruckKitchenSupplyID		INTEGER IDENTITY,
	intTruckID					INTEGER				NOT NULL,
	intKitchenSupplyID			INTEGER				NOT NULL,
	CONSTRAINT TrucksKitchenSupplies_PK PRIMARY KEY ( intTruckKitchenSupplyID )
)

CREATE TABLE Foods 
(
	intFoodID					INTEGER IDENTITY,
	strFoodName					VARCHAR(255)		NOT NULL,
	dblAmount					DECIMAL(5,2)		NOT NULL,
	dblPurchasePrice			DECIMAL(5,2)		NOT NULL,
	dblSellPrice				DECIMAL(3,2)		NOT NULL,
	intFoodTypeID				INTEGER				NOT NULL,
	CONSTRAINT Foods_PK PRIMARY KEY (intFoodID)
)

CREATE TABLE FoodTypes
(
	intFoodTypeID				INTEGER IDENTITY,
	strFoodType					VARCHAR(50)			NOT NULL,
	CONSTRAINT FoodTypes_PK PRIMARY KEY (intFoodTypeID)
)

CREATE TABLE SubMenusFoods
(
	intSubMenuFoodID			INTEGER IDENTITY,
	intSubMenuID				INTEGER				NOT NULL,
	intFoodID					INTEGER				NOT NULL,
	CONSTRAINT SubMenusFoods_PK PRIMARY KEY (intSubMenuFoodID)
)

CREATE TABLE MenuItemsFoods
(
	intMenuItemFoodID			INTEGER IDENTITY,
	intMenuItemID				INTEGER				NOT NULL,
	intFoodID					INTEGER				NOT NULL,
	dblFoodWeight				DECIMAL(5,2)		NOT NULL,
	CONSTRAINT MenuItemsFoods_PK PRIMARY KEY ( intMenuItemFoodID )
)

CREATE TABLE KitchenSupplies
(
	intKitchenSupplyID			INTEGER IDENTITY,
	strKitchenSupplyName		VARCHAR(255)		NOT NULL,
	intAmount					INTEGER				NOT NULL,
	intKitchenSupplyTypeID		INTEGER				NOT NUll,
	CONSTRAINT KitchenSupply_PK PRIMARY KEY (intKitchenSupplyID)
)

CREATE TABLE KitchenSupplyTypes
(
	intKitchenSupplyTypeID		INTEGER IDENTITY,
	strKitchenSupplyTypeName	VARCHAR(255)		NOT NULL,
	CONSTRAINT KitchenSupplyTypes_PK PRIMARY KEY (intKitchenSupplyTypeID)
)


----------------------------------------------------------------------------
-- Foreign Keys
----------------------------------------------------------------------------
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
FOREIGN KEY (intTruckID) REFERENCES Trucks (intTruckID)

-- 2.
ALTER TABLE ORDERS ADD CONSTRAINT Orders_Customers_FK
FOREIGN KEY (intCustomerID) REFERENCES Customers (intCustomerID)

-- 3.
ALTER TABLE Orders ADD CONSTRAINT Orders_Sales_FK
FOREIGN KEY (intSaleID) REFERENCES Sales (intSaleID)

-- 4.
ALTER TABLE Sales ADD CONSTRAINT Sales_SalesPaymentTypes_FK
FOREIGN KEY (intSalesPaymentTypeID) REFERENCES SalesPaymentTypes (intSalesPaymentTypeID)

-- 5.
ALTER TABLE TrucksFoods ADD CONSTRAINT TrucksFoods_Trucks_FK
FOREIGN KEY (intTruckID) REFERENCES Trucks (intTruckID)

-- 6.
ALTER TABLE TrucksFoods ADD CONSTRAINT TrucksFoods_Foods_FK
FOREIGN KEY (intFoodID) REFERENCES Foods (intFoodID)

-- 7.
ALTER TABLE TrucksKitchenSupplies ADD CONSTRAINT TrucksKitchenSupplies_Trucks_FK
FOREIGN KEY (intTruckID) REFERENCES Trucks (intTruckID)

-- 8.
ALTER TABLE TrucksKitchenSupplies ADD CONSTRAINT TrucksKitchenSupplies_KitchenSupplies_FK
FOREIGN KEY (intKitchenSupplyID) REFERENCES KitchenSupplies (intKitchenSupplyID)

-- 9.
ALTER TABLE KitchenSupplies ADD CONSTRAINT KitchenSupplies_KitchenSupplyTypes_FK
FOREIGN KEY (intKitchenSupplyTypeID) REFERENCES KitchenSupplyTypes (intKitchenSupplyTypeID)

-- 10.
ALTER TABLE Foods ADD CONSTRAINT Foods_FoodTypes_FK
FOREIGN KEY (intFoodTypeID) REFERENCES FoodTypes (intFoodTypeID)

-- 11.
ALTER TABLE LoyaltyMembers ADD CONSTRAINT LoyaltyMembers_Customers_FK
FOREIGN KEY (intCustomerID) REFERENCES Customers (intCustomerID)

-- 12.
ALTER TABLE LoyaltyMembers ADD CONSTRAINT LoyaltyMembers_LoyaltyRewards_FK
FOREIGN KEY (intLoyaltyRewardID) REFERENCES LoyaltyRewards (intLoyaltyRewardID)

-- 13.
ALTER TABLE Employees ADD CONSTRAINT Employees_EmployeeTypes_FK
FOREIGN KEY (intEmployeeTypeID) REFERENCES EmployeeTypes (intEmployeeTypeID)

-- 14.
ALTER TABLE EmployeesShifts ADD CONSTRAINT EmployeesShifts_Employees_FK
FOREIGN KEY (intEmployeeID) REFERENCES Employees (intEmployeeID)

-- 15.
ALTER TABLE EmployeesShifts ADD CONSTRAINT EmployeesShifts_Shifts_FK
FOREIGN KEY (intShiftID) REFERENCES Shifts (intShiftID)

-- 16.
ALTER TABLE TrucksShifts ADD CONSTRAINT TrucksShifts_Shifts_FK
FOREIGN KEY (intShiftID) REFERENCES Shifts (intShiftID)

-- 17.
ALTER TABLE TrucksShifts ADD CONSTRAINT TrucksShifts_Trucks_FK
FOREIGN KEY (intTruckID) REFERENCES Trucks (intTruckID)

-- 18.
ALTER TABLE TrucksMenuItems ADD CONSTRAINT TrucksMenuItems_MenuItems_FK
FOREIGN KEY (intMenuItemID) REFERENCES MenuItems (intMenuItemID)

-- 19.
ALTER TABLE TrucksMenuItems ADD CONSTRAINT TrucksMenuItems_Trucks_FK
FOREIGN KEY (intTruckID) REFERENCES Trucks (intTruckID)

-- 20.
ALTER TABLE MenuItems ADD CONSTRAINT MenuItems_MenuItemsTypes_FK
FOREIGN KEY (intMenuItemTypeID) REFERENCES MenuItemsTypes (intMenuItemTypeID)

-- 21.
ALTER TABLE MenuItemsFoods ADD CONSTRAINT MenuItemsFoods_Foods_FK
FOREIGN KEY (intFoodID) REFERENCES Foods (intFoodID)

-- 22.
ALTER TABLE MenuItemsFoods ADD CONSTRAINT MenuItemsFoods_MenuItems_FK
FOREIGN KEY (intMenuItemID) REFERENCES MenuItems (intMenuItemID)

-- 23.
ALTER TABLE MenuItems ADD CONSTRAINT MenuItems_SubMenus_FK
FOREIGN KEY (intSubMenuID) REFERENCES SubMenus (intSubMenuID)

-- 24.
ALTER TABLE SubMenusFoods ADD CONSTRAINT SubMenusFoods_SubMenus_FK
FOREIGN KEY (intSubMenuID) REFERENCES SubMenus (intSubMenuID)

-- 25.
ALTER TABLE SubMenusFoods ADD CONSTRAINT SubMenusFoods_Foods_FK
FOREIGN KEY (intFoodID) REFERENCES Foods (intFoodID)


----------------------------------------------------------------------------
-- Views
----------------------------------------------------------------------------

GO

CREATE VIEW VMenuItems
(
	MenuItemID,
	MenuItemName,
	MenuItemImage,
	MenuItemDescription,
	MenuItemPrice,
	MenuType
)
AS
SELECT
	MI.intMenuItemID,
	MI.strMenuItemName,
	MI.imgMenuItemImage,
	MI.strDescription,
	MI.dblPrice,
	MI.intMenuItemTypeID
	
FROM
	MenuItems AS MI
	
GO

-- TEST VMenuItems
-- SELECT * FROM VMenuItems

CREATE VIEW VTruckName
(
	TruckName
)
AS
SELECT
	strTruckName
FROM
	Trucks

GO

-- TEST VTruckName
-- SELECT * FROM VTruckName

CREATE VIEW VSubMenuItems
(
	SubMenuItem,
	MenuItem
)
AS
SELECT
	F.strFoodName,
	MI.intMenuItemID
FROM
	MenuItems AS MI JOIN SubMenus AS SM
	ON MI.intSubMenuID = SM.intSubMenuID

	JOIN SubMenusFoods AS SMF
	ON SMF.intSubMenuID = SM.intSubMenuID

	JOIN Foods AS F
	ON F.intFoodID = SMF.intFoodID

GO

-- TEST VSubMenuItem
-- SELECT SubMenuItem FROM VSubMenuItems WHERE MenuItem = 1

CREATE VIEW VSubMenuName
(
	SubMenu,
	MenuItem
)
AS
SELECT
	SM.strSubMenuName,
	MI.intMenuItemID
FROM
	SubMenus AS SM JOIN MenuItems AS MI
	ON SM.intSubMenuID = MI.intSubMenuID

GO

-- TEST VSubMenuName
-- SELECT SubMenu FROM VSubMenuName WHERE MenuItem = 1


----------------------------------------------------------------------------
-- Stored Procedures
----------------------------------------------------------------------------
GO

CREATE PROCEDURE uspAddMenuItem
(
	@strMenuItemName VARCHAR(255),
	@imgMenuItemImage VARBINARY(MAX),
	@strDescription VARCHAR(1000),
	@dblPrice DECIMAL(10,2),
	@intMenuItemTypeID INTEGER
)
AS
BEGIN
	
	INSERT INTO MenuItems ( strMenuItemName, imgMenuItemImage, strDescription, dblPrice, intMenuItemTypeID )
	VALUES ( @strMenuItemName, @imgMenuItemImage, @strDescription, @dblPrice, @intMenuItemTypeID )

END

GO

-- TEST uspAddMenuItem
 --EXECUTE uspAddMenuItem 'Chicken Sandwhich', NULL, 'Bun, chicken, and lettuce', 7.50, 1

CREATE PROCEDURE uspAddCompanyDetails
(
	@intTruckNumber INTEGER,
	@strCompanyName VARCHAR(255),
	@imgCompanyLogo VARBINARY(MAX)
)
AS
BEGIN

	INSERT INTO Trucks ( intTruckNumber, strTruckName, imgCompanyLogo )
	VALUES ( @intTruckNumber, @strCompanyName, @imgCompanyLogo )

END

GO

-- TEST uspAddCompanyDetails
--EXECUTE uspAddCompanyDetails 2, 'SuperTruck2', NULL
--SELECT * FROM Trucks
--DELETE FROM Trucks WHERE intTruckID = 2


----------------------------------------------------------------------------
-- Functions
----------------------------------------------------------------------------

GO

CREATE FUNCTION fnEmployeeLogin
(
	@strLastName VARCHAR(255),
	@strPassword VARCHAR(255)
)
RETURNS INTEGER
AS
BEGIN

	DECLARE @intUID INTEGER

	SELECT @intUID = intEmployeeID
	FROM
		Employees
	WHERE
		strLastName = @strLastName
	AND strPassword = @strPassword

	RETURN @intUID

END

GO


----------------------------------------------------------------------------
-- Insert Statements
----------------------------------------------------------------------------
-- Number to the right of each record is the primary key index of that
-- record in the relative table.

INSERT INTO EmployeeTypes ( strEmployeeType )
VALUES  ( 'cashier' ),		-- 1
	    ( 'manager' ),		-- 2
	    ( 'cook' )			-- 3

INSERT INTO Employees ( strFirstName, strLastName, strUserName, strPassword, dblHourlyRate, 
						intEmployeeTypeID, strLicensedToDrive )
VALUES	( 'Cole', 'Whitaker', 'CW', 'test1', 20.50, 2, 'Y' ),		-- 1
		( 'Adam', 'Broderick', 'AB', 'test1', 20.50, 2, 'Y' ),		-- 2
		( 'Jason', 'Cope', 'JC', 'test1', 20.50, 2, 'Y' ),			-- 3
		( 'Bruce', 'Wayne', 'BW', 'test1', 18.75, 3, 'N' ),			-- 4
		( 'Clark', 'Kent', 'CK', 'test1', 18.75, 3, 'Y' ),			-- 5
		( 'Oliver', 'Queen', 'OQ', 'test1', 18.75, 3, 'N' ),		-- 6
		( 'Barry', 'Allen', 'BA', 'test1', 18.75, 1, 'Y' ),			-- 7
		( 'Barbara', 'Gordon', 'BG', 'test1', 18.75, 1, 'N' ),		-- 8
		( 'Harvey', 'Dent', 'HD', 'test1', 18.75, 1, 'Y' )			-- 9

INSERT INTO Shifts ( dtmShiftDate )
VALUES	( '2025-07-01' ),		-- 1
		( '2025-07-02' ),		-- 2
		( '2025-07-03' )		-- 3

INSERT INTO EmployeesShifts ( intEmployeeID, intShiftID, dtmShiftStart, dtmShiftEnd )
VALUES	( 1, 1, '2025-07-01 08:00:00', '2025-07-01 16:00:00' ),		-- 1
		( 4, 1, '2025-07-01 08:00:00', '2025-07-01 16:00:00' ),		-- 2
		( 9, 1, '2025-07-01 08:00:00', '2025-07-01 16:00:00' ),		-- 3
		( 2, 2, '2025-07-02 08:00:00', '2025-07-02 16:00:00' ),		-- 4
		( 5, 2, '2025-07-02 08:00:00', '2025-07-02 16:00:00' ),		-- 5
		( 7, 2, '2025-07-02 08:00:00', '2025-07-02 16:00:00' ),		-- 6
		( 3, 3, '2025-07-03 08:00:00', '2025-07-03 16:00:00' ),		-- 7
		( 6, 3, '2025-07-03 08:00:00', '2025-07-03 16:00:00' ),		-- 8
		( 8, 3, '2025-07-03 08:00:00', '2025-07-03 16:00:00' )		-- 9

INSERT INTO Trucks ( intTruckNumber, strTruckName, imgCompanyLogo )
VALUES	( 1, 'SuperTruck', NULL )		-- 1

INSERT INTO TrucksShifts ( intShiftID, intTruckID )
VALUES	( 1, 1 ),	-- 1
		( 2, 1 ),	-- 2
		( 3, 1 )	-- 3

INSERT INTO LoyaltyRewards ( strLoyaltyRewardType )
VALUES  ( '10% off' ),			-- 1
		( '15% off' ),			-- 2
		( '1 free drink' )		-- 3

INSERT INTO Customers ( strFirstName, strLastName, strUserName, strEmail, strPassword, strPhoneNumber )
VALUES	( 'Hal', 'Jordan', 'GreenLantern', 'hjordan@gmail.com', 'test2', '513-111-1111' ),		-- 1
		( 'Lex', 'Luthor', 'EvilGuy', 'lluthor@gmail.com', 'test2', '513-222-2222' ),			-- 2
		( 'Jason', 'Todd', 'RedHood', 'jtodd@gmail.com', 'test2', '513-333-3333' )				-- 3

INSERT INTO LoyaltyMembers ( intCustomerID, intLoyaltyRewardID )
VALUES	( 1, NULL ),	-- 1
		( 2, 2 ),		-- 2
		( 3, 3 )		-- 3

INSERT INTO SalesPaymentTypes ( strSalesPaymentType )
VALUES	( 'cash' ),		-- 1
		( 'card' )		-- 2

INSERT INTO Sales ( dblSaleAmount, dtmDate, intSalesPaymentTypeID )
VALUES	( 30.50, '2025-07-01 09:00:00', 1 ),		-- 1
		( 10.50, '2025-07-01 10:00:00', 1 ),		-- 2
		( 22.50, '2025-07-01 11:00:00', 2 ),		-- 3
		( 7.25, '2025-07-01 12:00:00', 1 ),			-- 4
		( 28.75, '2025-07-01 13:00:00', 2 ),		-- 5
		( 21.50, '2025-07-02 09:00:00', 1 ),		-- 6
		( 4.50, '2025-07-02 10:00:00', 1 ),			-- 7
		( 14.25, '2025-07-02 11:00:00', 1 ),		-- 8
		( 25.15, '2025-07-02 12:00:00', 2 ),		-- 9
		( 2.50, '2025-07-02 13:00:00', 1 ),			-- 10
		( 17.50, '2025-07-03 09:00:00', 2 ),		-- 11
		( 31.75, '2025-07-03 10:00:00', 2 ),		-- 12
		( 11.60, '2025-07-03 11:00:00', 1 ),		-- 13
		( 18.50, '2025-07-03 12:00:00', 2 ),		-- 14
		( 6.30, '2025-07-03 13:00:00', 1 )			-- 15

INSERT INTO Orders ( intTruckID, intSaleID, intCustomerID )
VALUES	( 1, 1, NULL ),		-- 1
		( 1, 2, 1 ),		-- 2
		( 1, 3, NULL ),		-- 3
		( 1, 4, NULL ),		-- 4
		( 1, 5, 2 ),		-- 5
		( 1, 6, NULL ),		-- 6
		( 1, 7, 3 ),		-- 7
		( 1, 8, 1 ),		-- 8
		( 1, 9, NULL ),		-- 9
		( 1, 10, NULL ),	-- 10
		( 1, 11, NULL ),	-- 11
		( 1, 12, 2 ),		-- 12
		( 1, 13, NULL ),	-- 13
		( 1, 14, NULL ),	-- 14
		( 1, 15, 3 )		-- 15

INSERT INTO KitchenSupplyTypes ( strKitchenSupplyTypeName )
VALUES	( 'Utensils' ),					-- 1
		( 'Cookingware' ),				-- 2		
		( 'Serving Containers' ),		-- 3
		( 'Paper goods' ),				-- 4
		( 'Cups' ),						-- 5
		( 'Straws' ),					-- 6
		( 'Plasticware' )				-- 7

INSERT INTO KitchenSupplies ( strKitchenSupplyName, intAmount, intKitchenSupplyTypeID )
VALUES	( 'Tongs', 6, 1 ),								-- 1
		( 'Spatula', 4, 1 ),							-- 2
		( 'Slotted Turner', 4, 1 ),						-- 3
		( 'Chef Knife', 3, 1 ),							-- 4
		( 'Pizza Cutter', 2, 1 ),						-- 5
		( 'Pizza Peel', 1, 1 ),							-- 6
		( 'Sauce Pan', 2, 2 ),							-- 7
		( 'Stock Pot', 3, 2 ),							-- 8
		( 'Saute Pan', 3, 2 ),							-- 9
		( 'Pizza Box', 30, 3 ),							-- 10
		( 'Food Boat', 200, 3 ),						-- 11
		( 'Paper Towel Roll', 12, 4 ),					-- 12
		( 'Napkins', 500, 4 ),							-- 13
		( '8oz Plastic Cups', 200, 5 ),					-- 14
		( '12oz Plastic Cups', 150, 5 ),				-- 15
		( '20oz Plastic Cups', 100, 5 ),				-- 16
		( '7.75in Paper Wrapped Straw', 500, 6 ),		-- 17
		( 'Plastic Fork', 300, 7 ),						-- 18
		( 'Plastic Spoon', 100, 7 ),					-- 19
		( 'Plastic Knife', 200, 7 )						-- 20

INSERT INTO TrucksKitchenSupplies ( intTruckID, intKitchenSupplyID )
VALUES  ( 1, 1 ),		-- 1
		( 1, 2 ),		-- 2
		( 1, 3 ),		-- 3
		( 1, 4 ),		-- 4
		( 1, 5 ),		-- 5
		( 1, 6 ),		-- 6
		( 1, 7 ),		-- 7
		( 1, 8 ),		-- 8
		( 1, 9 ),		-- 9
		( 1, 10 ),		-- 10
		( 1, 11 ),		-- 11
		( 1, 12 ),		-- 12
		( 1, 13 ),		-- 13
		( 1, 14 ),		-- 14
		( 1, 15 ),		-- 15
		( 1, 16 ),		-- 16
		( 1, 17 ),		-- 17
		( 1, 18 ),		-- 18
		( 1, 19 ),		-- 19
		( 1, 20 )		-- 20

INSERT INTO FoodTypes ( strFoodType )
VALUES	( 'Meats' ),			-- 1
		( 'Veggies' ),			-- 2
		( 'Drinks' ),			-- 3
		( 'Breads' ),			-- 4
		( 'Cheeses' ),			-- 5
		( 'Seasonings' ),		-- 6
		( 'Sauce' ),			-- 7
		( 'Condiments' ),		-- 8
		( 'Other' )				-- 9

INSERT INTO SubMenus ( strSubMenuName )
VALUES  ( 'Burgers' ),		-- 1
		( 'Tacos' ),		-- 2
		( 'Pizzas' ),		-- 3
		( 'Hotdogs' )		-- 4

INSERT INTO Foods ( strFoodName, dblAmount, dblPurchasePrice, dblSellPrice, intFoodTypeID )
VALUES	( 'Chicken', 20, 100, 1.88, 1 ),							-- 1
		( 'Ground Beef', 20, 60, 1.13, 1 ),							-- 2
		( 'Hamburger Patty', 10, 35, 3.50, 1 ),						-- 3
		( 'Hotdog', 10, 25, 1.50, 1 ),								-- 4
		( 'Shredded Lettuce', 10, 10, 0.10, 2 ),					-- 5
		( 'Lettuce Leaf', 10, 10, 0.15, 2 ),						-- 6
		( 'Diced Tomato', 10, 12, 0.11, 2 ),						-- 7
		( 'Sliced Tomato', 10, 12, 0.25, 2 ),						-- 8
		( 'Potatoes', 25, 30, 0.20, 2 ),							-- 9
		( 'Burger Bun', 30, 12, 0.50, 4 ),							-- 10
		( 'Hot Dog Bun', 4.8, 14, 0.40, 4 ),                        -- 11
		( 'Tortilla', 6.25, 15, 0.30, 4 ),							-- 12
		( 'Cheddar Cheese', 5, 20, 0.75, 5 ),						-- 13
		( 'Mozzarella Cheese', 5, 18, 0.45, 5 ),					-- 14
		( 'Pizza Dough Ball', 20, 22, 1.50, 4 ),					-- 15
		( 'Pizza Sauce', 10, 10, 0.30, 7 ),							-- 16
		( 'Pepperoni', 5, 14, 0.60, 1 ),							-- 17
		( 'Sausage Crumble', 5, 16, 0.65, 1 ),						-- 18
		( 'Onions', 10, 8, 0.10, 2 ),								-- 19
		( 'Pickles', 5, 6, 0.10, 2 ),								-- 20
		( 'Ketchup', 3, 4, 0.10, 8 ),								-- 21
		( 'Mustard', 3, 4, 0.10, 8 ),								-- 22
		( 'Mayonnaise', 3, 4, 0.10, 8 ),							-- 23
		( 'Coca-Cola Syrup (5 gal box)', 640, 95, 0.25, 3 ),		-- 24
		( 'Dr. Pepper Syrup (5 gal box)', 640, 95, 0.25, 3 ),		-- 25
		( 'Lemonade Mix (1 gal)', 128, 8, 0.08, 3 ),				-- 26
		( 'Bottled Water (16.9oz)', 24, 10, 1.00, 3 ),				-- 27
		( 'Blue Powerade Mix (1 gal)', 128, 9, 0.10, 3 );			-- 28

INSERT INTO SubMenusFoods ( intSubMenuID, intFoodID )
VALUES	
		-- Burger Toppings
		( 1, 10 ),		-- 1
		( 1, 8 ),		-- 2
		( 1, 13 ),		-- 3
		( 1, 6 ),		-- 4
		( 1, 19 ),		-- 5
		( 1, 20 ),		-- 6
		( 1, 21 ),		-- 7
		( 1, 22 ),		-- 8
		( 1, 23 ),		-- 9

		-- Taco Toppings
		( 2, 12 ),		-- 10
		( 2, 1 ),		-- 11
		( 2, 2 ),		-- 12
		( 2, 5 ),		-- 13
		( 2, 7 ),		-- 14
		( 2, 13 ),		-- 15
		( 2, 19 ),		-- 16

		-- Pizza Toppings
		( 3, 15 ),		-- 17
		( 3, 16 ),		-- 18
		( 3, 14 ),		-- 19
		( 3, 2 ),		-- 20
		( 3, 17 ),		-- 21
		( 3, 18 ),		-- 22
		( 3, 8 ),		-- 23
		( 3, 19 ),		-- 24

		-- Hotdog toppings
		( 4, 11 ),		-- 25
		( 4, 4 ),		-- 26
		( 4, 21 ),		-- 27
		( 4, 22 )		-- 28
 
INSERT INTO TrucksFoods ( intTruckID, intFoodID )
VALUES	( 1, 1 ),		-- 1
		( 1, 2 ),		-- 2
		( 1, 3 ),		-- 3
		( 1, 4 ),		-- 4
		( 1, 5 ),		-- 5
		( 1, 6 ),		-- 6
		( 1, 7 ),		-- 7
		( 1, 8 ),		-- 8
		( 1, 9 ),		-- 9
		( 1, 10 ),		-- 10
		( 1, 11 ),		-- 11
		( 1, 12 ),		-- 12
		( 1, 13 ),		-- 13
		( 1, 14 ),		-- 14
		( 1, 15 ),		-- 15
		( 1, 16 ),		-- 16
		( 1, 17 ),		-- 17
		( 1, 18 ),		-- 18
		( 1, 19 ),		-- 19
		( 1, 20 ),		-- 20
		( 1, 21 ),		-- 21
		( 1, 22 ),		-- 22
		( 1, 23 ),		-- 23
		( 1, 24 ),		-- 24
		( 1, 25 ),		-- 25
		( 1, 26 ),		-- 26
		( 1, 27 )		-- 27

INSERT INTO MenuItemsTypes ( strMenuItemType )
VALUES	( 'Mains' ),			-- 1
		( 'Sides' ),			-- 2
		( 'Drinks' )			-- 3

INSERT INTO MenuItems ( strMenuItemName, imgMenuItemImage, intMenuItemTypeID, strDescription, dblPrice, intSubMenuID )
VALUES	( 'Burger', NULL, 1, 'Burger with bun, patty, cheese, lettuce, tomato, onion, ketchup, mustard, and mayonnaise', 9.50, 1 ),		-- 1
		( 'Chicken Taco', NULL, 1, 'Taco with tortialla, chicken, lettuce, and tomato', 3.25, 2 ),										-- 2
		( 'Beef Taco', NULL, 1, 'Taco with tortilla, beef, lettuce, and tomato', 3.00, 2 ),												-- 3
		( 'Fries', NULL, 2, NULL, 1.50, NULL ),																							-- 4
		( 'Cheese Pizza', NULL, 1, 'Pizza with dough, sauce, and cheese', 7.00, 3 ),													-- 5
		( 'Veggie Pizza', NULL, 1, 'Pizza with dough, sauce, cheese, tomato, and onion', 9.00, 3 ),										-- 6
		( 'Sausage & Pepperoni Pizza', NULL, 1, 'Pizza with dough, sauce, cheese, sausage, and pepperoni', 11.00, 3 ),					-- 7
		( 'Hotdog', NULL, 1, 'Hotdog bun, hotdog, ketchup, and mustard', 3.50, 4 ),														-- 8
		( 'Coca-Cola', NULL, 3, NULL, 1.50, NULL ),																						-- 9
		( 'Dr. Pepper', NULL, 3, NULL, 1.50, NULL ),																					-- 10
		( 'Lemonade', NULL, 3, NULL, 1.75, NULL ),																						-- 11
		( 'Water', NULL, 3, NULL, 1.25, NULL ),																							-- 12
		( 'Blue Powerade', NULL, 3, NULL, 1.50, NULL )																					-- 13

INSERT INTO MenuItemsFoods ( intMenuItemID, intFoodID, dblFoodWeight )
VALUES
		-- Burger (MenuItemID 1)
		( 1, 3, 0.25 ),			-- 1 -- Hamburger Patty (4 oz)
		( 1, 10, 0.25 ),		-- 2 -- Burger Bun (~0.25 lb)
		( 1, 6, 0.05 ),			-- 3 -- Lettuce Leaf (0.75 oz)
		( 1, 8, 0.06 ),			-- 4 -- Sliced Tomato (1 oz)
		( 1, 13, 0.06 ),		-- 5 -- Cheddar Cheese (1 oz)
		( 1, 20, 0.03 ),		-- 6 -- Pickles (0.5 oz)
		( 1, 21, 0.02 ),		-- 7 -- Ketchup (0.25 oz)
		( 1, 22, 0.02 ),		-- 8 -- Mustard (0.25 oz)
		( 1, 23, 0.02 ),		-- 9 -- Mayonnaise (0.25 oz)

		-- Chicken Taco (MenuItemID 2)
		( 2, 1, 0.13 ),			-- 10 -- Chicken (2 oz)
		( 2, 12, 0.25 ),		-- 11 -- Tortilla (~0.25 lb)
		( 2, 5, 0.031 ),		-- 12 -- Shredded Lettuce (0.5 oz)
		( 2, 7, 0.031 ),		-- 13 -- Diced Tomato (0.5 oz)
		( 2, 13, 0.05 ),		-- 14 -- Cheddar Cheese (0.75 oz)

		-- Beef Taco (MenuItemID 3)
		( 3, 2, 0.13 ),			-- 15 -- Ground Beef (2 oz)
		( 3, 12, 0.25 ),		-- 16 -- Tortilla (~0.25 lb)
		( 3, 5, 0.031 ),		-- 17 -- Shredded Lettuce (0.5 oz)
		( 3, 7, 0.031 ),		-- 18 -- Diced Tomato (0.5 oz)
		( 3, 13, 0.05 ),		-- 19 -- Cheddar Cheese (0.75 oz)

		-- Fries (MenuItemID 4)
		( 4, 9, 0.31 ),			-- 20 -- Potatoes (5 oz)

		-- Cheese Pizza (MenuItemID 5)
		( 5, 15, 0.25 ),		-- 21 -- Pizza Dough Ball (~0.25 lb)
		( 5, 16, 0.19 ),		-- 22 -- Pizza Sauce (3 oz)
		( 5, 14, 0.19 ),		-- 23 -- Mozzarella Cheese (3 oz)

		-- Veggie Pizza (MenuItemID 6)
		( 6, 15, 0.25 ),		-- 24 -- Pizza Dough Ball (~0.25 lb)
		( 6, 16, 0.19 ),		-- 25 -- Pizza Sauce (3 oz)
		( 6, 14, 0.16 ),		-- 26 -- Mozzarella Cheese (2.5 oz)
		( 6, 7, 0.06 ),			-- 27 -- Diced Tomato (1 oz)
		( 6, 19, 0.06 ),		-- 28 -- Onions (1 oz)

		-- Sausage & Pepperoni Pizza (MenuItemID 7)
		( 7, 15, 0.25 ),		-- 29 -- Pizza Dough Ball (~0.25 lb)
		( 7, 16, 0.19 ),		-- 30 -- Pizza Sauce (3 oz)
		( 7, 14, 0.19 ),		-- 31 -- Mozzarella Cheese (3 oz)
		( 7, 17, 0.13 ),		-- 32 -- Pepperoni (2 oz)
		( 7, 18, 0.13 ),		-- 33 -- Sausage Crumble (2 oz)

		-- Hotdog (MenuItemID 8)
		( 8, 11, 0.25 ),		-- 34 -- Hot Dog Bun (~0.25 lb)
		( 8, 4, 0.15 ),			-- 35 -- Hotdog (~0.15 lb)
		( 8, 21, 0.02 ),		-- 35 -- Ketchup (0.25 oz)
		( 8, 22, 0.02 ),		-- 36 -- Mustard (0.25 oz)

		-- Coca-Cola (MenuItemID 9)
		( 9, 24, 0.75 ),		-- 37 -- Coca-Cola Syrup (12 oz)

	    -- Dr. Pepper (MenuItemID 10)
		( 10, 25, 0.75 ),		-- 38 -- Dr. Pepper Syrup (12 oz)

		-- Lemonade (MenuItemID 11)
		( 11, 26, 0.5 ),		-- 39 -- Lemonade Mix (8 oz)

		-- Water (MenuItemID 12)
		( 12, 27, 1.00 ),		-- 40 -- Bottled Water (16 oz bottle)

		-- Blue Powerade (MenuItemID 13)
		( 13, 28, 1.25 );		-- 41 -- Blue Powerade Mix (20 oz)

INSERT INTO TrucksMenuItems ( intTruckID, intMenuItemID )
VALUES	( 1, 1 ),	-- 1
		( 1, 2 ),	-- 2
		( 1, 3 ),	-- 3
		( 1, 4 ),	-- 4
		( 1, 5 ),	-- 5
		( 1, 6 ),	-- 6
		( 1, 7 ),	-- 7
		( 1, 8 ),	-- 8
		( 1, 9 ),	-- 9
		( 1, 10 ),	-- 10
		( 1, 11 ),	-- 11
		( 1, 12 ),	-- 12
		( 1, 13 )	-- 13