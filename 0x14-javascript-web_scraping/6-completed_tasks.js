#!/usr/bin/node

const request = require('request');

// Get the API URL from the command-line arguments
const apiUrl = process.argv[2];

// Send a GET request to the specified API URL
request.get(apiUrl, (error, response, body) => {
  if (error) {
    // If an error occurred during the request, print the error object
    console.error(error);
  } else {
    // Parse the response body as JSON to access the tasks data
    const tasksData = JSON.parse(body);

    // Create an empty object to store the number of completed tasks per user
    const completedTasksCount = {};

    // Loop through each task
    for (const task of tasksData) {
      // Check if the task is completed (completed tasks have 'completed' property set to true)
      if (task.completed) {
        // Increment the count for the corresponding user ID or set it to 1 if the ID doesn't exist in the object
        completedTasksCount[task.userId] = (completedTasksCount[task.userId] || 0) + 1;
      }
    }

    // Print the object containing the number of completed tasks per user ID
    console.log(completedTasksCount);
  }
});
