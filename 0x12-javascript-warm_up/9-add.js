#!/usr/bin/node

function add(a, b) {
  return a + b;
}

const [ , , num1, num2 ] = process.argv;
const int1 = parseInt(num1);
const int2 = parseInt(num2);

if (!Number.isNaN(int1) && !Number.isNaN(int2)) {
  console.log(add(int1, int2));
} else {
  console.log("Invalid input, please provide two integers as arguments");
}
