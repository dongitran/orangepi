

var sqlite3 = require('sqlite3').verbose();
var db = new sqlite3.Database('./db/firmware.db',(err)=>{
  if(err){
    console.error(err.message);
  }
  else{
    console.log('Connected db ok');

    db.run("CREATE TABLE IF NOT EXISTS esp32 (deviceName TEXT, version TEXT)", (err)=>{
      let version = '';
      let deviceExist = false;
      db.run("SELECT deviceName deviceName, version version \
              FROM esp32 WHERE deviceName = ?", ['esp32DevKit'], (err, row)=>{
        console.log('-----------SELECT-----------');
        if(err){
          console.log(err);
        }
        else if(row != undefined){              
          console.log(row);
          console.log('deviceName: ' + row.deviceName);
          console.log("version: " + row.version);
          version = row.version + '-add';
          deviceExist = true;
        }

        if(deviceExist == false){
          db.run("INSERT INTO esp32(deviceName, version) VALUES(?,?)", ['esp32DevKit','init'], (err)=>{
            console.log('--------INSERT -------');
            console.log("INSERT ERROR: " + err);
          })
        }
        else{
          
          db.run("UPDATE esp32 SET version=? WHERE deviceName=?", [version,"esp32DevKit"], (err)=>{
            console.log(err);
            console.log('-------- UPDATE -------');
            console.log(version);
            console.log("UPDATE ERROR: " + err);
            console.log(this.changes)
          })
        }
        

      });
    });

    //var stmt = db.prepare("INSERT INTO esp32(deviceName, version) VALUES (?,?)");
    //for (var i = 0; i < 10; i++) {
    //    stmt.run([i + '', 'b']);
    //}
    //stmt.finalize();

    db.each("SELECT * FROM esp32 ", function(err, row) {
      console.log('---------SELECT ALL---------');
      console.log(row);
    });

    
    
    
    
  }
});

db.serialize(function() {
  
});

db.close();
