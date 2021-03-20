var formidable = require('formidable');
var express = require('express');
var router = express.Router();
let fs = require('fs');

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.post('/upload',function(req,res){
  const form = formidable({ multiples: true });
 
  form.parse(req, (err, fields, files) => {
    res.writeHead(200, { 'content-type': 'application/json' });
    res.end(JSON.stringify({ fields, files }, null, 2));
  });
});

module.exports = router;
