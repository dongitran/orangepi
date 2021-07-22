const notifier = require('node-notifier');
const si = require('systeminformation');

function CheckRamUsed(){
    si.mem()
    .then(data=>{
        if(data.active*100/data.total > 80){
            notifier.notify({
                title: 'Hey!',
                message: 'CPU Stress.......'
            });
        }
        //console.log(data.active*100/data.total);
        setTimeout(CheckRamUsed, 3000);
    })
    .catch(error =>{
        console.error(error);
        setTimeout(CheckRamUsed, 3000);
    });
}


CheckRamUsed();