#!/usr/bin/node
let Integer = parseInt(process.argv[2], 10);
if (!isNaN(Integer) && Integer > 0) {
  for (Integer; Integer !== 0; Integer--) {
    console.log('C is fun');
  }
} else if (isNaN(Integer)) {
  console.log('Missing number of occurrences');
}
