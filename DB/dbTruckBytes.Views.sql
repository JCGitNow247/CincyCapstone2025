----------------------------------------------------------------------------
-- Options
----------------------------------------------------------------------------
USE dbTruckBytes
SET NOCOUNT ON

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
	MenuItemPrice
)
AS
SELECT
	MI.intMenuItemID,
	MI.strMenuItemName,
	MI.imgMenuItemImage,
	MI.strDescription,
	MI.dblPrice
	
FROM
	MenuItems AS MI
	
GO

SELECT * FROM VMenuItems

IF OBJECT_ID('VMenuItems') IS NOT NULL DROP VIEW VMenuItems