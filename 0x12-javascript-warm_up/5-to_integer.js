#!/usr/bin/node
// Prints message

const firstArgv = process.argv[2];

if (parseInt(firstArgv)) {
  console.log(`My number: ${parseInt(firstArgv)}`);
} else {
  console.log('Not a number');
}
