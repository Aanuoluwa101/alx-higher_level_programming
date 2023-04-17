#!/usr/bin/node
exports.logMe = function (item) {
  let argCount = 0;

  function incr () {
    console.log(`${argCount}: ${item}`);
    argCount++;
  }
  return incr;
}

