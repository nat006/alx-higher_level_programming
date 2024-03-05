#!/usr/bin/node

// add function to be visible from outside
const add = (num1, num2) => {
  return num1 + num2;
};

module.exports = {
  add
};
