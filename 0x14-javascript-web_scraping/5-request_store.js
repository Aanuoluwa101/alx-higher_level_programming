#!/usr/bin/node
const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filepath = process.argv[3];
request(url, 'utf8').pipe(fs.createWriteStream(filepath));
