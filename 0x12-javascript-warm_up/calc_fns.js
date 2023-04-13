#!/usr/bin/node

const ops = {
  add: function (a, b) {
    return (a + b);
  },
  sub: function (a, b) {
    return (a - b);
  },
  mul: function (a, b) {
    return (a * b);
  },
  div: function (a, b) {
    return (a / b);
  },
  pow: function (a, b) {
    return (a ** b);
  }
};

export ops;
