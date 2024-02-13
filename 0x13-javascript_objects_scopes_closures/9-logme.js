#!/usr/bin/node
'use strict';

let numArgsPrinted = 0;

exports.logMe = function (item) {
  console.log(`${numArgsPrinted}: ${item}`);
  numArgsPrinted++;
};
