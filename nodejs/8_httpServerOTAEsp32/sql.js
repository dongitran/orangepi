var sqlite3 = require('sqlite3').verbose();
var db = new sqlite3.Database('./db/firmware.db',(err)=>{
  if(err){
    console.error(err.message);
  }
  else{
    console.log('Connected db ok');
  }
});

db.serialize(function() {
  db.run("CREATE TABLE IF NOT EXISTS esp32 (deviceName TEXT, version TEXT)");

  //var stmt = db.prepare("INSERT INTO esp32(deviceName, version) VALUES (?,?)");
  //for (var i = 0; i < 10; i++) {
  //    stmt.run([i + '', 'b']);
  //}
  //stmt.finalize();

  db.each("SELECT * FROM esp32 ", function(err, row) {
    console.log(row);
  });

  //db.get("SELECT deviceName deviceName, version version \
  //        FROM esp32 WHERE deviceName = ?", ['0'], (err, row)=>{
  //          if(err){
  //            console.log(err);
  //          }
  //          else if(row != undefined){              
  //            console.log(row);
  //            console.log('deviceName: ' + row.deviceName);
  //            console.log("version: " + row.version);
  //          }
  //        });
});

function AddVersion(deviceName, version){
  console.log("AddVersion");
  db.run("INSERT INTO esp32(deviceName, version) VALUES(?,?)", [deviceName, version], (err)=>{
    if(err){
      console.log(err);
    }
  })
}
function GetVersion(deviceName){
  console.log('GetVersion');
  console.log(deviceName);
  db.get("SELECT version version FROM esp32 WHERE deviceName = ?", ["esp32DevKit"], (err, row)=>{
    console.log('err' + err);
    console.log('row' + row.version);
    if(err){
      console.log(err);
      return "0.0";
    }
    else if(row != undefined){
      console.log('GetVersion: ' + row.version);
      return row.version;
    }
    else{
      return "0.0";
    }
  });
  
}

function GetVersionJson(deviceName){
  console.log('GetVersion');
  console.log(deviceName);
  db.get("SELECT version version FROM esp32 WHERE deviceName = ?", ["esp32DevKit"], (err, row)=>{
    console.log('err' + err);
    console.log('row' + row.version);
    if(err){
      console.log(err);
      return "0.0";
    }
    else if(row != undefined){
      console.log('GetVersion: ' + row.version);
      var versionJson = {version: row.version};
      return versionJson;
    }
    else{
      return "0.0";
    }
  });
  
}

function UpdateVerion(deviceName, version){
  console.log('UpdateVerion');
  db.run("UPDATE esp32 SET version=? WHERE deviceName=?", [version, "esp32DevKit"], (err)=>{
    if(err){
      console.log(err);
    }
    else{
      console.log("UpdateVerion Ok!");
      return;
    }
  });

  AddVersion(deviceName, version);
}

//db.close();
module.exports = [GetVersion, GetVersionJson, UpdateVerion];
