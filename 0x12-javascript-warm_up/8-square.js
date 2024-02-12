#!/usr/bin/node

const [ , , sizeArg ] = process.argv;
const size = parseInt(sizeArg);

if (!Number.isNaN(size)) {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
} else {
  console.log("Missing size");
}
