#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch movie information. Status code:', response.statusCode);
    process.exit(1);
  }

  const movie = JSON.parse(body);

  if (!movie.characters || movie.characters.length === 0) {
    console.error('No characters found for this movie.');
    process.exit(1);
  }

  // Function to fetch character's name and print
  function fetchCharacterName (characterUrl) {
    request(characterUrl, function (error, response, characterBody) {
      if (error) {
        console.error('Error:', error);
        process.exit(1);
      }

      if (response.statusCode !== 200) {
        console.error('Failed to fetch character information. Status code:', response.statusCode);
        process.exit(1);
      }

      const character = JSON.parse(characterBody);
      console.log(character.name);
    });
  }

  // Fetch and print each character's name
  (async function () {
    for (const characterUrl of movie.characters) {
      await new Promise(resolve => {
        fetchCharacterName(characterUrl);
        setTimeout(resolve, 500); // Add a small delay to prevent rate limiting
      });
    }
  })();
});
