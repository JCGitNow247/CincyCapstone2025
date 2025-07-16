----------------------------------------------------------------------------
-- Options
----------------------------------------------------------------------------
USE dbTruckBytes
SET NOCOUNT ON

----------------------------------------------------------------------------
-- DROP Statements
----------------------------------------------------------------------------
IF OBJECT_ID('VMenuItems') IS NOT NULL DROP VIEW VMenuItems
IF OBJECT_ID('VTruckName') IS NOT NULL DROP VIEW VTruckName
IF OBJECT_ID('VSubMenuItems') IS NOT NULL DROP VIEW VSubMenuItems

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
SELECT SubMenu FROM VSubMenuName WHERE MenuItem = 1