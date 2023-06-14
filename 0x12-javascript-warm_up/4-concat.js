#!/usr/bin/node

const argv = process.argv;
if (!argv[2]) {
  console.log('undefined' + ' is ' + `${argv[3]}`);
} else if (!argv[3]) {
  console.log(`${argv[2]}` + ' is ' + 'undefined');
} else {
  console.log(`${argv[2]}` + ' is ' + `${argv[3]}`);
}

/* Another solution is this:
#!/usr/bin/node
console.log(process.argv[2] ? process.argv[2] : 'No argument');
*/
