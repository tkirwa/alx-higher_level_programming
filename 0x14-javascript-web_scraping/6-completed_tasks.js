#!/usr/bin/node

// Include the 'request' module
const request = require('request');

// Make a GET request to the URL provided in the command-line arguments (process.argv[2])
request(process.argv[2], function (error, response, body) {
  if (!error) {
    // If the request was successful and no error occurred

    // Parse the response body as JSON to access the tasks data
    const todos = JSON.parse(body);

    // Create an empty object to store the number of completed tasks per user
    const completed = {};

    // Loop through each task using 'forEach' function
    todos.forEach((todo) => {
      // Check if the task is completed (completed tasks have 'completed' property set to true)
      // and if the user ID doesn't exist in the 'completed' object
      if (todo.completed && completed[todo.userId] === undefined) {
        // If the user ID doesn't exist in the 'completed' object and the task is completed,
        // initialize the count for this user ID to 1
        completed[todo.userId] = 1;
      } else if (todo.completed) {
        // If the user ID already exists in the 'completed' object and the task is completed,
        // increment the count for this user ID
        completed[todo.userId] += 1;
      }
    });

    // Print the object containing the number of completed tasks per user ID
    console.log(completed);
  }
});
