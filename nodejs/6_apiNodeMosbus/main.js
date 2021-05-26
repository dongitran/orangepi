var fs = require('fs');
var http = require('http');
var https = require('https');
var vsprintf = require('sprintf-js').vsprintf;
const got = require('got');
// create an empty modbus client
var ModbusRTU = require("modbus-serial");
var client = new ModbusRTU();
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

// Config file
config = '{"api":[{"id":0,"type":"post","server":"dweet.io","serverType":"https","port":443,"url":"/dweet/quietly/for/agvStatus","contentType":"json","contentLength":1,"content":"{\\\"status\\\":%d}"},{"id":1,"type":"get","server":"dweet.io","serverType":"https","port":443,"url":"/get/latest/dweet/for/agvControl","contentType":"json","content":"{\\\"this\\\":\\\"succeeded\\\",\\\"by\\\":\\\"getting\\\",\\\"the\\\":\\\"dweets\\\",\\\"with\\\":[{\\\"thing\\\":\\\"agvControl\\\",\\\"created\\\":\\\"#\\\",\\\"content\\\":{\\\"status\\\":@,\\\"control\\\":@}}]}"}]}';
// Parse json config file
var configObj = JSON.parse(config);


// open connection to a serial port
client.connectRTUBuffered("/dev/ttyUSB0", { baudRate: 115200 });
client.setID(1);
client.setTimeout(100);
var isSending = false;
var counter = 0;
var options;

