    $('document').ready(function(){
        $("#btn_ingred").on('click',function(){
            var newIngredient = '<div id="ingred" ng-repeat="ingr in ingredient" class="new_ingredient ng-scope"><input class="form-control"/><select class="form-control"><option ng-repeat="measurement in measurements">{{ measurement }}</option></select><select class="form-control"><option ng-repeat="instr in ingredients">{{ instr }}</option></select></br></div>';
            $('#ingred').append(newIngredient);
        });
    });
    $('document').ready(function(){
        $("#btn_instru").on('click',function(){
            var newInstruction = '<div class="col-recipe-instructions"><i class="ic icon-manual-madrab"></i><span class="count-of"></span><input type="text" class="form-control" placeholder="Instructions" name="recipe_instructions[]"><span class="remove-recipe-col"><i class="fa fa-times"></i></span></div>';
            $('#instru').append(newInstruction);
        });
    });