
var orderitemImport = angular.module('orderitemImport', []);
orderitemImport.config(function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});

orderitemImport.controller('AppController', ['$scope', 'orderitemFactory', 'orders',
                                             function($scope, orderitemFactory, orders) {
    var self = this;
    $scope.number_of_results = orders.get_number_of_results;
    $scope.list_of_orders = orders.list;

    self.init = function() {
        orders.reset();
        orderitemFactory.getListOfOrders()
        .success(function(data) {
            orders.add_multiple_orders(data);
        })
        .error(function() {
            console.log('GetListOfOrders: FAIL in init()');
        });
    };
    self.init();

    self.import_orderitems_of_today = function() {
        orderitemFactory.importOrderItemsOfToday()
        .success(function(data) {
            orderitemFactory.getListOfOrders()
            .success(function(data) {
                orders.reset();
                orders.add_multiple_orders(data);
            })
            .error(function(data) {
                console.log('GetListOfOrders: FAIL');
            });
        })
        .error(function() {
            console.log("Import OrderItems of today failed");
        });
    };
}]);