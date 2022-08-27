crc16 = require('node-crc16')
const {performance} = require('perf_hooks')

time = performance.now();

a = crc16.checkSum('1503006b0003');

timeProcess = performance.now() - time;
console.log('timeProcess: ' + timeProcess)
