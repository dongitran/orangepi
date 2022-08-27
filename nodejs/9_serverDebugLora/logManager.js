const [DeviceActivityLogDbInit, GetAllLogDb, AddDeviceActivityLogToDb, GetMarkNoReadCount, IncreaseMarkNoReadCount, ResetMarkNoReadCount] = require('./database/deviceActivityLog');

var logGroup = [];
var last50Log = [];
function GetAllLogOnDb(){
  DeviceActivityLogDbInit();

  let allLogs = GetAllLogDb();
  for(let i = 0; i < allLogs.length; i++){
    logGroup.push(allLogs[i]);
  }
  var last50Log_t = logGroup.slice(Math.max(logGroup.length - 50, 0));
  for(let i = 0; i < last50Log_t.length; i++){
    let log_min = {a:last50Log_t[i].id,b:last50Log_t[i].dateTime,c:last50Log_t[i].content};
    last50Log.push(log_min);
  }
}
GetAllLogOnDb();

function GetAllLogs(){
  return logGroup;
}

function GetLast50Logs(){
  return last50Log;
}

function AddLog(id, dateTime, content){
  let log = {id:id, dateTime:dateTime, content:content};
  let logMin = {a:id,b:dateTime,c:content};

  AddDeviceActivityLogToDb(log);
  logGroup.push(log);
  last50Log.push(logMin);
  last50Log.shift();

  IncreaseMarkNoReadCount();
  
  return true;
}

module.exports = [GetAllLogs, GetLast50Logs, AddLog];
