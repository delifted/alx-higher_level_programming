#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./6-completed_tasks.js <API_URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Error:', `Received status code ${response.statusCode}`);
    process.exit(1);
  }

  const tasks = JSON.parse(body);
  const completedTasksByUser = {};

  tasks.forEach(task => {
    if (task.completed) {
      if (!completedTasksByUser[task.userId]) {
        completedTasksByUser[task.userId] = 1;
      } else {
        completedTasksByUser[task.userId]++;
      }
    }
  });

  console.log(completedTasksByUser);
});
