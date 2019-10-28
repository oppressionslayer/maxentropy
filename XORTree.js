// This server accepts a json request to reply with the XOR operations
// which get to a number, an example is
// curl -d '{"number":10009}' localhost:3000

const http = require('http');
//qs = require('querystring');
const { parse } = require('querystring');


const hostname = '127.0.0.1';
const port = 3000;

function Xploder(num,bits=1) {
  temp = BigInt(num) + BigInt(1)
  xnum = (temp * BigInt(Math.pow(2, bits)))-1n
  return xnum
}

function createGodsNum(num) {
   return ((2n<<BigInt(Math.ceil(Math.log2(num))-1)<<1n)-1n)^BigInt(num)
}

function Xploder(num,bits=1) {
  temp = BigInt(num) + BigInt(1)
  xnum = (temp * BigInt(Math.pow(2, bits)))-1n
  return xnum
}

function jsonifiedver(j) {
  var y=3n
  var o = {}
  o[0] = [];
  j=createGodsNum(j)
  console.log(j)
  doublin=0n
  doublin2=0n
  doublinanswer=0n
  prevdoublin=0n
  prevdoublin2=0n
  pattern='+'
  iterx=0n
  xplod=3
  for (x=0; x<1; x++) {
     while ( y < j)  {
       prevdoublin = doublin
       prevdoublin2 = doublinanswer
       y=Xploder(y)
       doublin=j-(((y*2n)+1n)^j) //jxorsubtractj(j,y)
       doublin2 = doublin/2n+1n
       if (doublin < 0n) {
          doublinanswer=doublin/2n
          //console.log(doublin/2n)
       } else {
          doublinanswer=(doublin/2n)+1n
          //console.log((doublin/2n)+1n)
       }
       dpd = doublin^prevdoublin
       dpd = dpd.toString()
       dpd2 =  doublinanswer^prevdoublin2
       dpd2 = dpd2.toString()
       dp2d2 = doublin2^prevdoublin2
       if (dp2d2 > 0n) {
         pattern='+'
       } else {
         pattern='-'
       }
       if ( x == 0 ) {
         prevdoub =  doublinanswer // (doublin/2n)+1n
       }
       equation =  prevdoub.toString()+"^"+pattern+"2**"+xplod.toString()
       prevdoub =  doublinanswer // (doublin/2n)+1n
       var data = {
         Y: y.toString(),
         J: j.toString(),
         DOUBLIN: doublin.toString(),
         DPD: dpd,
         DA: doublinanswer.toString(),
         DPD2: dpd2,
         PATTERN: pattern,
         EQUATION: equation
       };
       o[iterx] = [];
       xplod+=1
       o[iterx].push(data);
       //console.log(iterx,y,j,doublin, doublin^prevdoublin, doublinanswer, doublinanswer^prevdoublin2)
       iterx+=1n
     }
  }
  return o
}

const server = http.createServer((req, res) => {
  const methodType = req.method;
  if (methodType === "GET") {
    console.log("GET");
    res.statusCode = 200;
    res.setHeader('Content-Type', 'application/json'); 
    console.log(global.l);
    res.end(global.h3);
  } else if (methodType === 'POST') {
    console.log("POST")
    var body = ''
    req.on('data', function(data) { 
        body += data; // += chunk;
    });

    req.on('end', function() {
      global.l = JSON.parse(body);
      l = JSON.parse(body);
      global.h2=jsonifiedver(l.number);
      console.log("Just called jsonifiedver")
      global.h3 = JSON.stringify(h2);
      res.statusCode = 200;
      res.setHeader('Content-Type', 'application/json');
      console.log(global.l);
      res.end(global.h3);
    });
  }
});


server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
  //console.log(req.body);
});
Nadas-MBP:no
