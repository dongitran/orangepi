var DEVICE_NAME = "ClientCheckHttpServer"
var DEVICE_ID = "01"

const request = require('request');
var mqtt = require('mqtt');
var client = mqtt.connect('mqtt://172.16.120.128');


const { createLogger, format, transports } = require('winston');
const { combine, timestamp, label, printf } = format;
const logFormat = printf(({ level, message, timestamp }) => {
    return `${timestamp} - ${level}: ${message}`;
});
const logger = createLogger({
    format: combine(
        label({ label: 'right meow!' }),
        timestamp(),
        logFormat
    ),
    transports: [
        new transports.Console(),
        new transports.File({ filename: 'combined.log' })
    ]
});

client.on('connect', function () {
    logger.log({
        level: 'info',
        message: 'Mqtt - connect broker done!'
    });
});

var isFirstPollServer = true;
var counterCheck = 0, counterReceive = 0, isHigh = false;
var counterDisplay = 0;
var timeoutCount = 0, timeoutRepeat = 0;
var countPollOk = 0;
function PollServer(){
  request.get('http://172.16.120.173', {timeout:2000}, function(error, response, body){
    if(error != null){
      logger.log({
        level: 'error',
        message: 'Error: ' + error
      });

      timeoutCount++;

      client.publish('logs', '{"d":"' + DEVICE_NAME + '","i":"' + DEVICE_ID + '","a":[{"n":"Timeout","v":"' + timeoutCount + '"},{"n":"TimeoutIndex","v":1}]}');

      setTimeout(PollServer, 500);
    }
    else if(response.statusCode == 200){
      //console.log(response.body);
      let strArr = response.body.split(',');

      if(isFirstPollServer){
        isFirstPollServer = false;
        
        counterCheck = parseInt(strArr[1]);
        counterReceive = counterCheck;
        if(parseInt(strArr[0]) == 1){
          isHigh = true;
        }
        logger.log({
          level: 'info',
          message: 'First Poll - Counter: ' + counterCheck
        });
      }
      else{
        if(parseInt(strArr[0]) == 1){
          if(isHigh == false){
            isHigh = true;
            counterCheck++;
          }
        }
        else{
          isHigh = false;
        }

        countPollOk++;

        client.publish('logs', '{"d":"' + DEVICE_NAME + '","i":"' + DEVICE_ID + '","a":[{"n":"CountPollDone","v":' + countPollOk + '},{"n":"CounterCheck","v":"' + counterCheck + '"},{"n":"CounterReceived","v":"' + counterReceive + '"}]}');

        counterReceive = parseInt(strArr[1]);
        counterDisplay++;
        if(counterDisplay > 100){
          counterDisplay = 0;
          logger.log({
            level: 'info',
            message: 'Poll:' + response.body + '-Check:' + counterCheck + '-Receive:' + counterReceive + '-Timeout:' + timeoutCount
          });
        }

        timeoutRepeat = 0;
      }
      //console.log('Counter Check: ' + counterCheck);
      //console.log('Counter Receive: ' + counterReceive);

      setTimeout(PollServer, 500);
    }
    else{
      logger.log({
        level: 'error',
        message: 'ErrorCode: ' + response.statusCode + ' Body: ' + body
      });
    }
  });
}

PollServer();