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
config = '{"api":[{"id":0,"type":"post","server":"dweet.io","serverType":"https","port":443,"url":"/dweet/quietly/for/agvStatus","contentType":"json","contentLength":1,"content":"{\\\"status\\\":\\\"%s\\\"}"},{"id":1,"type":"get","server":"dweet.io","serverType":"https","port":443,"url":"/get/latest/dweet/for/agvControl","contentType":"json","content":"{\\\"this\\\":\\\"succeeded\\\",\\\"by\\\":\\\"getting\\\",\\\"the\\\":\\\"dweets\\\",\\\"with\\\":[{\\\"thing\\\":\\\"agvControl\\\",\\\"created\\\":\\\"#\\\",\\\"content\\\":{\\\"status\\\":@,\\\"control\\\":@}}]}"},{"id":2,"type":"get","server":"dweet.io","serverType":"https","port":443,"url":"/get/latest/dweet/for/agvMap","contentType":"json","contentLength":1,"content":"{\\\"this\\\":\\\"succeeded\\\",\\\"by\\\":\\\"getting\\\",\\\"the\\\":\\\"dweets\\\",\\\"with\\\":[{\\\"thing\\\":\\\"agvMap\\\",\\\"created\\\":\\\"#\\\",\\\"content\\\":{\\\"map\\\":\\\"&\\\"}}]}"}]}';
// Parse json config file
var configObj = JSON.parse(config);


// open connection to a serial port
client.connectRTUBuffered("/dev/ttyUSB0", { baudRate: 115200 });
client.setID(1);
client.setTimeout(1000);
var isSending = false;
var counter = 0;
var options;

