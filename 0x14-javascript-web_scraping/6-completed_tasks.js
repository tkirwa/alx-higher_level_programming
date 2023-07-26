#!/usr/bin/node
const request = require('request');

// Get the API URL from the command line arguments (process.argv[2])
request(process.argv[2], function (error, response, body) {
  // Check if there was an error in the HTTP request
  if (!error) {
    // Parse the response body (which is in JSON format) into a JavaScript object
    const todos = JSON.parse(body);

    // Create an object to store the count of completed tasks for each user
    const completed = {};

    // Iterate over each todo in the response
    todos.forEach((todo) => {
      // Check if the todo is completed (property 'completed' is true)
      if (todo.completed) {
        // If the user id is not in the 'completed' object, initialize it to 1.
        // Otherwise, increment the count by 1.
        if (completed[todo.userId] === undefined) {
          completed[todo.userId] = 1;
        } else {
          completed[todo.userId] += 1;
        }
      }
    });

    // Print the 'completed' object, which contains the count of completed tasks for each user
    console.log(completed);
  }
});
