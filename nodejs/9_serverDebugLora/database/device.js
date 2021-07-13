const Database = require('better-sqlite3');
const db = new Database('./db/device.db');  //, { verbose: console.log });

function DeviceDbInit(){
  db.exec('CREATE TABLE IF NOT EXISTS esp32 (id TEXT, type TEXT, version TEXT, status TEXT, timeUpdate INTEGER)');
}

function GetAllDeviceDb(){
  const stmt = db.prepare('SELECT * FROM esp32');

  result = stmt.all();
  return result;
}

function AddDeviceToDb(id, type, version, status, timeUpdate){
  const stmt = db.prepare('INSERT INTO esp32(id, type, version, status, timeUpdate) VALUES(?, ?, ?, ?, ?)');

  stmt.run(id, type, version, status, timeUpdate);
}

function UpdateStatusToDb(id, status){
  const stmt = db.prepare('UPDATE esp32 SET status=? WHERE id=?');

  stmt.run(status, id);
}

function UpdateVersionToDb(id, version){
  const stmt = db.prepare('UPDATE esp32 SET version=? WHERE id=?');

  stmt.run(version, id);
}

function UpdateTimeUpdateToDb(id, timeUpdate){
  const stmt = db.prepare('UPDATE esp32 SET timeUpdate=? WHERE id=?');

  stmt.run(timeUpdate, id);
}

module.exports = [DeviceDbInit, GetAllDeviceDb, AddDeviceToDb, UpdateStatusToDb, UpdateVersionToDb, UpdateTimeUpdateToDb];
