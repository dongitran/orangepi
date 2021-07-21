const { InfluxDB } = require('@influxdata/influxdb-client')

// You can generate a Token from the "Tokens Tab" in the UI
const token = 'VYwuwT3YNwffTJWTKytqeckOcRxPdW9X3ff8V72kx4Ykw9DvW-Wo_B875yyl00et81wzuCT9cSEC12RsSUT8sw=='
const org = 'IDEA'
const bucket = 'test1'

const client = new InfluxDB({ url: 'http://localhost:8086', token: token })

const { Point } = require('@influxdata/influxdb-client')




function sendRandom1() {
    let writeApi = client.getWriteApi(org, bucket)
    writeApi.useDefaultTags({ host: 'host1' })
    point = new Point('mem')
        .floatField('val1', parseInt(Math.random() * 25))
        .floatField('val2', parseInt(Math.random() * 12))
        .floatField('type', "1")
    writeApi.writePoint(point)
    writeApi
        .close()    
        .then(() => {
            console.log('FINISHED')
            setTimeout(sendRandom1, 1000);
        })
        .catch(e => {
            console.error(e)
            console.log('\\nFinished ERROR')
        })
    
}

function sendRandom2() {
    let writeApi = client.getWriteApi(org, bucket)
    writeApi.useDefaultTags({ host: 'host1' })
    point = new Point('mem')
        .floatField('val3', parseInt(Math.random() * 25))
        .floatField('val4', parseInt(Math.random() * 12))
        .floatField('type', "2")
    writeApi.writePoint(point)
    writeApi
        .close()
        .then(() => {
            console.log('FINISHED')
            setTimeout(sendRandom2, 1000);
        })
        .catch(e => {
            console.error(e)
            console.log('\\nFinished ERROR')
        })
    
}


setTimeout(sendRandom1, 1000);
setTimeout(sendRandom2, 1000);
