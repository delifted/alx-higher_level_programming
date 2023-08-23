#!/usr/bin/node

const request = require('request');

const apiURL = process.argv[2];

request(apiURL, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const movieData = JSON.parse(body);
  const wedgeAntillesMovies = movieData.results.filter(movie => movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
  );
  console.log(wedgeAntillesMovies.length);
});
