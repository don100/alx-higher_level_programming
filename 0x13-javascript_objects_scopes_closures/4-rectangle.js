#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let side = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        side += 'X';
      }
      console.log(side);
      side = '';
    }
  }

  rotate () {
    const a = this.width;
    this.width = this.height;
    this.height = a;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
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
