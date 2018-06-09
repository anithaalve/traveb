/////////////////////////////////////////////////////////////////////
// Using Angularjs(2.0.2)
// All rights reserved @traavn 2018
/////////////////////////////////////////////////////////////////////

(function()  {
 'use strict';
  masterapp.module('masterapp.masterctrl', ['$scope', '$http', function($scope, $http) {

    $scope.name = 'Main';
    $scope.triplist = {};
    $http.get("http://192.168.1.10:8000/api/listtrips")
      .success(function(response) {
        $scope.triplist = response;
      });

  }]);

});

