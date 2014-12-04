
orderitemImport.factory('orderitemFactory', ['$http', function($http) {

    var orderitemFactory = {};

    orderitemFactory.importOrderItemsOfToday = function () {
        return $http.get('/sale/api/import_orderitems_of_today/');
    };

    return orderitemFactory;
}]);