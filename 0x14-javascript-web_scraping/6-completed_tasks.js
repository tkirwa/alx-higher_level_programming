#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    // If an error occurred during the request, print the error object
    console.log(error);
  } else if (response.statusCode === 200) {
    // If the request was successful (status code 200), proceed

    // Create an empty object to store the number of completed tasks per user
    const dic = {};

    // Parse the response body as JSON to access the tasks data
    const tasks = JSON.parse(body);

    // Loop through each task
    for (const i in tasks) {
      // Check if the task is completed (completed tasks have 'completed' property set to true)
      if (tasks[i].completed) {
        // Increment the count for the corresponding user ID or set it to 1 if the ID doesn't exist in the object
        dic[tasks[i].userId] = (dic[tasks[i].userId] || 0) + 1;
      }
    }

    // Print the object containing the number of completed tasks per user ID
    console.log(dic);
  } else {
    // If the request returned an invalid response, print the status code
    console.log('Error: ' + response.statusCode);
  }
});
