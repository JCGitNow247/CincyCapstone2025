----------------------------------------------------------------------------
-- Options
----------------------------------------------------------------------------
USE dbTruckBytes
SET NOCOUNT ON

----------------------------------------------------------------------------
-- DROP Statements
----------------------------------------------------------------------------

IF OBJECT_ID('uspAddMenuItem')		 IS NOT NULL DROP PROCEDURE uspAddMenuItem
IF OBJECT_ID('uspAddCompanyDetails') IS NOT NULL DROP PROCEDURE uspAddCompanyDetails

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
