#!/usr/bin/node

const argv = process.argv;

// if (argv[2])
const number = parseInt(argv[2]);

if (isNaN(number)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < number; i++) {
    console.log('C is fun');
  }
}

/* Another solution is this:
#!/usr/bin/node
const argv0 = process.argv[2];
const argv1 = process.argv[3];

console.log(`${argv0} is ${argv1}`);
*/
