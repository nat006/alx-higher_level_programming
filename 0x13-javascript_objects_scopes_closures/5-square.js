#!/usr/bin/node
'use strict';

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return {}; // Return an empty object if conditions are met
    }
    this.width = w;
    this.height = h;
  }

  print () {
    if (this.width === undefined || this.height === undefined) {
      console.log('Empty Rectangle');
    } else {
      for (let i = 0; i < this.height; i++) {
        let row = '';
        for (let j = 0; j < this.width; j++) {
          row += 'X';
        }
        console.log(row);
      }
    }
  }

  rotate () {
    if (this.width !== undefined && this.height !== undefined) {
      const temp = this.width;
      this.width = this.height;
      this.height = temp;
    }
  }

  double () {
    if (this.width !== undefined && this.height !== undefined) {
      this.width *= 2;
      this.height *= 2;
    }
  }
}

class Square extends Rectangle {
  constructor (size) {
    super(size, size); // Call the constructor of Rectangle with the given size for both width and height
  }
}

// Example usage for Square
const square = new Square(5);
square.print();

module.exports = Square;
