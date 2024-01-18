#!/usr/bin/node
/**
 * Write a script that prints all characters of a Star Wars movie:
 * - The first argument is the Movie ID
 *        - example: 3 = “Return of the Jedi”
 * - Display one character name by line in the same order of the list
 *  “characters” in the /films/ response
 * - You must use the Star wars API
 * - You must use the module request
 */
const request = require("request");

const id = parseInt(process.argv[2], 10);

/**
 * Fetches the name of a Star Wars character from a given URL.
 * @param {string} url - The URL of the Star Wars character API.
 * @returns {Promise<string>} - A promise that resolves with the name of the character.
 */
const fetchCharacter = async (url) => {
  return new Promise((resolve, reject) => {
    request(url, (err, res, body) => {
      if (err) reject(err);
      resolve(JSON.parse(body).name);
    });
  });
};

/**
 * Fetches data for a Star Wars film and logs the names of its characters to the console.
 * @async
 * @function fetchFilm
 * @param {number} id - The ID of the film to fetch.
 * @returns {Promise<void>} - A Promise that resolves when all character names have been logged.
 */
const fetchFilm = async (id) => {
  const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;
  const body = await new Promise((resolve, reject) => {
    request(url, (err, res, body) => {
      if (err) reject(err);
      resolve(body);
    });
  });

  const filmData = JSON.parse(body);
  const characters = filmData.characters;
  for (let i = 0; i < characters.length; i++) {
    const charName = await fetchCharacter(characters[i]);
    console.log(charName);
  }
};

fetchFilm(id);
