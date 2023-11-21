#!/usr/bin/node

const args = process.argv;
const fs = require('fs')
let data = '';

fs.readFile(args[2].toString(), (err, dataA) => {
  if (err) throw err;
  data = dataA.toString();

  fs.readFile(args[3].toString(), (err, dataB) => {
    if (err) throw err;
    data += dataB.toString();

    fs.writeFile(args[4].toString(), data, (err) => {
      if (err) throw err;
    });
  });
});
