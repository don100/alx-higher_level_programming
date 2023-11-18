#!/usr/bin/node
const args = process.argv;
if (parseInt(args[2])) {
  for (let i = 0; i < parseInt(args[2]); i++) {
    console.log('X');
  }
} else {
  console.log('Missing size');
}
