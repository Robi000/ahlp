#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  if (isNaN(x)) {
    return;
  }
  for (let i = parseInt(x); i > 0; i--) {
    theFunction();
  }
};
