#!/usr/bin/node

const argv = require("process").argv[2];

if (isNaN(argv)) {
  console.log("1");
} else {
  let ans = 1;
  for (let i = parseInt(argv); i > 0; i--) {
    ans = ans * i;
  }
  console.log(ans);
}
