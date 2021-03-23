var formidable = require('formidable');
var express = require('express');
var router = express.Router();
var mv = require('mv');
var fs = require('fs');
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

router.post('/control.html',function(req,res){
  const form = formidable({ multiples: false });

  form.parse(req, (err, fields, files) => {
    mv(files.file.path, "uploads/" + files.file.name, (err) => {
      if(err){
        console.log('Error - 5_controlSoundWithTimerAndConfigOverWeb: ' + err);
      }
    });

    res.writeHead(204);
    res.end();
  });
});

router.post('/control/init',function(req,res){
  //console.log(req);
  var arr = '';
  fs.readdir('./uploads', (err, files) => {
    //files.forEach(file => {
    //  arr = arr + file + ',';
    //  console.log(file);
    //});
    for(let i = 0; i < files.length; i++){
      arr = arr + files[i] + ',';
      console.log(files[i]);
    }
    console.log(arr);

    res.send(arr);
  })
});

router.post('/control/delete',function(req,res){
  console.log(req.body);
  let filePath = './uploads/' + req.body.name;
  fs.unlinkSync(filePath);
  res.send({test: '0'});
});

module.exports = router;


