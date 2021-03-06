
-- DROP TABLE main_food_desc;
-- CREATE TABLE main_food_desc(
    -- foodcode int PRIMARY KEY, 
    -- start_date date,
    -- end_date date,
    -- main_food_desc varchar(200),
    -- fortification_id int,
    -- empty varchar(1)
-- );

-- \copy main_food_desc from '/home/andrea/Documents/calcount/fndds/MainFoodDesc.txt' (delimiter '^');


-- DROP TABLE nut_vals;
-- CREATE TABLE nut_vals(
    -- foodcode int,
    -- nutcode int,
    -- start_date date,
    -- end_date date,
    -- nutval numeric,
    -- empty varchar(1)
-- );

-- \copy nut_vals from '/home/andrea/Documents/calcount/fndds/FNDDSNutVal.txt' (delimiter '^');


-- DROP TABLE nut_desc;
-- CREATE TABLE nut_desc(
    -- nutcode int,
    -- nut_desc varchar(45),
    -- tagname varchar(15),
    -- unit varchar(10),
    -- decimals int,
    -- empty varchar(1)
-- );

-- \copy nut_desc from '/home/andrea/Documents/calcount/fndds/NutDesc.txt' (delimiter '^');

SELECT main_food_desc, nut_desc, nutval FROM nut_vals INNER JOIN nut_desc using (nutcode) INNER JOIN main_food_desc USING (foodcode) WHERE nut_desc = '~Energy~' AND main_food_desc ~ 'Tomatoes' ORDER BY nutval;

-- SELECT * FROM main_food_desc WHERE main_food_desc ~ '~Chicken';

