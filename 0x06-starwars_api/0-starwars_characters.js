#!/usr/bin/node
// Prints all characters of a star wars movie
const request = require('request');

const args = process.argv;
const id = args[2];

request(`https://swapi-api.alx-tools.com/api/films/${id}`,
  (err, res, body) => {
    if (!err) {
      const characters = JSON.parse(body).characters;

      for (const character of characters) {
        request(character, (err, res, body) => {
          if (!err) {
            const name = JSON.parse(body).name;
            console.log(name);
          }
        });
      }
    }
  });
