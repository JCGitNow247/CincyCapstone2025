----------------------------------------------------------------------------
-- Options
----------------------------------------------------------------------------
USE dbTruckBytes
SET NOCOUNT ON

----------------------------------------------------------------------------
-- Notes
----------------------------------------------------------------------------
-- Number to the right of each record is the primary key index of that
-- record in the relative table.

----------------------------------------------------------------------------
-- Insert Statements
----------------------------------------------------------------------------
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

INSERT INTO Trucks ( intTruckNumber, strTruckName )
VALUES	( 1, 'SuperTruck' )		-- 1

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

INSERT INTO Foods ( strFoodName, dblAmount, dblPurchasePrice, dblSellPrice, intFoodTypeID )
VALUES	( 'Chicken', 20, 100, 1.88, 1 ),							-- 1
		( 'Ground Beef', 20, 60, 1.13, 1 ),							-- 2
		( 'Hamburger Patty', 10, 35, 3.50, 1 ),						-- 3
		( 'Shredded Lettuce', 10, 10, 0.10, 2 ),					-- 4
		( 'Lettuce Leaf', 10, 10, 0.15, 2 ),						-- 5
		( 'Diced Tomato', 10, 12, 0.10, 2 ),						-- 6
		( 'Sliced Tomato', 10, 12, 0.25, 2 ),						-- 7
		( 'Potatoes', 25, 30, 0.20, 2 ),							-- 8
		( 'Burger Bun', 30, 12, 0.50, 4 ),							-- 9
		( 'Hot Dog Bun', 4.8, 14, 0.40, 4 ),                        -- 10
		( 'Tortilla', 6.25, 15, 0.40, 4 ),							-- 11
		( 'Cheddar Cheese', 5, 20, 0.50, 5 ),						-- 12
		( 'Mozzarella Cheese', 5, 18, 0.45, 5 ),					-- 13
		( 'Pizza Dough Ball', 20, 22, 1.50, 4 ),					-- 14
		( 'Pizza Sauce', 10, 10, 0.30, 7 ),							-- 15
		( 'Pepperoni', 5, 14, 0.60, 1 ),							-- 16
		( 'Sausage Crumble', 5, 16, 0.65, 1 ),						-- 17
		( 'Onions', 10, 8, 0.10, 2 ),								-- 18
		( 'Pickles', 5, 6, 0.10, 2 ),								-- 19
		( 'Ketchup', 3, 4, 0.10, 8 ),								-- 20
		( 'Mustard', 3, 4, 0.10, 8 ),								-- 21
		( 'Mayonnaise', 3, 4, 0.10, 8 ),							-- 22
		( 'Coca-Cola Syrup (5 gal box)', 640, 95, 0.25, 3 ),		-- 23
		( 'Dr. Pepper Syrup (5 gal box)', 640, 95, 0.25, 3 ),		-- 24
		( 'Lemonade Mix (1 gal)', 128, 8, 0.08, 3 ),				-- 25
		( 'Bottled Water (16.9oz)', 24, 10, 1.00, 3 ),				-- 26
		( 'Blue Powerade Mix (1 gal)', 128, 9, 0.10, 3 );			-- 27

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

INSERT INTO MenuItems ( strMenuItemName, imgMenuItemImage, intMenuItemTypeID )
VALUES	( 'Burger', NULL, 1 ),							-- 1
		( 'Chicken Taco', NULL, 1 ),					-- 2
		( 'Beef Taco', NULL, 1 ),						-- 3
		( 'Fries', NULL, 2 ),							-- 4
		( 'Cheese Pizza', NULL, 1 ),					-- 5
		( 'Veggie Pizza', NULL, 1 ),					-- 6
		( 'Sausage & Pepperoni Pizza', NULL, 1 ),		-- 7
		( 'Hotdog', NULL, 1 ),							-- 8
		( 'Coca-Cola', NULL, 3 ),						-- 9
		( 'Dr. Pepper', NULL, 3 ),						-- 10
		( 'Lemonade', NULL, 3 ),						-- 11
		( 'Water', NULL, 3 ),							-- 12
		( 'Blue Powerade', NULL, 3 )					-- 13

