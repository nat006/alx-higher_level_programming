#!/usr/bin/node

// incrementAndCall function to be visible from outside
function incrementAndCall(number, theFunction) {
  let count = number + 1;
  theFunction(count);
}

module.exports = {
  incrementAndCall
}
