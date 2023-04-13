#!/usr/bin/node

const dict = require('./101-data').dict;

const newe = {};


Object.values(dict).forEach((occurrence) => {
    if (Object.keys(newDict).indexOf(occurrence) === -1) {
	newe[occurrence] = []
	const userId= Object.entries(dict).filter(([key, value]) => {
	    return occurrence === value;
	});

	userId.forEach(item => {
	    newe[occurrence].push(item[0]);
	});
    }
});
console.log(newe);
