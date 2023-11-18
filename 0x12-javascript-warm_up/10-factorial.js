#!/usr/bin/node
const args = process.argv;

function factorial (a) {
  let x = 1;
  if (parseInt(a)) {
    for (let i = 1; i <= parseInt(a); i++) {
      x *= i;
    }
    console.log(x);
  } else {
    console.log(1);
  }
}

factorial(args[2]);
