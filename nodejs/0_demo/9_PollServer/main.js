var fs = require('fs');
var http = require('http');
var https = require('https');
const got = require('got');
// create an empty modbus client
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

function PollServer(){
  (async () => {
    try {
      const options={
        timeout: 400,
        retry:0
      }
      const response = await got('http://192.168.0.107:80', options);

      //logger.log({
      //  level: 'info',
      //  message: 'Received - statusCode: ' + response.statusCode + ' - body: ' + response.body
      //});

      if(response.statusCode != 200){
        // Upgrade only request api
        setTimeout(PollServer, 200);
        logger.log({
          level: 'warning',
          message: 'StatusCode: ' + response.statusCode
        });
        
      }
      else{
        setTimeout(PollServer, 200);
      }
      //=> '<!doctype html> ...'
    } catch (error) {
      //console.log(error);
      logger.log({
        level: 'error',
        message: error.message
      });

      setTimeout(PollServer, 300);
    }
  })();
}

PollServer();
