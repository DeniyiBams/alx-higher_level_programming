#!/usr/bin/node
// prints x times 'C is fun'

const num = process.argv[2];

if (typeof num === 'undefined') {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
