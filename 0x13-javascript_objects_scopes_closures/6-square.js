#!/usr/bin/node
'use strict';

class Square extends require('./5-square.js') {
  charPrint(c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

// Example usage for Square
const square = new Square(4);
square.charPrint(); // Output using default character 'X'
square.charPrint('#'); // Output using '#' character

module.exports = Square;
