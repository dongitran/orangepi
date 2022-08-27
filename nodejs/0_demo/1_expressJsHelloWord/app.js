const express = require('express')
const app = express()
const port = 2000

app.get('/', (req, res) => {
  let status = 0;
  if(isHigh == true){
    status = 1;
  }
  res.send('' + status + '-' + counter);
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})
var counter = 0, isHigh = false;
function IncreaseCounter(){
  if(isHigh == false){
    isHigh = true;
    counter++;
  }
  else{
    isHigh = false;
  }

  setTimeout(IncreaseCounter, 2000);
}

IncreaseCounter();
