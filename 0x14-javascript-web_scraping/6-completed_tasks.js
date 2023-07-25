#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    // If an error occurred during the request, print the error object
    console.log(err);
  } else if (response.statusCode === 200) {
    // If the request was successful (status code 200), proceed

    // Create an empty object to store the number of completed tasks per user
    const completed = {};

    // Parse the response body as JSON to access the tasks data
    const tasks = JSON.parse(body);

    // Loop through each task
    for (const i in tasks) {
      const task = tasks[i];
      // Check if the task is completed (completed tasks have 'completed' property set to true)
      if (task.completed === true) {
        // Increment the count for the corresponding user ID or set it to 1 if the ID doesn't exist in the object
        if (completed[task.userId] === undefined) {
          completed[task.userId] = 1;
        } else {
          completed[task.userId]++;
        }
      }
    }

    // Print the object containing the number of completed tasks per user ID
    console.log(completed);
  } else {
    // If the request returned an invalid response, print the status code
    console.log('An error occurred. Status code: ' + response.statusCode);
  }
});
