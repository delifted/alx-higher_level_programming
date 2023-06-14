#!/usr/bin/node

const a = process.argv[2];

function fac (a) {
  if (!a) {
    return 1;
  } else {
    return a * fac(a - 1);
  }
}

console.log(fac(parseInt(a)));
