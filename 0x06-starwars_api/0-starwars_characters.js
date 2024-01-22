#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode}`);
    process.exit(1);
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  // Function to fetch and display character names
  const printCharacterNames = (characterUrls, index = 0) => {
    if (index === characterUrls.length) {
      // All characters displayed, exit
      process.exit(0);
    }

    const characterUrl = characterUrls[index];
    request(characterUrl, (err, resp, charBody) => {
      if (err) {
        console.error(err);
        process.exit(1);
      }

      if (resp.statusCode !== 200) {
        console.error(`Error: ${resp.statusCode}`);
        process.exit(1);
      }

      const character = JSON.parse(charBody);
      console.log(character.name);

      // Continue to the next character
      printCharacterNames(characterUrls, index + 1);
    });
  };

  // Start fetching and displaying character names
  printCharacterNames(characters);
});
