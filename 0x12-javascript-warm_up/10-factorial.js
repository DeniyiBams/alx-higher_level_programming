#!/usr/bin/node
// computes and print factorial

function factorial(num) {
  if (num === 1 || num === 0) {
    return 1;
  }
  return num * factorial(num - 1);
}

const factNum = parseInt(process.argv[2]);
if (isNaN(factNum)) {
  console.log(1);
} else {
  console.log(factorial(factNum));
}
