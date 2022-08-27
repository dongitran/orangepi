var Jimp = require('jimp');

Jimp.read( 
  Buffer.from('' , 'base64')
).then(img=>{
  return img
    .quality(60) // set JPEG quality
    .rgba(false)
    .write('out.jpg'); // save
})

