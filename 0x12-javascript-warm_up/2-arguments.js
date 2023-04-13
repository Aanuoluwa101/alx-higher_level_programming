#!/usr/bin/node
const argListLen = process.argv.length;
console.log(argListLen === 2 ? 'No argument' : argListLen === 3 ? 'Argument found' : 'Arguments found');
