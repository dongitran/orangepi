var express = require('express');
var router = express.Router();
var si = require('systeminformation');

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.post('/',function(req,res){
  si.cpu()
    .then(cpuData => {
      //console.log(cpuData); 
      cpuSpeed = cpuData.speed;
      
      si.cpuCurrentSpeed()
        .then(currentSpeedData=>{
          //console.log(currentSpeedData);
          currentSpeed = currentSpeedData.avg;

          si.mem()
            .then(memData=>{
              //console.log(memData);
              memTotal = memData.total;
              memFree = memData.free;

              si.cpuTemperature()
                .then(temperatureData=>{
                  //console.log(temperatureData);
                  returnObj = {
                    cpuSpeed: cpuSpeed, 
                    currentSpeed: currentSpeed,
                    memTotal: memTotal,
                    memFree: memFree,
                    temperature: temperatureData.main
                  };
                  //console.log(returnObj);
                  res.send(returnObj);
                })
                .catch(error => console.log(error));
            })
            .catch(error => console.log(error));
        })
        .catch(error => console.log(error));
    })
	.catch(error => console.log(error));
});

module.exports = router;
