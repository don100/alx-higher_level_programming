#!/usr/bin/node
const args = process.argv;
if(args.length > 2){
  for (let x = 0; x < parseInt(args[2]); x++) {
  console.log('C is fun');
}
} else {
  console.log('Missing number of occurrences');
}
