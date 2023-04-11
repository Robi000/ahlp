#!/usr/bin/node

const argv = require("process").argv[2];

const num = parseInt(argv);

for (let i = 0; i < num; i++) {
  let str = "";
  for (let j = 0; j < num; j++) {
    str = str + "x";
  }
  console.log(str);
}
