var net = require('net');

var client = new net.Socket();
var dataSend = null;
client.connect(19204, '192.168.192.5', function () {
    console.log('Tcp connected..');
    isTcpInitDone = true;
    //client.write('Hello, server! Love, Client.');
    let datSend = [0x5A, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x4C, 0x04, 0x4C, 0x00, 0x00, 0x00, 0x00];
    let hexVal = new Uint8Array(datSend);
    client.write(hexVal);

    //  a = '{ "vx" :  0.020000, "vy"  : 0.000000, "w"  : 0.000000 }'
});

client.on('data', function (data) {
    console.log('Received: ' + data);
    waitingReceived = false;
});


