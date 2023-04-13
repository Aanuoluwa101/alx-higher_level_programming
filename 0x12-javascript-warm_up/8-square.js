#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const count = process.argv[2];
  for (let i = 0; i < count; i++) {
    console.log('X'.repeat(count));
  }
}
