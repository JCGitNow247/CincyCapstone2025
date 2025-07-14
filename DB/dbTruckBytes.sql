----------------------------------------------------------------------------
-- Options
----------------------------------------------------------------------------
USE dbTruckBytes
SET NOCOUNT ON

----------------------------------------------------------------------------
-- Drop Statements
----------------------------------------------------------------------------
IF OBJECT_ID('Orders')					IS NOT NULL DROP TABLE Orders
IF OBJECT_ID('EmployeesShifts')			IS NOT NULL DROP TABLE EmployeesShifts
IF OBJECT_ID('TrucksShifts')			IS NOT NULL DROP TABLE TrucksShifts
IF OBJECT_ID('TrucksMenuItems')			IS NOT NULL DROP TABLE TrucksMenuItems
IF OBJECT_ID('TrucksKitchenSupplies')	IS NOT NULL DROP TABLE TrucksKitchenSupplies
IF OBJECT_ID('MenuItemsFoods')			IS NOT NULL DROP TABLE MenuItemsFoods
IF OBJECT_ID('TrucksFoods')				IS NOT NULL DROP TABLE TrucksFoods
IF OBJECT_ID('Trucks')					IS NOT NULL DROP TABLE Trucks
IF OBJECT_ID('MenuItems')				IS NOT NULL DROP TABLE MenuItems
IF OBJECT_ID('MenuItemsTypes')			IS NOT NULL DROP TABLE MenuItemsTypes
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
-- Create Tables
----------------------------------------------------------------------------
CREATE TABLE Trucks
(
	intTruckID					INTEGER IDENTITY,
	intTruckNumber				INTEGER				NOT NULL,
	strTruckName				VARCHAR(255)		NOT NULL,
	CONSTRAINT Trucks_PK PRIMARY KEY (intTruckID)
)

CREATE TABLE MenuItems
(
	intMenuItemID				INTEGER IDENTITY,
	strMenuItemName				VARCHAR(255)		NOT NULL,
	imgMenuItemImage			VARBINARY(MAX),
	intMenuItemTypeID			INTEGER				NOT NULL,
	strDescription				VARCHAR(100),
	dblPrice					DECIMAL(10,2)		NOT NULL,
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