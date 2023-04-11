#!/usr/bin/node

const argv = require("process").argv[2];

const num = parseInt(argv);

for (let i = 0; i < num; i++) {
  console.log("C is fun");
}
