Drop procedure if exists AddRecipe;
Drop procedure if exists GetRecipeById;
Drop procedure if exists recipeinstruction;
Drop procedure if exists GetIngrMeasurFromRecipe;
Drop procedure if exists GetWeekmealsByType;
Drop procedure if exists GetMealRecipe;
Drop procedure if exists GetRecipesLike;

DELIMITER //
CREATE PROCEDURE AddRecipe(IN name VARCHAR(120),IN image VARCHAR(99),IN prep VARCHAR(12),IN cook VARCHAR(10),IN servings int(5),IN diet VARCHAR(10))
    BEGIN 
        INSERT INTO recipe(recipe_name,recipe_picture,prep_time,cook_time,servings,diet_type) VALUES(name,image,prep,cook,servings,diet);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE GetRecipeById(IN res_id INT)
BEGIN (
        SELECT * FROM recipe WHERE recipe.recipe_id = res_id
      );
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE recipeinstruction (IN recp_id INT )
BEGIN (
        SELECT instruction.step_num, instruction.direction
        FROM instruction JOIN recipe
        ON instruction.recipe_id = recipe.recipe_id where recipe.recipe_id = recp_id
        ORDER BY instruction.step_num
      );
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE GetIngrMeasurFromRecipe(IN id INT)
BEGIN (
        SELECT needs.quantity, measurement.measurement_name, ingredients.ingredient_name FROM needs join measurement on needs.measurement_id=measurement.measurement_id JOIN ingredients ON
        needs.ingredient_id=ingredients.ingredient_id join recipe on needs.recipe_id=recipe.recipe_id where recipe.recipe_id = id
        
      );
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE GetWeekmealsByType(IN mltype VARCHAR(50))
BEGIN (SELECT meal.meal_name, meal.num_calorie, meal.meal_id FROM meal WHERE meal.meal_type = mltype
ORDER BY RAND()
LIMIT 7);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE GetMealRecipe(IN m_id int)
BEGIN (SELECT recipe.recipe_name, recipe.recipe_picture,recipe.prep_time,recipe.cook_time,recipe.servings,
recipe.diet_type FROM meal join makes on makes.meal_id=meal.meal_id join recipe on recipe.recipe_id=makes.recipe_id 
join needs on needs.recipe_id=recipe.recipe_id join measurement on needs.measurement_id=measurement.measurement_id JOIN ingredients ON 
needs.ingredient_id=ingredients.ingredient_id WHERE meal.meal_id = m_id
);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE GetRecipesLike(IN name VARCHAR(120))
BEGIN (
    SELECT * from recipe WHERE recipe.recipe_name LIKE name
);
END //
DELIMITER ;


-- DELIMITER //
-- CREATE PROCEDURE shoppingList(IN name VARCHAR(120))
-- BEGIN (
--     "SELECT ingredient.name, needs.quantity, measurement.measurement_name FROM  mealplan JOIN contains on contains.mealplan_id = mealplan.mealplan_id on meal.meal_id = contains.meal_id join makes on makes.meal_id=meal.meal_id join recipe on recipe.recipe_id=makes.recipe_id 
-- join needs on needs.recipe_id=recipe.recipe_id join measurement on needs.measurement_id=measurement.measurement_id JOIN ingredients ON 
-- needs.ingredient_id=ingredients.ingredient_id WHERE ingredient.ingredient_name NOT IN (SELECT * FROM kitchen)
-- );
-- END //
-- DELIMITER ;