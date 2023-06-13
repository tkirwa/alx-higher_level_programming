#!/usr/bin/node

const dict = require('./101-data').dict;

const occurrences = {};
for (const key in dict) {
  const occurrence = dict[key];
  if (occurrence in occurrences) {
    occurrences[occurrence].push(key);
  } else {
    occurrences[occurrence] = [key];
  }
}

console.log(occurrences);
