var Jimp = require('jimp');
  


Jimp.read('https://media.geeksforgeeks.org/wp-content/uploads/20190328185333/gfg111.png')
.then(lenna => {
  return lenna
    .resize(2560, 2560) // resize
    .quality(60) // set JPEG quality
    .greyscale() // set greyscale
    .rgba(false)
    .write('lena-small-bw.jpg'); // save
})
.catch(err => {
  console.error(err);
});

const img_url = "lena-small-bw.jpg";

Jimp.read(img_url, function (err, image) {
  image.getBase64(Jimp.AUTO, function(err, data) {  // Add err
    console.log(data.length); 
  });
});