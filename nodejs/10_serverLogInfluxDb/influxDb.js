const { InfluxDB } = require('@influxdata/influxdb-client')

// You can generate a Token from the "Tokens Tab" in the UI
const token = 'VYwuwT3YNwffTJWTKytqeckOcRxPdW9X3ff8V72kx4Ykw9DvW-Wo_B875yyl00et81wzuCT9cSEC12RsSUT8sw=='
const org = 'IDEA'
const bucket = 'test1'

const client = new InfluxDB({ url: 'http://localhost:8086', token: token })

const { Point } = require('@influxdata/influxdb-client')

var timeStart = Date.now();
var counterRun = 0;
function WriteDb(device, id, jsonData){
    console.log(jsonData);
    let writeApi = client.getWriteApi(org, device)
    writeApi.useDefaultTags({ host: id })
    p = new Point("mem");
    for(let i = 0; i < jsonData.length; i++){
        if(Array.isArray(jsonData[i].v)){
            for(let j = 0; j < jsonData[i].v.length; j++){
                p.floatField(jsonData[i].n + j, jsonData[i].v[j]);
            }
        }
        else if(typeof(jsonData[i].v) == 'number'){
            p.floatField(jsonData[i].n, jsonData[i].v);
        }
        else{
            p.stringField(jsonData[i].n, jsonData[i].v);
        }
    }

    writeApi.writePoint(p)
    writeApi
        .close()    
        .then(() => {
            //setTimeout(sendRandom1, 1000);
            //console.log('Finished')
            counterRun++;
            if(counterRun >= 1000){
                console.log(counterRun/((Date.now() - timeStart)/1000));
                counterRun = 0;
                timeStart = Date.now();
            }
        })
        .catch(e => {
            console.log('\\nFinished ERROR')
        })
}

module.exports = WriteDb;
