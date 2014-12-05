var Order = function(data) {
    this.marketplace_order_id = data.marketplace_order_id;
    this.purchase_time = data.purchase_time;
    this.marketplace_name = data.marketplace_name;
    this.customer_name = data.customer_name;
    this.invoice_number = data.invoice_number;
};

orderitemImport.factory('orders', function() {
    var self = this;
    var orders = [];
    var orderService = {};

    orderService.list = function() {
        return orders;
    };

    orderService.get_number_of_results = function() {
        return orders.length;
    };

    orderService.reset = function() {
        // console.log("RESET_CALLED");
        orders = [];
        ordersService = {};
    };

    orderService.add_multiple_orders = function(data) {
        //console.log("In add multiple orders: ");
        for(var idx in data) {
            order_data = data[idx];
            // console.log(order_data)
            orders.push(new Order(order_data));
        }
    };

    return orderService;
});