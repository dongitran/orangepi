var Jimp = require('jimp');

var mainImage = new Jimp(1000, 1000, function (err, image) {
  image.opacity(0, function(err, image) {

  });
  
});



for(let x = 0; x < 100; x++){
  for(let y = 0; y < 500; y++){
    mainImage.setPixelColor(0xff00aaff, x, y);
  }
}
/*
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
*/


Jimp.read(mainImage, function (err, image) {
  image.write('out.png');
});



mainImage.getBase64(Jimp.AUTO, function(err, data) {  // Add err
  console.log(data); 
});