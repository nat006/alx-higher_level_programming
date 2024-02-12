#!/usr/bin/node

const [ , , num ] = process.argv;
const count = parseInt(num);

if (!Number.isNaN(count)) {
  for (let i = 0; i < count; i++) {
    console.log("C is fun");
  }
} else {
  console.log("Missing number of occurrences");
}
