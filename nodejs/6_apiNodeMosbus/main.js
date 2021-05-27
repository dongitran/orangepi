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
//config = '{"api":[{"id":0,"type":"post","server":"dweet.io","serverType":"https","port":443,"url":"/dweet/quietly/for/agvStatus","contentType":"json","contentLength":1,"content":"{\\\"status\\\":%d}"},{"id":1,"type":"get","server":"dweet.io","serverType":"https","port":443,"url":"/get/latest/dweet/for/agvControl","contentType":"json","content":"{\\\"this\\\":\\\"succeeded\\\",\\\"by\\\":\\\"getting\\\",\\\"the\\\":\\\"dweets\\\",\\\"with\\\":[{\\\"thing\\\":\\\"agvControl\\\",\\\"created\\\":\\\"#\\\",\\\"content\\\":{\\\"status\\\":@,\\\"control\\\":@}}]}"}]}';
var config = '';
// Parse json config file
var configObj;


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
  
              if(body == 200){
                
              }
              else{
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
                let dataFormat = configObj.api[indexApi].content;
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

// Step:  0 - Send start sync -> Wait start sync ok
//        1 - Send request length config data -> Waiting length config data
//        2 - Send request data -> Waiting data reponse
//        3 - Send finish sync -> Waiting finish sync ok
//
var syncStep = 0, lengthConfigStr, lengthRemainGetConfigStr, blockRequestGetConfigStr;
var errSync = 0;
function SyncConfigData(){
  switch(syncStep){
    case 0:{    //  Send start sync -> Wait start sync ok
      client.writeRegisters(10, [11])
      .then(value=>{
        client.readHoldingRegisters(0, 1)
        .then(valueRead=>{
          if(valueRead.data[0] == 11){
            syncStep++;

            setTimeout(SyncConfigData, 10);
          }
          else{
            logger.log({
              level: 'error',
              message: "Mcu not accept start sync"
            });

            setTimeout(SyncConfigData, 10);
          }
        })
        .catch((e)=>{
          logger.log({
            level: 'error',
            message: 'Error 11.0 - ' + e.message
          });

          setTimeout(SyncConfigData, 10);
        });
      })
      .catch((e)=>{
        logger.log({
          level: 'error',
          message: 'Error 11.1 - ' + e.message
        });
        
        setTimeout(SyncConfigData, 10);
      });
      break;
    }
    case 1:{    //  Send request length config data -> Waiting length config data
      client.writeRegisters(10, [12])
      .then(value=>{
        client.readHoldingRegisters(0, 2)
        .then(valueRead=>{
          if(valueRead.data[0] == 12){
            lengthConfigStr = valueRead.data[1];
            lengthRemainGetConfigStr = lengthConfigStr;
            blockRequestGetConfigStr = 0;
            syncStep++;

            setTimeout(SyncConfigData, 10);
          }
          else{
            logger.log({
              level: 'error',
              message: "Mcu not accept get length config data"
            });

            setTimeout(SyncConfigData, 10);
          }
        })
        .catch((e)=>{
          logger.log({
            level: 'error',
            message: 'Error 12.0 - ' + e.message
          });

          setTimeout(SyncConfigData, 10);
        });
      })
      .catch((e)=>{
        logger.log({
          level: 'error',
          message: 'Error 12.1 - ' + e.message
        });

        setTimeout(SyncConfigData, 10);
      });
      break;
    }
    case 2:{    //  Send request data -> Waiting data reponse
      let lengthCharacterRequest;
      if(lengthRemainGetConfigStr >= 16){
        lengthCharacterRequest = 16;
      }
      else{
        lengthCharacterRequest = lengthRemainGetConfigStr;
      }
      lengthRemainGetConfigStr -= lengthCharacterRequest;
      blockRequestGetConfigStr++;

      client.writeRegisters(10, [13, blockRequestGetConfigStr])
      .then(value=>{
        client.readHoldingRegisters(0, 10)
        .then(valueRead=>{
          if((valueRead.data[0] == 13)&&(valueRead.data[1] == blockRequestGetConfigStr)){
            lengthConfigStr = valueRead.data[1];
            
            // Get config data
            let counterRegister = 0;
            counterRegister = Math.floor(lengthCharacterRequest/2);
            if(lengthCharacterRequest%2 > 0){
              counterRegister++;
            }

            for(let i = 0; i < counterRegister; i++){
              config += String.fromCharCode(valueRead.data[2 + i]%256);
              config += String.fromCharCode(Math.floor(valueRead.data[2 + i]/256));
            }

            // Check data is remain?
            if(lengthRemainGetConfigStr == 0){
              configObj = JSON.parse(config);
              console.log(configObj);
              syncStep++;
            }
            setTimeout(SyncConfigData, 10);
          }
          else{
            logger.log({
              level: 'error',
              message: "Mcu not accept get config data"
            });
            //errSync = 1;
            blockRequestGetConfigStr--;
            lengthRemainGetConfigStr += lengthCharacterRequest;

            setTimeout(SyncConfigData, 10);
          }
        })
        .catch((e)=>{
          logger.log({
            level: 'error',
            message: "Error 1: " + e
          });
          blockRequestGetConfigStr--;
          lengthRemainGetConfigStr += lengthCharacterRequest;

          setTimeout(SyncConfigData, 10);
        });
      })
      .catch((e)=>{
        logger.log({
          level: 'error',
          message: "Error 2: " + e
        });
        blockRequestGetConfigStr--;
        lengthRemainGetConfigStr += lengthCharacterRequest;

        setTimeout(SyncConfigData, 10);
      });
      break;
    }
    case 3:{    //  Send finish sync -> Waiting finish sync ok
      client.writeRegisters(10, [14])
      .then(value=>{
        syncStep++;
        setTimeout(SyncConfigData, 10);
      })
      .catch((e)=>{
        logger.log({
          level: 'error',
          message: "Error 4: " + e
        });
        setTimeout(SyncConfigData, 10);
      });
      break;
    }
    case 4:{    
      setTimeout(CheckApiRequest, 10);
      errSync = 1;
      break;
    }
  }
}

//setTimeout(CheckApiRequest, 10);
setTimeout(SyncConfigData, 1000);

