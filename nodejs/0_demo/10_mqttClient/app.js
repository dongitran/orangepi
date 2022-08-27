var mqtt = require('mqtt')
var client  = mqtt.connect('mqtt://192.168.0.125')

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
  //client.subscribe('test/message', function (err) {
  client.subscribe('/clientPub', function (err) {
    if (!err) {
      
    }
  })

  client.subscribe('test/message', function (err) {
    if (!err) {
      
    }
  })
})
 
var counterCheckEsp32 = 0, isFirstGetEsp32 = true, counterInitEsp32 = 0, logFilterEsp32 = 0, isEsp32Error = false, errorFilterEsp32 = 0;
var counterCheckPi = 0, isFirstGetPi = true, counterInitPi = 0, logFilterPi = 0, isPiError = false, errorFilterPi = 0;
client.on('message', function (topic, message) {
  let counterReceive = parseInt(message.toString());

  if(topic == '/clientPub'){
    counterCheckEsp32++;

    if(isFirstGetEsp32){
      isFirstGetEsp32 = false;
      counterCheckEsp32 = counterReceive;
      counterInitEsp32 = counterReceive;
      console.log('Esp32 Init! ' + counterReceive);
    }
    else if(counterReceive == counterCheckEsp32){
      logFilterEsp32++;
      if(logFilterEsp32 > 100){
        logFilterEsp32 = 0;

        logger.log({
          level: 'info',
          message: 'Esp32 Ok! ' + (counterReceive - counterInitEsp32)
        });
      }
      
      isEsp32Error = false;
    }
    else{
      if(isEsp32Error == false){
        errorFilterEsp32 = 0;
        isEsp32Error = true;

        logger.log({
          level: 'error',
          message: 'Esp32 Error! ' + counterReceive + '-' + counterCheckEsp32
        });
      }
      else{
        errorFilterEsp32++;

        if(errorFilterEsp32 > 20){
          errorFilterEsp32 = 0;

          logger.log({
            level: 'error',
            message: 'Esp32 Error! ' + counterReceive + '-' + counterCheckEsp32
          });
        }
      }
    }
  }
  else if(topic == 'test/message'){
    counterCheckPi++;

    if(isFirstGetPi){
      isFirstGetPi = false;
      counterCheckPi = counterReceive;
      counterInitPi = counterReceive;
      console.log('Pi Init! ' + counterReceive);
    }
    else if(counterReceive == counterCheckPi){
      logFilterPi++;
      if(logFilterPi > 500){
        logFilterPi = 0;
        logger.log({
          level: 'info',
          message: 'Pi Ok! ' + (counterReceive - counterInitPi)
        });
      } 

      isPiError = false;
    }
    else{
      if(isPiError == false){
        errorFilterPi = 0;
        isPiError = true;

        logger.log({
          level: 'error',
          message: 'Pi Error! ' + counterReceive + '-' + counterCheckPi
        });
      }
      else{
        errorFilterPi++;

        if(errorFilterPi > 100){
          errorFilterPi = 0;

          logger.log({
            level: 'error',
            message: 'Pi Error! ' + counterReceive + '-' + counterCheckPi
          });
        }
      }
    }
  }
  
})

var counter = 0;
function Send(){
  counter++;
  client.publish('test/message', '' + counter);

  setTimeout(Send, 100);
}

//Send();
