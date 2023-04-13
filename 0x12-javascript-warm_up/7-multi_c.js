#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  let count = process.argv[2];
  while (count > 0) {
    console.log('C is fun');
    count--;
  }
}
