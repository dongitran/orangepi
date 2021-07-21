var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
var mqtt = require('mqtt');


var indexRouter = require('./routes/index');
var usersRouter = require('./routes/users');
var WriteDb = require('./influxDb');
var WriteLogDebug = require('./logDebug');
const { Serializer } = require('v8');

var app = express();
var client = mqtt.connect('mqtt://172.16.120.128');

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', indexRouter);
app.use('/users', usersRouter);

// catch 404 and forward to error handler
app.use(function (req, res, next) {
  next(createError(404));
});

// error handler
app.use(function (err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});


client.on('connect', function () {
  WriteLogDebug('info', 'Mqtt - connect broker done!');

  client.subscribe('logs', function (err) {
    if (err) {
      WriteLogDebug('error', 'Subcribe Error: device/status');
    }
  });
});

/*{
  device: "gateway",
  id:"FA0D87",
  data:"[{"name":"val1","val":5},{"name":"val2","val":"adsf"}]"
}*/

client.on('message', function (topic, message) {
  message = message + "";
  if (topic == 'logs') {
    // Check enough field device, id and data
    if(IsJsonString(message)){
      receivedJson = JSON.parse(message);

      if((receivedJson.d == undefined)||(receivedJson.i == undefined)||(receivedJson.a == undefined)){
        WriteLogDebug('error', "Received data is incorrect format: " + message);
      }
      else{
        if(IsJson(receivedJson.a)){
          WriteDb(receivedJson.d, receivedJson.i, receivedJson.a);
        }
        else{
          WriteLogDebug('error', "Data content is not json: " + message);
        }
      }
    } else {
      WriteLogDebug('error', "Received data is not json: " + message);
    }
  }
});

function IsJsonString(str){
  if (/^[\],:{}\s]*$/.test(str.replace(/\\["\\\/bfnrtu]/g, '@').
    replace(/"[^"\\\n\r]*"|true|false|null|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?/g, ']').
    replace(/(?:^|:|,)(?:\s*\[)+/g, ''))) {
    
    return true;
  } else {
    return false;
  }
}

function IsJson(obj) {
  var t = typeof obj;
  return ['boolean', 'number', 'string', 'symbol', 'function'].indexOf(t) == -1;
}


module.exports = app;
