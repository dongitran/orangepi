const StatusDevice = require('./models/statusDevice');

var deviceGroup = [];

function AddDevice(device){
  let deviceGroupSize = deviceGroup.length;

  for(let i = 0; i < deviceGroupSize; i++){
    if(deviceGroup[i].id == device.id){
      return false;
    }
  }

  deviceGroup.push(device);
  return true;
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

module.exports = [AddDevice, GetAllDevice, UpdateVersionDevice];
