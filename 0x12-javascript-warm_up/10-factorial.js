#!/usr/bin/node

function factorial(n) {
  if (n === 0 || Number.isNaN(n)) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const [ , , num ] = process.argv;
const int = parseInt(num);

console.log(factorial(int));
