#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

// Make the API request and process the data
request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode === 200) {
    const tasks = JSON.parse(body);
    const completedTasksByUser = {};

    // Count completed tasks for each user
    tasks.forEach(task => {
      if (task.completed) {
        if (completedTasksByUser[task.userId] === undefined) {
          completedTasksByUser[task.userId] = 1;
        } else {
          completedTasksByUser[task.userId]++;
        }
      }
    });

    console.log(completedTasksByUser);
  } else {
    console.error('Error:', response.statusCode);
  }
});
