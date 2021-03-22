var formidable = require('formidable');
var express = require('express');
var router = express.Router();
var mv = require('mv');
var fs = require('fs');

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
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
  fs.readdir('/home/idea/git/nodejs/5_controlSoundWithTimerAndConfigOverWeb/uploads', (err, files) => {
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


