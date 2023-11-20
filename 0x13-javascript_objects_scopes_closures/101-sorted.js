#!/usr/bin/node
const dict = require('./101-data').dict;

const v = [...new Set(Object.values(dict))];
let a = [];
const d = {};
for (const i of v) {
  for (const key in dict) {
    // console.log("Key: " + key + ", Value: " + dict[key]);
    if (dict[key] === i) {
      a.push(key);
    }
  }
  d[i] = a;
  a = [];
}
console.log(d);
