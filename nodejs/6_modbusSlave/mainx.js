const serial = require('serialport')
const port = new serial('/dev/ttyUSB0',{baudRate:115200})
const ByteLength = new require('@serialport/parser-byte-length')

port.write('hello');
var counter = 0;

function waitAndProcessData(){
  counter++;
  console.log(counter);
  console.log(port.read());
  setTimeout(waitAndProcessData, 1);
  port.write('hello');
}

//setTimeout(waitAndProcessData, 10);

setTimeout(sendTest, 1);
function sendTest(){
  port.write('0123456789');
  setTimeout(sendTest, 5);
}

const parser = port.pipe(new ByteLength({length:1}))
var counterRec = 0;
var counterBefore = 0;
var timeCal  = Math.round(Date.now()/10000);
parser.on('data', (data)=>{
  //console.log(data);
  counterRec++;
  /*
  if(counterRec >= 1000){
    counterRec = 0;
    counter++;
    console.log(counter);
  }
   */


  let timeNow  = Math.round(Date.now()/10000);
  if(timeNow > timeCal){
    timeCal = timeNow;
    
    console.log((counterRec - counterBefore)/10);
    counterBefore = counterRec;
  }

})
