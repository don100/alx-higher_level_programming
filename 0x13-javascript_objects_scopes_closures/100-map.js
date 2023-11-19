#!/usr/bin/node
const list = require('./100-data').list;

console.log(list);

const map1 = list.map((i, x) => i * x);

console.log(map1);
