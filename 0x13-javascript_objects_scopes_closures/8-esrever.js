#!/usr/bin/node

exports.esrever = function (list) {
    const rlist = [];
    // append to the beging of the list 
    list.forEach((item) => rlist.unshift(item); });
    return rlist;
};
