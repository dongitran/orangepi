var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');

var indexRouter = require('./routes/index');
var usersRouter = require('./routes/users');
var mqtt = require('mqtt');
var client  = mqtt.connect('mqtt://172.16.120.128');
var [return1, return2] = require('./store');
const StatusDevice = require('./models/statusDevice');
const [AddDeviceAndCheckVersionAndTimeUpdate, GetAllDevice, UpdateVersionDevice, UpdateStatusDevice] = require('./deviceManager');
const [GetAllFirmwareDevice, GetVersion, AddFirmwareDevice, UpdateVersionFirmwareDevice] = require('./firmwareManager');

const { createLogger, format, transports } = require('winston');
const { combine, timestamp, label, printf } = format;
const logFormat = printf(({ level, message, timestamp }) => {
  return `${timestamp} - ${level}: ${message}`;
});
const loggerApi = createLogger({
  format: combine(
    label({ label: 'right meow!' }),
    timestamp(),
    logFormat
  ),
  transports: [
    new transports.Console(),
    new transports.File({ filename: 'logApi.log' })
  ]
});
const loggerMqtt = createLogger({
  format: combine(
    label({ label: 'right meow!' }),
    timestamp(),
    logFormat
  ),
  transports: [
    new transports.Console(),
    new transports.File({ filename: 'logMqtt.log' })
  ]
});

client.on('connect', function () {
  loggerMqtt.log({
    level: 'info',
    message: 'Mqtt - connect broker done!'
  });

  client.subscribe('device/status', function (err) {
    if (err) {
      loggerMqtt.log({
        level: 'error',
        message: 'Subcribe Error: device/status'
      });
    }
  });

  setTimeout(PublishVersionCurrent, 1000);
});

client.on('message', function (topic, message) {
  if(topic == 'device/status'){
    //loggerMqtt.log({
    //  level: 'info',
    //  message: 'Mqtt - New connect: ' + message
    //});
    //console.log('mqtt device/status: ' + message);
    let messageStr = '' + message;
    let objRec = messageStr.split('-');
    let device = new StatusDevice(objRec[0], objRec[1], objRec[2], objRec[3], Date.now());
    //console.log(Date.now());
    //console.log(device);
    if(AddDeviceAndCheckVersionAndTimeUpdate(device)){
      loggerMqtt.log({
        level: 'info',
        message: 'Mqtt - New device: ' + objRec[0]
      });
    }
  }
});

setInterval(UpdateStatusDevice, 3000);

async function PublishVersionCurrent(){
  let allDeviceFirmware = await GetAllFirmwareDevice();

  for(let i = 0; i < allDeviceFirmware.length; i++){
    client.publish('device/version_' + allDeviceFirmware[i].deviceName, '' + allDeviceFirmware[i].version);
  }
  

  setTimeout(PublishVersionCurrent, 5000);
}

var app = express();

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
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;


