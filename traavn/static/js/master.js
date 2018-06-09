/////////////////////////////////////////////////////////////////////
// Using Angularjs(2.0.2)
// All rights reserved @traavn 2018
/////////////////////////////////////////////////////////////////////

(function()  {
 'use strict';

  var masterapp = angular.module('masterapp', ['ngRoute']);

  masterapp.config(['$routeProvider', function($routeProvider) {
    $routeProvider
      .when('/',  {
        templateUrl: 'static/ngtemplates/tripcard.html',
        controller: 'masterctrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  }]);

  masterapp.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  }]);

  masterapp.controller('masterctrl', ['$scope', '$http', function($scope, $http) {

    $scope.tripdata =  {};
    $scope.triplist = {};
    $http.get("http://192.168.1.10:8000/api/listtrips")
      .success(function(response) {
        $scope.triplist = response;
      })

        console.log("submitting");
      $scope.trippost = function() {
        console.log("submitting");
      }

  }]);

}());
