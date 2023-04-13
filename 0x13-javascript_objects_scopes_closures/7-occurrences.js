#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
    // filter the items and return the length of the item
    return (list.filter((item) => searchElement === item)).length;
};
