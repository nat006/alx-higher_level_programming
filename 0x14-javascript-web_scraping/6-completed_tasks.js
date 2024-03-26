#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const completedTasksByUser = {};
    const todos = JSON.parse(body);

    for (const todo of todos) {
      if (todo.completed) {
        const userId = todo.userId;
        completedTasksByUser[userId] = completedTasksByUser[userId] ? completedTasksByUser[userId] + 1 : 1;
      }
    }

    console.log(completedTasksByUser);
  } else {
    console.log(`An error occurred. Status code: ${response.statusCode}`);
  }
});
