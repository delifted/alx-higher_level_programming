#!/usr/bin/node

const argv = process.argv;

//if (argv[2])
const number = parseInt(argv[2]);

if (!argv[2] || isNaN(number)) {
	console.log('Not a number');
	} else {
		console.log('My number:', number);
	}

/* Another solution is this:
#!/usr/bin/node
const argv0 = process.argv[2];
const argv1 = process.argv[3];

console.log(`${argv0} is ${argv1}`);
*/
