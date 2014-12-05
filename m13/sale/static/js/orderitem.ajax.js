
orderitemImport.factory('orderitemFactory', ['$http', function($http) {

    var orderitemFactory = {};

    orderitemFactory.importOrderItemsOfToday = function () {
        return $http.get('/sale/api/import_orderitems_of_today/');
    };

    orderitemFactory.getListOfOrders = function () {
        return $http.get('/sale/api/orders/');
    };

    return orderitemFactory;
}]);