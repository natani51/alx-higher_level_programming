#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) console.error(error);
  const todos = JSON.parse(body);
  const usersCompleted = {};
  for (const todo of todos) {
    if (todo.completed === true) {
      if (todo.userId in usersCompleted) {
        usersCompleted[todo.userId] += 1;
      } else {
        usersCompleted[todo.userId] = 1;
      }
    }
  }
  console.log(usersCompleted);
});
