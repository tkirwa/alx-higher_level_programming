#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

// Send a GET request to the specified API URL
request.get(apiUrl, (error, response, body) => {
  if (error) {
    // If an error occurred during the request, print the error object
    console.error(error);
  } else if (response.statusCode === 200) {
    // If the request was successful (status code 200), proceed

    // Parse the response body as JSON to access the tasks data
    const tasks = JSON.parse(body);

    // Create an empty object to store the number of completed tasks per user
    const completedTasks = {};

    // Loop through each task
    for (const task of tasks) {
      // Check if the task is completed (completed tasks have 'completed' property set to true)
      if (task.completed) {
        // Increment the count for the corresponding user ID or set it to 1 if the ID doesn't exist in the object
        completedTasks[task.userId] = (completedTasks[task.userId] || 0) + 1;
      }
    }

    // Print the object containing the number of completed tasks per user ID
    console.log(completedTasks);
  } else {
    // If the request returned an invalid response, print the status code
    console.log('An error occurred. Status code: ' + response.statusCode);
  }
});
