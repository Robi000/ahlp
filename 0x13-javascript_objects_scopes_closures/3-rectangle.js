#!/usr/bin/node

class Rectangle {
    constructor (w, h) {
	// Create an empty object if width and/or height is an invalid number.
	if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) { return; }
	this.width = w;
	this.height = h;
    }

    print () {
	for (let i = 0; i < this.height; i++) {
	    let prt = '';
	    for (let j = 0; j < this.width; j++) {
		prt = prt + 'X';
	    }
	    console.log(prt);
	}
    }
}

module.exports = Rectangle;
