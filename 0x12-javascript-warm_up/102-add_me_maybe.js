#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  if (isNaN(number)) return;
  theFunction(parseInt(number) + 1);
};
