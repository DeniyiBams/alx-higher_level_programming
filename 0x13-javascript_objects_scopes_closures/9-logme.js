#!/usr/bin/node
let globalIndex = 0;
exports.logMe = function (item) {
  console.log(`${globalIndex}: ${item}`);
  globalIndex++;
};
