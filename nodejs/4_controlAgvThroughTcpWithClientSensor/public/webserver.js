
var http = require('http').createServer(handler); //require http server, and cr>
var fs = require('fs'); //require filesystem module

http.listen(8091); //listen to port 8080

function handler (req, res) { //create server
  url = req.url;
  if((req.url == "/")||(req.url=="/index")){
    url = "/index.html";
  }
  fs.readFile(__dirname + url, function(err, data) { //read fi>
    if (err) {
      //res.writeHead(404, {'Content-Type': 'text/html'}); //display 404 on error
      console.log("File not detect");
      console.log(url);
      return res.end("404 Not Found");
    }
    //res.writeHead(200, {'Content-Type': 'text/html'}); //write HTML
    res.write(data); //write data from index.html
    return res.end();
  });
}
