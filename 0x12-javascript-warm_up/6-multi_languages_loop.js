#!/usr/bin/node
/*
const myVar = ['C is fun', 'Python is cool', 'Javascript is amazing'];
for (let i = 0; i < myVar.length; i++) {
  console.log(myVar[i]);
} */

const myVar = ['C is fun', 'Python is cool', 'Javascript is amazing'];
myVar.forEach((val, i) => {
  console.log(`${val}`);
});
