#!/usr/bin/node
// prints x times 'C is fun'

const myVar = 'C is fun';
const num = process.argv[2];

if (typeof num === 'undefined') {
  console.log('Missing number of occurences');
}

if (num > 0) {
  let i = 0;
  while (i < num) {
    console.log(myVar);
    i++;
  }
} else {
  return;
}
