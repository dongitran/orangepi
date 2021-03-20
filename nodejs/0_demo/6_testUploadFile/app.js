const http = require('http');
const formidable = require('formidable');
const fs = require('fs');
var mv = require('mv');
 
const server = http.createServer((req, res) => {
  if (req.url === '/' && req.method.toLowerCase() === 'post') {
    // parse a file upload
    const form = formidable({ multiples: false });

    form.parse(req, (err, fields, files) => {
      console.log(files);

      try{
        console.log(files.multipleFiles);
      }        
      catch(e){
        console.log('files.multipleFiles error');
      }

      try{
        console.log(files.multipleFiles.path);
      }        
      catch(e){
        console.log('files.multipleFiles.path error');
      }
      
      mv(files.multipleFiles.path, "uploads/" + files.multipleFiles.name, (err) => {
        if(err){
          console.log('Error: ' + err);
        }
        console.log('rename');
      });

      res.writeHead(200, { 'content-type': 'application/json' });
      res.end(JSON.stringify({ fields, files }, null, 2));
    });
 
    return;
  }
 
  // show a file upload form
  res.writeHead(200, { 'content-type': 'text/html' });
  res.end(`
    <h2>With Node.js <code>"http"</code> module</h2>
    <form action="/" enctype="multipart/form-data" method="post">
      <div>Text field title: <input type="text" name="title" /></div>
      <div>File: <input type="file" name="multipleFiles" multiple="multiple" /></div>
      <input type="submit" value="Upload" />
    </form>
  `);
});
 
server.listen(3000, () => {
  console.log('Server listening on http://localhost:3000/ ...');
});

