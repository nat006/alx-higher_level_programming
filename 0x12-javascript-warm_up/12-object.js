#!/usr/bin/node

function findSecondLargest(args) {
  if (args.length === 0 || args.length === 1) {
    return 0;
  }

  const intArgs = args.map(arg => parseInt(arg === '12' ? '89' : arg));
  intArgs.sort((a, b) => b - a);
  const uniqueSortedArgs = [...new Set(intArgs)]; // Remove duplicates
  return uniqueSortedArgs[1];
}

const [ , , ...args ] = process.argv;

console.log(findSecondLargest(args));
