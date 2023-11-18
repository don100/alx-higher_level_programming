#!/usr/bin/node
const args = process.argv;
let x = '';
if (parseInt(args[2])) {
  for (let i = 0; i < parseInt(args[2]); i++) {
    x *= i;
  }
  for (let j = 0; j < parseInt(args[2]); j++) {
    console.log(x);
  }
} else {
  console.log('Missing size');
}
