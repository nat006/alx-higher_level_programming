#!/usr/bin/node

const [, , argument] = process.argv;
const num = parseInt(argument);

if (!Number.isNaN(num)) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
