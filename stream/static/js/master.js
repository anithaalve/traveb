/////////////////////////////////////////////////////////////////////
// Using Angularjs(2.0.2)
// All rights reserved @traavn 2018
/////////////////////////////////////////////////////////////////////

(function()  {
 'use strict';

  var app = angular.module('masterapp', ['ngRoute']);

  app.config(['$routeProvider', function($routeProvider) {
    $routeProvider
      .when('/',  {
        templateUrl: 'static/ngtemplates/tripcard.html',
        controller: 'tripctrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  }]);

  app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  }]);

  app.controller('tripctrl', ['$scope', '$http', function($scope, $http) {

    // getting the list of the trips
    $scope.triplist = {};
    $scope.gettriplist = function() {
      $http.get('/api/listtrips')
      .then(function(response) {
        $scope.triplist = response.data;
      });
    }();

    // posting new trip
    $scope.tripdata = {}
    var timezoneoffset = moment().utcOffset() * 60;

    $scope.trippost = function() {
      $(".form-control").prop('disabled', true);
      $("#trippostbtn").prop('disabled', true);
      $scope.tripdata.fromlocation   = angular.element('#fromlocation').val();
      $scope.tripdata.tolocation     = angular.element('#tolocation').val();
      $scope.tripdata.leavingon      = moment($scope.triplist.leavingon).unix();
      $scope.tripdata.reachingon     = moment($scope.triplist.leavingon).unix();
      $scope.tripdata.timezoneoffset = timezoneoffset;
      var tripdata = {'tripdata': $scope.tripdata};
      $http({
        method: 'POST',
        url: '/api/trippost',
        data: tripdata,
        headers: {'Content-Type': 'application/json; charset=utf-8'}
      })
      .success(function(response) {
        $(".form-control").prop('disabled', false);
        $("#trippostbtn").prop('disabled', false);
        $('#trippostform').find('input:text, input:password, select, textarea').val('');
        $('#trippostform').find('input:radio, input:checkbox').prop('checked', false);
        $scope.gettriplist();
      })
    }
  }]);
}());
