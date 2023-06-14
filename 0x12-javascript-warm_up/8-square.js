#!/usr/bin/node

const argv = process.argv;

// if (argv[2])
const number = parseInt(argv[2]);

if (isNaN(number)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < number; i++) {
    let j = 0;
    let myVar = '';

    while (j < number) {
      myVar = myVar + 'X';
      j++;
    }
    console.log(myVar);
  }
}

/* Another solution is this:
#!/usr/bin/node
const argv0 = process.argv[2];
const argv1 = process.argv[3];

console.log(`${argv0} is ${argv1}`);
*/
