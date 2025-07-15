----------------------------------------------------------------------------
-- Options
----------------------------------------------------------------------------
USE dbTruckBytes
SET NOCOUNT ON

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

-- EXECUTE uspAddMenuItem 'Chicken Sandwhich', NULL, 'Bun, chicken, and lettuce', 7.50, 1
