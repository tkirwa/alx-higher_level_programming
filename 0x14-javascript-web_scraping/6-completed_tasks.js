#!/usr/bin/node

const request = require('request');

// Make a GET request to the provided API URL
request(process.argv[2], function (error, response, body) {
  if (error) {
    // If an error occurred during the request, print the error message
    console.error(error);
  }

  // Parse the response body (JSON) and reduce it to a dictionary of completed tasks by user ID
  const dict = JSON.parse(body).reduce((acc, elem) => {
    if (!acc[elem.userId]) {
      // If the user ID does not exist in the dictionary, initialize it to 1 if the task is completed
      if (elem.completed) {
        acc[elem.userId] = 1;
      }
    } else {
      // If the user ID already exists in the dictionary, increment the count if the task is completed
      if (elem.completed) {
        acc[elem.userId] += 1;
      }
    }
    return acc;
  }, {});

  // Print the dictionary containing the number of completed tasks for each user
  console.log(dict);
});
