DELIMITER //
CREATE PROCEDURE AddRecipe(IN name VARCHAR(120),IN image VARCHAR(99),IN prep VARCHAR(12),IN cook VARCHAR(10),IN servings int(5))
    BEGIN 
        INSERT INTO recipe(recipe_name,recipe_image,prep_time,cook_time,servings) VALUES(name,image,prep,cook,servings);
END //
DELIMITER ;