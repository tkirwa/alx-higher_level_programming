#!/usr/bin/node

const request = require('request');

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

// Make a GET request to the API URL using the 'request' module
request(apiUrl, (error, response, body) => {
  if (error) {
    // If there's an error, log and exit
    console.error('Error:', error);
    return;
  }

  // Check if the API responded with a valid status code (200 means success)
  if (response.statusCode !== 200) {
    console.error('Invalid API response:', response.statusCode);
    return;
  }

  // Parse the response body (which is in JSON format) into a JavaScript object
  const tasks = JSON.parse(body);

  // Create an empty object to store the count of completed tasks for each user
  const completedTasksByUser = {};

  // Iterate over each task in the response
  tasks.forEach(task => {
    // Check if the task is completed (property 'completed' is true)
    if (task.completed) {
      // If the user id is not already in the completedTasksByUser object,
      // initialize it to 1. Otherwise, increment the count by 1.
      if (!completedTasksByUser[task.userId]) {
        completedTasksByUser[task.userId] = 1;
      } else {
        completedTasksByUser[task.userId]++;
      }
    }
  });

  // Print the completedTasksByUser object, which contains the count of completed tasks for each user
  console.log(completedTasksByUser);
});

