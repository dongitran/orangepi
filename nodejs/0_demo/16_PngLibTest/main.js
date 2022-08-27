var PNGlib = require('pnglib');
var p = new PNGlib(50, 50, 256);

for (var x = 0; x < 50; x++)
    for (var y = 0; y < 50; y++)
        p.buffer[p.index(x, y)] = p.color(0,0,0,255);

    for (var x = 20; x < 30; x++)
        for (var y = 30; y < 40; y++)
            p.buffer[p.index(x, y)] = p.color(0,255,0,255);

            for (var x = 0; x < 10; x++)
            for (var y = 0; y < 10; y++)
                p.buffer[p.index(x, y)] = p.color(255,255,0,255);

console.log('<img src="data:image/png;base64,' + p.getBase64() + '">');