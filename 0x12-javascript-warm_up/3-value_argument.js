#!/usr/bin/node

const argv = process.argv;
const hasArguments = argv[2] !== undefined;

if (hasArguments) {
  console.log(`${argv[2]}`);
} else {
  console.log('No argument');
}
