#!/usr/bin/node

const argv = process.argv;
const hasArguments = argv[2] !== undefined;

if (hasArguments) {
  console.log(`${argv[2]}`);
} else {
  console.log('No argument');
}

/* Another solution is this:
#!/usr/bin/node
console.log(process.argv[2] ? process.argv[2] : 'No argument');
*/
