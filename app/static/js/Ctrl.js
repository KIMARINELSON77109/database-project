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
        getRecipes : function(meal_id){
            var deferred = $q.defer();
            $http.get('/meals/' + meal_id)
            .success(function(data){
                deferred.resolve(data);
            })
            .error(function(err){
                deferred.reject(err);
            });
            return deferred.promise;
        },
        getmealplanmeals : function(mtype){
            var deferred = $q.defer();
            $http.get('/getmealplanmeals/' + mtype)
            .success(function(data){
                console.log("rad");
                console.log(data);
                deferred.resolve(data);
            })
            .error(function(err){
                deferred.reject(err);
            });
            return deferred.promise;
        }
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

}]);

angular.module('MealPlanner').controller('GenMealPlanCtrl', ['$scope', 'Service', function ($scope, Service){
	
	$scope.dostuff = function(){
	    Service.getmealplanmeals('Breakfast').then(function (meals) {
		$scope.breakfasts = meals.meals;
    	});
    
        Service.getmealplanmeals('Lunch').then(function (meals) {
    		$scope.lunches = meals.meals;
    	});
    	Service.getmealplanmeals('Dinner').then(function (meals) {
    		$scope.dinners = meals.meals;
    	});
	};
	    
		
}]);

