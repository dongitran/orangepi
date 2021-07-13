const Database = require('better-sqlite3');
const db = new Database('./db/firmware.db');//, { verbose: console.log });

function FirmwareDbInit(){
  db.exec('CREATE TABLE IF NOT EXISTS esp32 (deviceName TEXT, version TEXT)');
  //const stmt = db.prepare('INSERT INTO esp32(deviceName, version) VALUES(?, ?)');
  //stmt.run("esp32DevKit", "1.8.6");
}

function GetAllFirmwareDevice(){
  const stmt = db.prepare('SELECT * FROM esp32');

  result = stmt.all();
  return result;
}

function AddFirmwareDevice(deviceName, version){
  const stmt = db.prepare('INSERT INTO esp32(deviceName, version) VALUES(?, ?)');

  stmt.run(deviceName, version);
}

function GetVersionJson(deviceName){
  const stmt = db.prepare('SELECT version FROM esp32 WHERE deviceName=?');
  result = stmt.all(deviceName);
  // BUG 
  return result[0];
}

function UpdateVerion(deviceName, version){
  const stmt = db.prepare('UPDATE esp32 SET version=? WHERE deviceName=?');

  stmt.run(version, deviceName);
}

module.exports = [FirmwareDbInit, GetAllFirmwareDevice, AddFirmwareDevice, GetVersionJson, UpdateVerion];
