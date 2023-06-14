#!/usr/bin/node

const numArgs = process.argv.length;

if (numArgs > 2) {
	console.log('Argument' + (numArgs > 3 ? 's' : '') + ' found');
} else {
	console.log('No argument');
}
