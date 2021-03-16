var express = require('express');
var router = express.Router();
var si = require('systeminformation');

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.post('/',function(req,res){
  cpuSpeedStr = '';
  si.cpu()
	.then(data => {
		console.log(data.speed); 
		cpuSpeedStr = data.speed;
		returnObj = {cpuSpeed: cpuSpeedStr};
		console.log(returnObj);
		res.send(returnObj);
	})
	.catch(error => console.log(error));
});

module.exports = router;
