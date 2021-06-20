const Database = require('better-sqlite3');
const db = new Database('./db/firmware.db', { verbose: console.log });

db.exec('CREATE TABLE IF NOT EXISTS esp32 (deviceName TEXT, version TEXT)');

function GetVersion(){

}

function GetVersionJson(deviceName){
  const stmt = db.prepare('SELECT version FROM esp32 WHERE deviceName=?');

  result = stmt.all(deviceName);
  return result[0];
}

function UpdateVerion(deviceName, version){
  const stmt = db.prepare('UPDATE esp32 SET version=? WHERE deviceName=?');

  stmt.run(version, deviceName);
}

module.exports = [GetVersion, GetVersionJson, UpdateVerion];