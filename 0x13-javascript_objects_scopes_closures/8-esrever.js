#!/usr/bin/node
exports.esrever = function (list) {
  let newList = [];
  let lastItemIndex = list.length - 1;
  while (lastItemIndex >= 0) {
    newList.push(list[lastItemIndex]);
    lastItemIndex--;
  }
  return newList;
};
