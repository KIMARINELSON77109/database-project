var app = angular.module("MealPlanner",['ngRoute','ui.bootstrap']);

angular.module('MealPlanner').factory('Service',['$http','$q',function($http,$q){
    return{
        getIngredients : function(){
            var deferred = $q.defer();
            $http.get('/ingredients')
            .success(function(data){
                deferred.resolve(data);
            })
            .error(function(err){
                deferred.reject(err);
            });
            return deferred.promise;
        },
        getMeasurements : function(){
            var deferred = $q.defer();
            $http.get('/measurements')
            .success(function(data){
                deferred.resolve(data);
            })
            .error(function(err){
                deferred.reject(err);
            });
            return deferred.promise;
        },
        
    }
}]);

angular.module('MealPlanner').controller('NewRecipeCtrl', ['$scope', 'Service', function ($scope, Service){
	Service.getMeasurements().then(function (measurements) {
		console.log(measurements);
		$scope.measurements = measurements.measurements;
	});

	Service.getIngredients().then(function (ingredients) {
		console.log(ingredients);
		$scope.ingredients = ingredients.ingredients;
	});

	$scope.ingredient= [];
    $scope.instructions = [];
    
	$scope.add_ingredient = function(){
	    var x = {
			quantity: 1,
			measurement: '',
			ingredient: ''

		};
		$scope.ingredient.push(
		   x
		);
		console.log("hi");
	};
    
    
	$scope.add_instruction = function(){
	    var x = {
			quantity: 1,
			measurement: '',
			ingredient: ''

		};
		$scope.instructions.push(
		   x
		);
		console.log("hi");
	};

}]);