function CheckApiRequest(){  // Read 
  counter++;
  client.readHoldingRegisters(0, 100)
    .then(value0_99=>{
      client.readHoldingRegisters(100, 47)
      .then(value100_146=>{
        if(value0_99.data[0] == 1){
          value = value0_99;
          for(let i = 0; i < 47; i++){
            value.data.push(value100_146.data[i]);
          }

          console.log('Api Request');
          let indexApi = value.data[1];
  
          // Build data to send
          let strSend = '';
          if(configObj.api[indexApi].type == 'post'){
            //let datSend = [value.data[2],value.data[3],value.data[4],value.data[5],value.data[6],value.data[7],value.data[8],value.data[9]];
            //strSend = vsprintf(configObj.api[indexApi].content, datSend);
            let datSend = [];

            // Check variable count receive from modbus with configObj
            // Adding..
            // Build data send
            let indexDataRegister = 19;
            for(let i = 0; i < value.data[2]; i++){
              if(value.data[3 + i] == 0){ // Error
                logger.log({
                  level: 'error',
                  message: 'Error 3 - Length variable = 0'
                });
              }
              if(value.data[3 + i] == 1){ // Number 16 bit
                datSend.push(value.data[indexDataRegister]);
                indexDataRegister++;
              }
              else{                       // String
                let strDatElement = '';
                for(let j = 0; j < value.data[3 + i]; j++){
                  strDatElement += String.fromCharCode(value.data[indexDataRegister]);
                  indexDataRegister++;
                }
                datSend.push(strDatElement);
              }
            }

            console.log(datSend);
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
                  client.writeRegisters(147, [1])
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
                console.log(response.body);
                console.log(response.statusCode);
  
                if(response.statusCode != 200){
                  // Upgrade only request api
                  //setTimeout(CheckApiRequest, 10);
  
                  // Repair data to send mcu
                  client.writeRegisters(10, [1])
                  .then(value=>{
                    setTimeout(CheckApiRequest, 10);
                    console.log(value);
                  })
                  .catch((e)=>{
                    console.log('Error 6');
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
                  let dataArr = [], lengthDataArr = 0, lengthRegisterArr = 0, dataStrTemp = '';
                  let lengthOfElementArr = [], lengthOfElement;
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
                          console.log('Error1: Length received not enought');
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
                      else if(dataFormat[indexFormat] == '@'){    // Is a number 16 bit
                        isSpecialCharacter = 2;
                        indexFormat++;
  
                        dataStrTemp = '';
                      }
                      else if(dataFormat[indexFormat] == '&'){    // Is a string
                        isSpecialCharacter = 3;
                        indexFormat++;

                        lengthOfElement = 0;
                      }
                      // Error data
                      else{
                        console.log(dataFormat[indexFormat]);
                        console.log(dataReceived[indexReceived]);
                        console.log('Error2: Data receive not determined');
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
                            console.log('Error3: Length received not enought');
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
                            console.log('Error4: Length received not enought');
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

                          dataArr.push(parseInt(dataStrTemp));
                          lengthRegisterArr++;

                          lengthOfElementArr.push(1);
                          lengthDataArr++;
                        }
                      }
                      else if(isSpecialCharacter == 3){
                        if(dataFormat[indexFormat] != dataReceived[indexReceived]){
                          //dataStrTemp += dataReceived[indexReceived];
                          
                          dataArr.push(dataReceived[indexReceived]);
                          lengthRegisterArr++;

                          lengthOfElement++;
  
                          if(indexReceived >= lengthDataReceived){
                            console.log('Error5: Length received not enought');
                            logger.log({
                              level: 'error',
                              message: 'Error 5 - Length received not enought'
                            });
                            errorCode = 2;
                            break;
                          }

                          indexReceived++;
                        }
                        else{
                          isSpecialCharacter = 0;

                          lengthOfElementArr.push(lengthOfElement);
                          lengthDataArr++;
                        }
                      }
                    }
                  }

                  if(errorCode == 0){   // Not error
  
                    // Repair data to send mcu
                    let datReturn = [1,0,0,0,0,0,0,0,0,errorCode];  // [DataReady,Dat0,Dat1,Dat2,Dat3,Dat4,Dat5,Dat6,Dat7,ErrorCode]
                    //for(let i = 0; i < dataArr.length; i++){
                    //  datReturn[i + 1] = parseInt(dataArr[i]);
                    //}

                    let lengthRegisterArrRemain = lengthRegisterArr;

                    // Send data received
                    let indexRegisterDataSend = 165;
                    let indexOnDataArr = 0;
                    //while(lengthRegisterArrRemain > 0){
                      
                    //}
                    


                    var datSend = [];
                    for(let i = 0; i < lengthOfElementArr.length; i++){
                      if(lengthOfElementArr[i] == 1){
                        datSend.push(dataArr[indexOnDataArr]);
                        indexOnDataArr++;
                      }
                      else{   //  lengthOfElementArr[i] > 0
                        for(let j = 0; j < lengthOfElementArr[i]; j++){
                          if((dataArr[indexOnDataArr] >= 0)&&(dataArr[indexOnDataArr] <= 9)){
                            datSend.push(parseInt(dataArr[indexOnDataArr + i]) + 48);
                          }
                          else{
                            datSend.push(dataArr[indexOnDataArr + i].charCodeAt(0));
                          }
                          indexOnDataArr++;
                        }
                      }
                    }
                    // Increase pointer of data arr
                    // indexOnDataArr += lengthSend_t;

                    const WriteBlock = async(index, datSend)=>{
                      try{
                        await client.writeRegisters(index, datSend);
                      }
                      catch(e){
                        console.log('Error 5');
                        console.log(e.message);
                      }
                    }
                    
                    (async () => {
                      try{
                        let indexOfDatSend = 0;
                        while(lengthRegisterArrRemain > 0){
                          let datSendBlock = [];
                          let lengthSend_t;
                          if(lengthRegisterArrRemain > 64){
                            lengthSend_t = 64;
                          }
                          else{
                            lengthSend_t = lengthRegisterArrRemain;
                          }
                          
                          for(let i = 0; i < lengthSend_t; i++){
                            datSendBlock.push(datSend[indexOfDatSend + i]);
                          }
                          function sleep(ms){
                            return new Promise(resolve => setTimeout(resolve, ms));
                          }
                          
                          await client.writeRegisters(indexRegisterDataSend, datSendBlock);
                          //await sleep(10);

                          indexOfDatSend += lengthSend_t;
                          indexRegisterDataSend += lengthSend_t;
                          lengthRegisterArrRemain -= lengthSend_t;
                        }

                        let datSend1 = [1, lengthDataArr];
                        
                        // Send flag finish, total count data, length of element data
                        for(let i = 0; i < lengthDataArr; i++){
                          datSend1.push(lengthOfElementArr[i]);
                        }
                        console.log('datSend1: ' + datSend1);
                        client.writeRegisters(147, datSend1)
                        .then(value=>{
                          setTimeout(CheckApiRequest, 10);
                        })
                        .catch((e)=>{
                          console.log('Error 4');
                          console.log(e.message);
                          setTimeout(CheckApiRequest, 10);
                        });
                      }
                      catch(e){
                        console.log('Error 3');
                        console.log(e.message);
                        setTimeout(CheckApiRequest, 10);
                        return;
                      }
                    })();
                    while(false){
                      
                      client.writeRegisters(indexRegisterDataSend, datSend)
                      .then(value=>{
                        // Increase position register
                        indexRegisterDataSend += lengthSend_t;

                        // Send flag finish, total count data, length of element data
                        let datSend = [1, lengthDataArr];
                        for(let i = 0; i < lengthDataArr; i++){
                          datSend.push(lengthOfElementArr[i]);
                        }

                        client.writeRegisters(147, datSend)
                        .then(value=>{
                          setTimeout(CheckApiRequest, 10);
                        })
                        .catch((e)=>{
                          console.log(e.message);
                          setTimeout(CheckApiRequest, 10);
                        });
                      })
                      .catch((e)=>{
                        console.log(e.message);
                        setTimeout(CheckApiRequest, 10);
                        return;
                      });
                    }
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
        logger.log({
          level: 'error',
          message: 'Error 2 - ' + e.message
        });
        setTimeout(CheckApiRequest, 1000);
      });
    })
    .catch((e)=>{
      logger.log({
        level: 'error',
        message: 'Error 1 - ' + e.message
      });
      setTimeout(CheckApiRequest, 1000);
    });
}
setTimeout(CheckApiRequest, 1000);

