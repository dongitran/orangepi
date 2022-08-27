var mqtt = require('mqtt');
var client = mqtt.connect('mqtt://172.16.120.128');

client.on('connect', function () {

    setTimeout(PublishTest, 2);
});


function PublishTest() {
    client.publish('logs', '{"d":"IOT1","i":"FA5C","a":[{"n":"val1","v":' + parseInt(Math.random()*100) + '},{"n":"val6","v":"adsf"}]}');


    setTimeout(PublishTest, 2);
}



