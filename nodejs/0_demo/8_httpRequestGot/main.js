const got = require('got');

(async () => {
    try {
        const response = await got('https://dweet.io/get/latest/dweet/for/agvControl');
        console.log(response.statusCode);
        console.log(response.body);
        //=> '<!doctype html> ...'
    } catch (error) {
        console.log(error.response.body);
        //=> 'Internal server error ...'
    }
})();
