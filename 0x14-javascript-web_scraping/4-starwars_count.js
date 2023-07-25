#!/usr/bin/node

const request = require('request');

// Get the API URL from the command-line arguments
const apiUrl = process.argv[2];

// Wedge Antilles character ID
const wedgeAntillesId = 18;

// Send a GET request to the Star Wars API
request.get(apiUrl, (error, response, body) => {
  if (error) {
    // If an error occurred during the request, print the error object
    console.error(error);
  } else {
    // Parse the response body as JSON to access the movie data
    const movieData = JSON.parse(body);

    // Filter the movie data to find the movies where Wedge Antilles is present
    const moviesWithWedgeAntilles = movieData.results.filter(movie =>
      movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntillesId}/`)
    );

    // Print the number of movies where Wedge Antilles is present
    console.log(moviesWithWedgeAntilles.length);
  }
});
