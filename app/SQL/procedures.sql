Drop procedure if exists AddRecipe;
DELIMITER //
CREATE PROCEDURE AddRecipe(IN name VARCHAR(120),IN image VARCHAR(99),IN prep VARCHAR(12),IN cook VARCHAR(10),IN servings int(5))
    BEGIN 
        INSERT INTO recipe(recipe_name,recipe_picture,prep_time,cook_time,servings) VALUES(name,image,prep,cook,servings);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE GetRecipeById(IN id INT)
BEGIN 
    (
        SELECT * FROM recipe WHERE recipe.recipe_id=id
    );
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE recipeinstruction (IN recp_id INT )
BEGIN (
        SELECT instruction.step_num, instruction.direction
        FROM instruction JOIN recipe
        ON instruction.recipe_id = recipe.recipe_id
        ORDER BY instruction.step_num
      );
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE GetIngrMeasurFromRecipe(IN id INT)
BEGIN (
        SELECT needs.quantity, measurement.measurement_name, ingredients.ingredient_name FROM needs join measurement on needs.measurement_id=measurement.measurement_id JOIN ingredients ON
        needs.ingredient_id=ingredients.ingredient_id
      );
END //
DELIMITER ;