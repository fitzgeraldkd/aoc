const fs = require('fs');
const inputs = fs
  .readFileSync("inputs.txt", "utf8")
  .split("\n")
  // .map(item => parseInt(item, 10));
  .map(item => item.trim());

const sample = fs
  .readFileSync("sample.txt", "utf8")
  .split("\n")
  // .map(item => parseInt(item, 10));
  .map(item => item.trim());

console.log(sample);
console.log(inputs);

let hor = 0;
let ver = 0;
let aim = 0;
inputs.forEach(move => {
  // console
  let [direction, amount] = move.split(' ');
  console.log(amount)
  amount = parseInt(amount, 10);
  if (direction === 'forward') {
    hor += amount
    ver += aim * amount
  }
  if (direction === 'down') aim += amount
  if (direction === 'up') aim -= amount
});

console.log(hor * ver)