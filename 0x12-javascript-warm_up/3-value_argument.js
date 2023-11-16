#!/usr/bin/node
const args = process.argv;
if (args.length <= 2) {
  console.log('No argument');
} else {
  args.forEach((val, index) => {
    if (index >= 2) {
      console.log(val);
    }
  });
}
