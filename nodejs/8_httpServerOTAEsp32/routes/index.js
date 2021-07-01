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
    cb(null, req.body.deviceName + '_' + req.body.version)
  }
})

const upload = multer({ storage: storage });

const [AddDeviceAndCheckVersionAndTimeUpdate, GetAllDevice, UpdateVersionDevice, UpdateStatusDevice] = require('../deviceManager');
const [GetAllLogs, GetLast50Logs, AddLog] = require('../logManager');
const [DeviceActivityLogDbInit, GetAllLogDb, AddDeviceActivityLogToDb, GetMarkNoReadCount, IncreaseMarkNoReadCount, ResetMarkNoReadCount] = require('../database/deviceActivityLog');
const [GetAllFirmwareDevice, GetVersion, AddFirmwareDevice, UpdateVersionFirmwareDevice] = require('../firmwareManager');
/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

/* GET home page. */
router.post('/', function(req, res, next) {
  UpdateStatusDevice();
  let allDeviceObj = GetAllDevice();
  let allLogObj = GetLast50Logs();
  let markNoReadCount = parseInt(GetMarkNoReadCount());
  res.send(JSON.parse(JSON.stringify({AllDevices:allDeviceObj,AllLogs:allLogObj,MarkNoRead:markNoReadCount})));
  //res.end();
});

router.get('/resetMarkNoRead', function(req, res, next) {
  ResetMarkNoReadCount();
  res.send(JSON.parse(JSON.stringify({status:"ok"})));
  //res.end();
});



router.get('/getFirmware/:deviceName', async function(req, res, next) {
  //console.log("get");
  //console.log(req.mqttClient);

  console.log(req.params.deviceName);

    //console.log(req);
  //console.log(res);
  let versionStr = await GetVersion(req.params.deviceName);
  let firmwareDeviceName = req.params.deviceName + '_' + versionStr;
  //console.log('versionStr: ' + versionJson.version);
  //console.log(req.headers);
  //console.log('__dirname: ' + __dirname);
  let path = require('path');
  var filePath = path.join(__dirname, '../uploads/' + firmwareDeviceName);
  console.log('filePath: ' + filePath);
  var options = {
    headers: {
      "x-MD5":  md5.sync(filePath)
    }
  }
  res.sendFile(filePath, function (err) {
    if (err) {
        next(err)
      } else {
        //console.log('Sent:', filePath)
    }
  });

  

//  //console.log(req);
//  //console.log(res);
//  let versionObj = await GetVersionJson("esp32DevKit");
//  let versionJson = JSON.parse(JSON.stringify(versionObj));
//  //console.log('versionStr: ' + versionJson.version);
//  //console.log(req.headers);
//  //console.log('__dirname: ' + __dirname);
//  let path = require('path');
//  var filePath = path.join(__dirname, '../uploads/' + versionJson.version);
//  console.log('filePath: ' + filePath);
//  var options = {
//    headers: {
//      "x-MD5":  md5.sync(filePath)
//    }
//  }
//  res.sendFile(filePath, function (err) {
//    if (err) {
//        next(err)
//      } else {
//        //console.log('Sent:', filePath)
//    }
//  });
});

router.post('/getAllFirmware', async function(req, res, next) {
  //Error
  let allDeviceVersion = await GetAllFirmwareDevice();
  let result = JSON.parse(JSON.stringify(allDeviceVersion));
  res.send(result);
});

router.post("/uploadFirmware", upload.array("files"), uploadFiles);
function uploadFiles(req, res, next) {
  console.log(req.body.version);
  console.log(req.files);

  let deviceExist = GetVersion(req.body.deviceName);

  // If device not exist
  if(deviceExist == undefined){
    console.log('AddFirmwareDevice');
    AddFirmwareDevice(req.body.deviceName, req.body.version);
  }
  else{
    console.log('UpdateVersionFirmwareDevice');
    UpdateVersionFirmwareDevice(req.body.deviceName, req.body.version);
  }

  res.send(JSON.parse(JSON.stringify({status:"ok"})));
};

module.exports = router;


