#!/usr/bin/node
const S = require('./5-square.js');
module.exports = class Square extends S {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    let side = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        side += c;
      }
      console.log(side);
      side = '';
    }
  }
};
