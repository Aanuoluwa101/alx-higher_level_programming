#!/usr/bin/node
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', (data, textStatus) => {
  for (const episode of data.results) {
    $('ul#list_movies').append($('<li></li>').text(episode.title));
  }
});
