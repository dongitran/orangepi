const Database = require('better-sqlite3');
const db = new Database('./db/deviceActivityLog.db'); //, { verbose: console.log });
let markNoReadCount = 0;
function DeviceActivityLogDbInit(){
  db.exec('CREATE TABLE IF NOT EXISTS deviceActivityLog (id TEXT, dateTime INTEGER, content TEXT)');
  db.exec('CREATE TABLE IF NOT EXISTS deviceActivityMarkNoRead (id INTEGER, count INTEGER)');

  // Check number mark read is not exist -> insert
  const stmtSelect = db.prepare('SELECT * FROM deviceActivityMarkNoRead WHERE id=?');
  result = stmtSelect.all(0);

  console.log(result);
  if(result.length == 0){
    const stmtInsert = db.prepare('INSERT INTO deviceActivityMarkNoRead(id, count) VALUES(?, ?)');

    stmtInsert.run(0, 0);
  }
  else{
    markNoReadCount = result[0].count;
  }
}

function GetAllLogDb(){
  const stmt = db.prepare('SELECT * FROM deviceActivityLog');

  result = stmt.all();
  return result;
}

function AddDeviceActivityLogToDb(log){
  const stmt = db.prepare('INSERT INTO deviceActivityLog(id, dateTime, content) VALUES(?, ?, ?)');

  stmt.run(log.id, log.dateTime, log.content);
}

function GetMarkNoReadCount(){
  return markNoReadCount;
}

function IncreaseMarkNoReadCount(){
  const stmt = db.prepare('UPDATE deviceActivityMarkNoRead SET count=? WHERE id=?');

  markNoReadCount++;
  stmt.run(markNoReadCount, 0);
}

function ResetMarkNoReadCount(){
  const stmt = db.prepare('UPDATE deviceActivityMarkNoRead SET count=? WHERE id=?');

  markNoReadCount = 0;
  stmt.run(markNoReadCount, 0);
}

module.exports = [DeviceActivityLogDbInit, GetAllLogDb, AddDeviceActivityLogToDb, GetMarkNoReadCount, IncreaseMarkNoReadCount, ResetMarkNoReadCount];