function CheckApiRequest(){  // Read 
  counter++;
  client.readHoldingRegisters(0, 10)
    .then(value=>{
      //setTimeout(CheckApiRequest, 10);
      // console.log('Receive....');
      // console.log(value.data);

      if(value.data[0] == 1){
        console.log('Api Request');
        let indexApi = value.data[1];

        // Build data to send
        let strSend = '';
        if(configObj.api[indexApi].type == 'post'){
          let datSend = [value.data[2],value.data[3],value.data[4],value.data[5],value.data[6],value.data[7],value.data[8],value.data[9]];
          strSend = vsprintf(configObj.api[indexApi].content, datSend);
        }

        let link = "";
        if(configObj.api[indexApi].serverType == 'https'){
          link = 'https://';
        }
        else{
          link = 'http://';
        }
        link = link + configObj.api[indexApi].server;
        link = link + ':' + configObj.api[indexApi].port;
        link = link + configObj.api[indexApi].url;
        
        if(configObj.api[indexApi].type == 'post'){
          (async () => {
            try{
              const {body, statusCode} = await got.post(link, {
                json: JSON.parse(strSend),
                responseType: 'json'
              });
            
              console.log(statusCode);
  
              if(body != 200){
                // Upgrade only request api
                //setTimeout(CheckApiRequest, 10);
  
                // Repair data to send mcu
                client.writeRegisters(10, [1])
                .then(value=>{
                  setTimeout(CheckApiRequest, 10);
                  console.log(value);
                })
                .catch((e)=>{
                  console.log(e.message);
                  setTimeout(CheckApiRequest, 10);
                });
              }
            }
            catch(e){
              console.log(e);
              logger.log({
                level: 'error',
                message: e
              });

              setTimeout(CheckApiRequest, 10);
            }
          })();
        }
        else{   // configObj.api[indexApi].type == 'get'
          (async () => {
            try {
              const response = await got(link);

              if(response.statusCode != 200){
                // Upgrade only request api
                setTimeout(CheckApiRequest, 10);

                // Repair data to send mcu
                client.writeRegisters(10, [1])
                .then(value=>{
                  setTimeout(CheckApiRequest, 10);
                  console.log(value);
                })
                .catch((e)=>{
                  console.log(e.message);
                  setTimeout(CheckApiRequest, 10);
                });
              }
              else{
                // Check format data receive correct
                let dataReceived = response.body;
                console.log('dataReceived: ' + dataReceived);
                
                let dataFormat = configObj.api[indexApi].content;
                console.log('dataFormat: ' + dataFormat);
                // Transfer data received to format data
                let indexFormat = 0, lengthDataFormat = dataFormat.length;
                let indexReceived = 0, lengthDataReceived = dataReceived.length;
                let isSpecialCharacter = 0;
                let dataArr = [], dataStrTemp = '';
                let errorCode = 0;
                while(indexFormat < lengthDataFormat){
                  if(isSpecialCharacter == 0){
                    if(dataFormat[indexFormat] == dataReceived[indexReceived]){
                      indexFormat++;
                      indexReceived++;

                      if((indexReceived == lengthDataReceived)&&(indexFormat == lengthDataFormat)){
                        errorCode = 0;
                        break;
                      }
                      else if(indexReceived >= lengthDataReceived){
                        console.log('Error1: Check data receive invalid');
                        errorCode = 2;
                        logger.log({
                          level: 'error',
                          message: 'Error 1 - Length received not enought'
                        });
                        break;
                      }
                    }
                    else if(dataFormat[indexFormat] == '#'){
                      isSpecialCharacter = 1;
                      indexFormat++;
                    }
                    else if(dataFormat[indexFormat] == '@'){
                      isSpecialCharacter = 2;
                      indexFormat++;

                      dataStrTemp = '';
                    }
                    // Error data
                    else{
                      console.log(dataFormat[indexFormat]);
                      console.log(dataReceived[indexReceived]);
                      console.log('Error2: Check data receive invalid');
                      errorCode = 2;
                      logger.log({
                        level: 'error',
                        message: 'Error 2 - Data receive not determined'
                      });
                      break;
                    }
                  }
                  else{
                    if(isSpecialCharacter == 1){
                      if(dataFormat[indexFormat] != dataReceived[indexReceived]){
                        indexReceived++;
                        if(indexReceived >= lengthDataReceived){
                          console.log('Error3: Check data receive invalid');
                          errorCode = 2;
                          logger.log({
                            level: 'error',
                            message: 'Error 3 - Length received not enought'
                          });
                          break;
                        }
                      }
                      else{
                        isSpecialCharacter = 0;
                      }
                    }
                    else if(isSpecialCharacter == 2){
                      if(dataFormat[indexFormat] != dataReceived[indexReceived]){
                        dataStrTemp += dataReceived[indexReceived];
                        indexReceived++;

                        if(indexReceived >= lengthDataReceived){
                          console.log('Error4: Check data receive invalid');
                          logger.log({
                            level: 'error',
                            message: 'Error 4 - Length received not enought'
                          });
                          errorCode = 2;
                          break;
                        }
                      }
                      else{
                        isSpecialCharacter = 0;
                        dataArr.push(dataStrTemp);
                      }
                    }
                  }
                }

                if(errorCode == 0){   // Not error
                  console.log(dataArr);

                  // Repair data to send mcu
                  let datReturn = [1,0,0,0,0,0,0,0,0,errorCode];  // [DataReady,Dat0,Dat1,Dat2,Dat3,Dat4,Dat5,Dat6,Dat7,ErrorCode]
                  for(let i = 0; i < dataArr.length; i++){
                    datReturn[i + 1] = parseInt(dataArr[i]);
                  }
                  console.log('dataReturn: ' + datReturn);
                  client.writeRegisters(10, datReturn)
                  .then(value=>{
                    setTimeout(CheckApiRequest, 10);
                    console.log(value);
                  })
                  .catch((e)=>{
                    console.log(e.message);
                    setTimeout(CheckApiRequest, 10);
                  });
                }
                else if(errorCode == 2){
                  // Repair data to send mcu
                  client.writeRegisters(19, [errorCode])
                    .then(value=>{
                      setTimeout(CheckApiRequest, 10);
                      console.log(value);
                    })
                    .catch((e)=>{
                      console.log(e.message);
                      setTimeout(CheckApiRequest, 10);
                    });
                }                      
              }
              //=> '<!doctype html> ...'
            } catch (error) {
              console.log(error);
              logger.log({
                level: 'error',
                message: error
              });

              setTimeout(CheckApiRequest, 10);
            }
          })();
        }
        /*
          if(configObj.api[indexApi].type == 'post'){
            options = {
              hostname: configObj.api[indexApi].server,
              port: configObj.api[indexApi].port,
              path: configObj.api[indexApi].url,
              header:{
                'Content-Type': 'application/json',
                'Content-Length': strSend.length
              },
              method:'POST',
              timeout: 3000,
            };
          }
          else{
            options = {
              hostname: configObj.api[indexApi].server,
              port: configObj.api[indexApi].port,
              path: configObj.api[indexApi].url,
              method:'GET',
              timeout: 3000,
            };
          }
          let req, http_https;
          if(configObj.api[indexApi].serverType == 'http'){
            http_https = http;
          }
          else{
            http_https = https;
          }
          try{
            req = http_https.request(options, res=>{
              console.log('status: ' + res.statusCode);
              if(configObj.api[indexApi].type == 'post'){
                console.log('Process after get');
                client.writeRegisters(10, [1])
                      .then(value=>{
                        setTimeout(CheckApiRequest, 10);
                        console.log(value);
                      })
                      .catch((e)=>{
                        console.log(e.message);
                        setTimeout(CheckApiRequest, 10);
                      });
              }
              res.on('data', d=>{
                console.log('Data ' + d);
    
                if(configObj.api[indexApi].type == 'get'){
                  
                }
              })
            });
    
            req.on('error', error=>{
              console.log(error);
            });
            if(configObj.api[indexApi].type == 'post')
              req.write(strSend);
            req.end();
          }
          catch(e){
            console.log('Error6: Request https crash');
            logger.log({
              level: 'error',
              message: 'Error 6 - Request https crash'
            });
            logger.log({
              level: 'error',
              message: e.message
            });
            setTimeout(CheckApiRequest, 10);
          }
        */
      }
      else{
        setTimeout(CheckApiRequest, 10);
      }
    })
    .catch((e)=>{
      console.log('readHoldingRegisters error');
      console.log(e.message);
      setTimeout(CheckApiRequest, 10);
    });
}
setTimeout(CheckApiRequest, 10);

