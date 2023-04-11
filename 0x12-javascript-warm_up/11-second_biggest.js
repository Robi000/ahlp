#!/usr/bin/node

const argv = require("process").argv;

const giv = [];

for (let i = 2; i < argv.length; i++) {
  giv.push(parseInt(argv[i]));
}

giv.sort((a, b) => a - b);

if (giv.length < 2) {
  console.log("0");
} else {
  console.log(nums[nums.length - 2]);
}
