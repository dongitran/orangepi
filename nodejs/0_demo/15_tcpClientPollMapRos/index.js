

/*
And connect with a tcp client from the command line using netcat, the *nix 
utility for reading and writing across tcp/udp network connections.  I've only 
used it for debugging myself.
$ netcat 127.0.0.1 1337
You should see:
> Echo server
*/

/* Or use this example tcp client written in node.js.  (Originated with 
example code from 
http://www.hacksparrow.com/tcp-socket-programming-in-node-js.html.) */

var net = require('net');

const fs = require('fs');



var client = new net.Socket();
client.connect(9090, 'localhost', function() {
	console.log('Connected');
	client.write('{"op":"subscribe","id":"subscribe:/map:1","type":"nav_msgs/OccupancyGrid","topic":"/map","compression":"png","throttle_rate":0,"queue_length":0}');
});
var counter = 0;
client.on('data', function(data) {
	console.log('Received: ' + data);
  counter++;
  console.log(counter)
	//client.destroy(); // kill client after server's response
});

client.on('close', function() {
	console.log('Connection closed');
});