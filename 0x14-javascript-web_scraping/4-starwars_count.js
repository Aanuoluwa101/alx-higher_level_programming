#!/usr/bin/node
const request = require('request');

const getId = element => { return parseInt(element.match(/\d+/)[0]); };

const url = process.argv[2];
request(url, (error, response, body) => {
  if (error || response.statusCode !== 200) {
    console.error(error);
    return;
  }
  let count = 0;
  const data = JSON.parse(body);
  data.results.forEach(episode => {
    episode.characters.forEach(element => {
      if (getId(element) === 18) {
        count++;
      }
    });
  });
  console.log(count);
});
