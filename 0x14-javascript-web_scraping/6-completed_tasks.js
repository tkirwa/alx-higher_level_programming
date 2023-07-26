#!/usr/bin/node
const request = require('request');

// Get the API URL from the command line arguments (process.argv[2])
const url = process.argv[2];

// Create an object to store the count of completed tasks for each user
const myDict = {};

// Make an HTTP GET request to the provided API URL
request(url, function (err, data, body) {
  if (err) {
    // If there's an error in the request, log the error
    console.log(err);
  } else {
    // Parse the response body (which is in JSON format) into a JavaScript object
    const response = JSON.parse(body);

    // Iterate over each element (todo) in the response
    for (let i = 0; i < response.length; i++) {
      // Check if the todo is completed (property 'completed' is true)
      if (response[i].completed === true) {
        // If the user id is not in 'myDict', initialize it to 1.
        // Otherwise, increment the count by 1.
        if (myDict[response[i].userId] === undefined) {
          myDict[response[i].userId] = 1;
        } else {
          myDict[response[i].userId] += 1;
        }
      }
    }
  }

  // Print the 'myDict' object, which contains the count of completed tasks for each user
  console.log(myDict);
});
