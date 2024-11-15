#!/usr/bin/node
// script that prints all characters of a Star Wars movie using Starwars API

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

// console.log(process.argv)
// console.log(url)

request(url, (error, response, body) => {
  if (error) {
    console.error('Error', error);
  } else if (response.statusCode !== 200) {
    console.error('Failed with status code:', response.statusCode);
  } else {
    const content = JSON.parse(body);
    const characters = content.characters;
    const characterNames = characters.map(charUrl => new Promise((resolve, reject) => {
      request(charUrl, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          resolve(JSON.parse(body).name);
        }
      });
    })
    );
    Promise.all(characterNames)
      .then(name => console.log(name.join('\n')))
      .catch(nameErr => console.err(nameErr));
  }
});
