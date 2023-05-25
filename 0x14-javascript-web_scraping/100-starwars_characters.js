#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, 'utf8', (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    JSON.parse(body).characters.forEach(character => {
      request(character, 'utf8', (error, response, body) => {
        if (error) {
          console.error(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
