
var orderitemImport = angular.module('orderitemImport', []);
orderitemImport.config(function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});

orderitemImport.controller('AppController', ['$scope', 'orderitemFactory',
                                             function($scope, orderitemFactory) {
    var self = this;

    self.import_orderitems_of_today = function() {
        console.log("CLICK");
        orderitemFactory.importOrderItemsOfToday()
        .success(function(data) {
            console.log(data.message);
        })
        .error(function(data) {
            console.log(data.message);
        });
    };
}]);