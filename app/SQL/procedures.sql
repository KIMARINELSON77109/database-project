Drop procedure if exists AddRecipe;
DELIMITER //
CREATE PROCEDURE AddRecipe(IN name VARCHAR(120),IN image VARCHAR(99),IN prep VARCHAR(12),IN cook VARCHAR(10),IN servings int(5))
    BEGIN 
        INSERT INTO recipe(recipe_name,recipe_picture,prep_time,cook_time,servings) VALUES(name,image,prep,cook,servings);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE GetRecipe(In id int)
    BEGIN 
        select * from recipe where recipe_id=id;
END //
DELIMITER ;