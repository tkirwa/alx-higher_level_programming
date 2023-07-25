#!/usr/bin/node

const request = require('request');

// Make a GET request to the provided API URL
request(process.argv[2], function (error, response, body) {
  if (error) {
    // If an error occurred during the request, print the error message
    console.error(error);
  }

  const tasks = JSON.parse(body);
  const dict = {};

  // Iterate through the tasks and count completed tasks for each user
  for (let i = 0; i < tasks.length; i++) {
    const task = tasks[i];
    if (task.completed) {
      if (!dict[task.userId]) {
        dict[task.userId] = 1;
      } else {
        dict[task.userId] += 1;
      }
    }
  }

  // Print the dictionary containing the number of completed tasks for each user
  console.log(dict);
});

