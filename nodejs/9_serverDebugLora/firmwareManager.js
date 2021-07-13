const [FirmwareDbInit, GetAllFirmwareDeviceDb, AddFirmwareDeviceDb, GetVersionJsonDb, UpdateVerionDb] = require('./database/firmware');

var firmwareOfDeviceGroup = [];

function FirmwareManagerInit(){
  FirmwareDbInit();

  let allFirmwareOfDevice = GetAllFirmwareDeviceDb();
  for(let i = 0; i < allFirmwareOfDevice.length; i++){
    firmwareOfDeviceGroup.push(allFirmwareOfDevice[i]);
  }

  console.log("firmwareOfDeviceGroup");
  console.log(firmwareOfDeviceGroup);
}
FirmwareManagerInit();

function GetAllFirmwareDevice(){
  return firmwareOfDeviceGroup;
}

function GetVersion(deviceName){
  for(let i = 0; i < firmwareOfDeviceGroup.length; i++){
    if(firmwareOfDeviceGroup[i].deviceName == deviceName){
      return firmwareOfDeviceGroup[i].version;
    }
  }
}

function AddFirmwareDevice(deviceName, version){
  AddFirmwareDeviceDb(deviceName, version);

  firmwareOfDeviceGroup.push({deviceName:deviceName, version:version})
}

function UpdateVersionFirmwareDevice(deviceName, version){
  UpdateVerionDb(deviceName, version);

  for(let i = 0; i < firmwareOfDeviceGroup.length; i++){
    if(firmwareOfDeviceGroup[i].deviceName == deviceName){
      firmwareOfDeviceGroup[i].version = version;
    }
  }
}

module.exports = [GetAllFirmwareDevice, GetVersion, AddFirmwareDevice, UpdateVersionFirmwareDevice];

