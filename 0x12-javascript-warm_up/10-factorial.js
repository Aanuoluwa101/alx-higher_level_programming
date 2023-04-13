#!/usr/bin/node
const arg = process.argv[2];

function factorial (num) {
  if (num === 0) {
    return 1;
  }
  return (num * factorial(num - 1));
}

if (isNaN(arg) || Number(arg) === 0) {
  console.log('1');
} else {
  console.log(factorial(arg));
}
