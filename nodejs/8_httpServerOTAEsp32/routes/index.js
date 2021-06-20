var express = require('express');
var router = express.Router();
const multer = require("multer");
var fs = require("fs");
var md5 = require("md5-file");
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
const [GetVersion, GetVersionJson, UpdateVerion] = require('../sql');

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
  let versionStr = GetVersion("esp32DevKit");

  console.log(req.headers);
  var filePath = path.join(__dirname, '../uploads/' + versionStr);
  var options = {
    headers: {
      "x-MD5":  md5.sync(filePath)
    }
  }
  res.sendFile(file, function (err) {
    if (err) {
        next(err)
      } else {
        console.log('Sent:', file)
    }
  });
});

router.post('/getVersion', async function(req, res, next) {
  //Error
  let a = await GetVersionJson("esp32DevKit");
  console.log('a: ' + a);
  let result = JSON.parse(JSON.stringify(a));
  console.log('Return /getVersion');
  res.send(result);
});

router.post("/uploadFirmware", upload.array("files"), uploadFiles);
function uploadFiles(req, res, next) {
  console.log(req.body.version);
  console.log(req.files);

  UpdateVerion("esp32DevKit", req.body.version);
};

module.exports = router;

