#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const apiUrl = 'https://swapi-api.hbtn.io/api/films/';

request.get(apiUrl + movieId, (err, response, movieBody) => {
  if (err) {
    console.error(err);
  }
  const movieData = JSON.parse(movieBody);
  const characters = movieData.characters;

  characters.forEach((characterUrl) => {
    request.get(characterUrl, (charErr, charRes, charBody) => {
      if (charErr) {
        console.error(charErr);
      }
      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
    });
  });
});