INSERT INTO MenuItemsFoods ( intMenuItemID, intFoodID, dblFoodWeight )
VALUES
    -- Burger (MenuItemID 1)
    ( 1, 3, 0.25 ),			-- 1 -- Hamburger Patty (4 oz)
    ( 1, 9, 0.25 ),			-- 2 -- Burger Bun (~0.25 lb)
    ( 1, 5, 0.05 ),			-- 3 -- Lettuce Leaf (0.75 oz)
    ( 1, 7, 0.06 ),			-- 4 -- Sliced Tomato (1 oz)
    ( 1, 12, 0.06 ),		-- 5 -- Cheddar Cheese (1 oz)
    ( 1, 19, 0.03 ),		-- 6 -- Pickles (0.5 oz)
    ( 1, 20, 0.02 ),		-- 7 -- Ketchup (0.25 oz)
    ( 1, 21, 0.02 ),		-- 8 -- Mustard (0.25 oz)
    ( 1, 22, 0.02 ),		-- 9 -- Mayonnaise (0.25 oz)

    -- Chicken Taco (MenuItemID 2)
    ( 2, 1, 0.13 ),			-- 10 -- Chicken (2 oz)
    ( 2, 11, 0.25 ),		-- 11 -- Tortilla (~0.25 lb)
    ( 2, 4, 0.031 ),		-- 12 -- Shredded Lettuce (0.5 oz)
    ( 2, 6, 0.031 ),		-- 13 -- Diced Tomato (0.5 oz)
    ( 2, 12, 0.05 ),		-- 14 -- Cheddar Cheese (0.75 oz)

    -- Beef Taco (MenuItemID 3)
    ( 3, 2, 0.13 ),			-- 15 -- Ground Beef (2 oz)
    ( 3, 11, 0.25 ),		-- 16 -- Tortilla (~0.25 lb)
    ( 3, 4, 0.031 ),		-- 17 -- Shredded Lettuce (0.5 oz)
    ( 3, 6, 0.031 ),		-- 18 -- Diced Tomato (0.5 oz)
    ( 3, 12, 0.05 ),		-- 19 -- Cheddar Cheese (0.75 oz)

    -- Fries (MenuItemID 4)
    ( 4, 8, 0.31 ),			-- 20 -- Potatoes (5 oz)

    -- Cheese Pizza (MenuItemID 5)
    ( 5, 14, 0.25 ),		-- 21 -- Pizza Dough Ball (~0.25 lb)
    ( 5, 15, 0.19 ),		-- 22 -- Pizza Sauce (3 oz)
    ( 5, 13, 0.19 ),		-- 23 -- Mozzarella Cheese (3 oz)

    -- Veggie Pizza (MenuItemID 6)
    ( 6, 14, 0.25 ),		-- 24 -- Pizza Dough Ball (~0.25 lb)
    ( 6, 15, 0.19 ),		-- 25 -- Pizza Sauce (3 oz)
    ( 6, 13, 0.16 ),		-- 26 -- Mozzarella Cheese (2.5 oz)
    ( 6, 6, 0.06 ),			-- 27 -- Diced Tomato (1 oz)
    ( 6, 18, 0.06 ),		-- 28 -- Onions (1 oz)

    -- Sausage & Pepperoni Pizza (MenuItemID 7)
    ( 7, 14, 0.25 ),		-- 29 -- Pizza Dough Ball (~0.25 lb)
    ( 7, 15, 0.19 ),		-- 30 -- Pizza Sauce (3 oz)
    ( 7, 13, 0.19 ),		-- 31 -- Mozzarella Cheese (3 oz)
    ( 7, 16, 0.13 ),		-- 32 -- Pepperoni (2 oz)
    ( 7, 17, 0.13 ),		-- 33 -- Sausage Crumble (2 oz)

    -- Hotdog (MenuItemID 8)
    ( 8, 10, 0.25 ),		-- 34 -- Hot Dog Bun (~0.25 lb)
    ( 8, 20, 0.02 ),		-- 35 -- Ketchup (0.25 oz)
    ( 8, 21, 0.02 ),		-- 36 -- Mustard (0.25 oz)

    -- Coca-Cola (MenuItemID 9)
    ( 9, 23, 0.75 ),		-- 37 -- Coca-Cola Syrup (12 oz)

    -- Dr. Pepper (MenuItemID 10)
    ( 10, 24, 0.75 ),		-- 38 -- Dr. Pepper Syrup (12 oz)

    -- Lemonade (MenuItemID 11)
    ( 11, 25, 0.5 ),		-- 39 -- Lemonade Mix (8 oz)

    -- Water (MenuItemID 12)
    ( 12, 26, 1.00 ),		-- 40 -- Bottled Water (16 oz bottle)

    -- Blue Powerade (MenuItemID 13)
    ( 13, 27, 1.25 );		-- 41 -- Blue Powerade Mix (20 oz)

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