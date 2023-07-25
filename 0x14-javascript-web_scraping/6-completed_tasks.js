#!/usr/bin/node
// Computes the number of tasks completed by user id from jsonplaceholder.typicode.com API

const request = require('request');
const url = process.argv[2]; // Get the API URL from the command-line arguments

request(url, function (err, res, body) {
  if (err) {
    // If an error occurred during the request, print the error object
    console.log(err);
  }

  // Parse the response body as JSON to access the tasks data
  const tasks = JSON.parse(body);

  // Create an empty object to store the number of completed tasks per user
  const obj = {};

  // Loop through each task
  for (const task of tasks) {
    // Check if the task is completed (completed tasks have 'completed' property set to true)
    if (task.completed === true) {
      // Increment the count for the corresponding user ID or set it to 1 if the ID doesn't exist in the object
      if (obj[task.userId] === undefined) {
        obj[task.userId] = 1;
      } else {
        obj[task.userId]++;
      }
    }
  }

  // Print the object containing the number of completed tasks per user ID
  console.log(obj);
});
