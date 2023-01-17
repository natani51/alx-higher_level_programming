#!/usr/bin/node
const request = require('request');
const find = '/18/';
request(process.argv[2], function (error, response, body) {
  if (error) console.error(error);
  let num = 0;
  for (const film of JSON.parse(body).results) {
    for (const character of film.characters) {
      num += (character.endsWith(find) ? 1 : 0);
    }
  }
  console.log(num);
});
