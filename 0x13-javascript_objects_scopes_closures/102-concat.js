#!/usr/bin/node

const fs = require('fs');
const args = process.argv.slice(2);

const file1 = args[0];
const file2 = args[1];
const destination = args[2];

const content1 = fs.readFileSync(file1, 'utf8');
const content2 = fs.readFileSync(file2, 'utf8');
const combinedContent = content1 + '\n' + content2;

fs.writeFileSync(destination, combinedContent);
