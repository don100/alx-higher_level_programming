#!/usr/bin/node
const args = process.argv;

if (args.length <= 3) {
  console.log(0);
} else {
  let max1 = args[2];
  let max2 = args[3];
  for (let i = 3; i < args.length; i++) {
    if (max1 < args[i]) {
      max2 = max1;
      max1 = args[i];
    }
  }
  console.log(max2);
}
