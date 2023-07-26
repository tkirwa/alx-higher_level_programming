#!/usr/bin/node

const request = require('request');

// Get the API URL from the command line arguments (process.argv[2])
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Invalid API response:', response.statusCode);
    return;
  }

  const tasks = JSON.parse(body);

  const completedTasksByUser = {};

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

  // Output the completedTasksByUser object in the desired format
  console.log(JSON.stringify(completedTasksByUser));
});
