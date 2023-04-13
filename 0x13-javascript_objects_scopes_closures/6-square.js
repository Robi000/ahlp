#!/usr/bin/node

const rec = require('./5-square');

class Square extends rec {
    charPrint (c) {
	if (c === undefined || c === '') {
	    c = 'X';
	}
	for (let i = 0; i < this.height; i++) {
	    let line = '';
	    for (let j = 0; j < this.width; j++) {
		line += c;
	    }
	    console.log(line);
	}
    }
}

module.exports = Square;
