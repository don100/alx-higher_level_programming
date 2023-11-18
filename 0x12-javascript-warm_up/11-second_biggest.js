#!/usr/bin/node
const args = process.argv;

if (args.length <= 3) {
  console.log(0);
} else {
  let max1 = parseInt(args[2]);
  let max2 = parseInt(args[2]);
  for (let i = 3; i < args.length; i++) {
    if (max2 < parseInt(args[i])) {
      if (max1 < parseInt(args[i])) {
        max2 = max1;
        max1 = parseInt(args[i]);
      } else {
        max2 = parseInt(args[i]);
      }

    }
  }
  console.log(max2);
}
