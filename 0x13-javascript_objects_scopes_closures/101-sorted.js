#!/usr/bin/node

const dict = require('./101-data').dict;

const occurrences = {};
for (const key in dict) {
  const occurrence = dict[key];
  if (occurrence in occurrences) {
    occurrences[occurrence].push(key.toString());
  } else {
    occurrences[occurrence] = [key.toString()];
  }
}

console.log(occurrences);
