#!/usr/bin/node
class Rectangle {
    // < 0 will create empty obj
    constructor (w, h) {
	if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) { return; }
	this.width = w;
	this.height = h;
    }
}

module.exports = Rectangle;
