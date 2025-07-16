----------------------------------------------------------------------------
-- Options
----------------------------------------------------------------------------
USE dbTruckBytes
SET NOCOUNT ON

----------------------------------------------------------------------------
-- DROP Statements
----------------------------------------------------------------------------
IF OBJECT_ID('fnEmployeeLogin') IS NOT NULL DROP FUNCTION fnEmployeeLogin

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