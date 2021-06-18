var express = require('express');
var router = express.Router();
const multer = require("multer");
var storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, 'uploads')
  },
  filename: function (req, file, cb) {
    cb(null, req.body.version)
  }
})

const upload = multer({ storage: storage });

const [AddDevice, GetAllDevice, UpdateVersionDevice] = require('../deviceManager');

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

/* GET home page. */
router.post('/', function(req, res, next) {
  res.send(JSON.parse(JSON.stringify(GetAllDevice())));
  //res.end();
});


router.get('/getFirmware', function(req, res, next) {
  //console.log("get");
  //console.log(req.mqttClient);

  //console.log(req);
  //console.log(res);
  
});

router.post("/uploadFirmware", upload.array("files"), uploadFiles);
function uploadFiles(req, res, next) {
  console.log(req.body.version);
  console.log(req.files);
};

module.exports = router;

