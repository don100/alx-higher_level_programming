#!/usr/bin/node
const args = process.argv;
let x = 1;
if (parseInt(args[2])) {
  for (let i = 1; i <= parseInt(args[2]); i++) {
    x *= i;
  }
    console.log(x);
} else {
  console.log(1);
}
