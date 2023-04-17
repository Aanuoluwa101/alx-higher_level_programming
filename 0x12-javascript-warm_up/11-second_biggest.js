#!/usr/bin/node

function secondBiggest (array) {
  let biggest = array[0];
  let second = array[1];

  for (let i = 0; i < array.length; i++) {
    if (second <= biggest) {
      if (array[i] > second && array[i] < biggest) {
        second = array[i];
      } else if (array[i] > second && array[i] > biggest) {
        second = biggest;
        biggest = array[i];
      }
    } else {
      if (array[i] > biggest && array[i] < second) {
        second = array[i];
      } else if (array[i] > second && array[i] > biggest) {
        biggest = array[i];
      }
    }
  }
  return (Math.min(second, biggest));
}

const arg = process.argv.slice(2);

if (arg.length < 4) {
  console.log(0);
} else {
  console.log(secondBiggest(arg));
}
