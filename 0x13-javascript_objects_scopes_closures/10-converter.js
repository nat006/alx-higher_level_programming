#!/usr/bin/node
'use strict';

exports.converter = function(base) {
  function convert(num) {
    if (num < base) {
      process.stdout.write(num.toString(base).toUpperCase());
    } else {
      convert(Math.floor(num / base));
      process.stdout.write((num % base).toString(base).toUpperCase());
    }
  }

  convert;
};
