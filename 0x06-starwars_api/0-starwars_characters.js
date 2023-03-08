#!/usr/bin/node
// Prints all characters of a star wars movie
const request = require('request');
const util = require('util');

const call = util.promisify(request);

const args = process.argv;
const id = args[2];

async function getCharacters () {
  const res = await call(`https://swapi-api.alx-tools.com/api/films/${id}`);
  return JSON.parse(res.body).characters;
}

getCharacters()
  .then(async (characters) => {
    for (const character of characters) {
      const res = await call(character);
      const name = JSON.parse(res.body).name;
      console.log(name);
    }
  });
