#!/usr/bin/node

const argv = require("process").argv;

function add(a, b) {
  return a + b;
}

if (isNaN(argv[2]) || isNaN(argv[2])) {
  console.log("NaN");
} else console.log(add(parseInt(argv[2]), parseInt(argv[3])));
