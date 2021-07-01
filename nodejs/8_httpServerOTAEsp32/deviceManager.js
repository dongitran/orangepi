const StatusDevice = require('./models/statusDevice');
const [DeviceDbInit, GetAllDeviceDb, AddDeviceToDb, UpdateStatusToDb, UpdateVersionToDb, UpdateTimeUpdateToDb] = require('./database/device');
const [GetAllLogs, GetLast50Logs, AddLog] = require('./logManager');

var deviceGroup = [];

function GetDeviceFromDb(){
  DeviceDbInit();

  let allDevices = GetAllDeviceDb();
  for(let i = 0; i < allDevices.length; i++){
    deviceGroup.push(allDevices[i]);
  }
  console.log('GetDeviceFromDb');
  console.log(allDevices);
}
GetDeviceFromDb();

function AddDeviceAndCheckVersionAndTimeUpdate(device){
  let deviceGroupSize = deviceGroup.length;

  for(let i = 0; i < deviceGroupSize; i++){
    //console.log('deviceGroup[i].id: ' + deviceGroup[i].id + '- device.id: ' + device.id + '- deviceGroup[i].type: ' + deviceGroup[i].type + '- device.type: ' + device.type);
    if((deviceGroup[i].id == device.id)&&(deviceGroup[i].type == device.type)){
      
      //deviceGroup[i].timeUpdate = device.timeUpdate;
      if(deviceGroup[i].version != device.version){
        deviceGroup[i].version = device.version;

        UpdateVersionToDb(deviceGroup[i].id, device.version);
        AddLog(deviceGroup[i].id, Date.now(), "update version " + device.version);
      }

      //console.log('deviceGroup[i].timeUpdate: ' + deviceGroup[i].timeUpdate + '-device.timeUpdate: ' + device.timeUpdate);
      if(deviceGroup[i].timeUpdate != device.timeUpdate){
        deviceGroup[i].timeUpdate = device.timeUpdate;

        UpdateTimeUpdateToDb(deviceGroup[i].id, device.timeUpdate);

        //console.log('UpdateTimeUpdateToDb: ' + device.id);
      }

      return false;
    }
  }
  AddDeviceToDb(device.id, device.type, device.version, device.status, device.timeUpdate);
  deviceGroup.push(device);
  return true;
}

function UpdateStatusDevice(){
  let deviceGroupSize = deviceGroup.length;
  let timeNow = Date.now();
  for(let i = 0; i < deviceGroupSize; i++){
    if((timeNow - deviceGroup[i].timeUpdate) >= 30000){
      if(deviceGroup[i].status != "Offline"){
        deviceGroup[i].status = "Offline";
        AddLog(deviceGroup[i].id, Date.now(), "disconnect!");
        UpdateStatusToDb(deviceGroup[i].id, "Offline");
      }
    }
    else{
      if(deviceGroup[i].status != "Running.."){
        deviceGroup[i].status = "Running..";
        AddLog(deviceGroup[i].id, Date.now(), "connect..");
        UpdateStatusToDb(deviceGroup[i].id, "Running..");
      }
    }
  }
}
function GetAllDevice(){

  return deviceGroup;
}

function UpdateVersionDevice(device){
  for(let i = 0; i < deviceGroupSize; i++){
    if(deviceGroup[i].id == device.id){
      deviceGroup[i].version = device.version;
    }
  }
}

module.exports = [AddDeviceAndCheckVersionAndTimeUpdate, GetAllDevice, UpdateVersionDevice, UpdateStatusDevice];

