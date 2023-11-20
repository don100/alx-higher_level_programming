#!/usr/bin/node
const dict = require('./101-data').dict;

let v = [...new Set(Object.values(dict))];
let a = [];
let d = {};
for (let i of v){
  for (let key in dict) {
    //console.log("Key: " + key + ", Value: " + dict[key]);
    if (dict[key] == i){
      a.push(key);
    }
  }
  d[i] = a;
  a = [];
}
console.log(d);
