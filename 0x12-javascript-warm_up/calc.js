#!/usr/bin/node

import { ops } from './calc_fns.js';

function calculate (a, b, operation) {
  return (operation(a, b));
};

const a = 2;
const b = 3;

// addition
console.log(`a + b = ${calculate(a, b, ops.add)}`);

// subtraction
console.log(`a - b = ${calculate(a, b, ops.sub)}`);

// division
console.log(`a / b = ${calculate(a, b, ops.div)}`);

// multiplication
console.log(`a * b = ${calculate(a, b, ops.mul)}`);

// power
console.log(`a ** b = ${calculate(a, b, ops.pow)}`);
