const fs = require('fs');
const inputs = fs
  .readFileSync("inputs.txt", "utf8")
  // .split("\n")
  // .map(item => parseInt(item, 10));
  // .map(item => item.trim());
  .trim();

console.log(inputs);

let [x, y] = [0, 0]
let [x2, y2] = [0, 0]
const houses = {};
houses['0,0'] = true
let robot = false;
inputs.split('').forEach(item => {
  if (robot) {
    if (item === '>') x2 += 1;
    if (item === '<') x2 -= 1;
    if (item === 'v') y2 -= 1;
    if (item === '^') y2 += 1;
    houses[`${x2},${y2}`] = true
  } else {
    if (item === '>') x += 1;
    if (item === '<') x -= 1;
    if (item === 'v') y -= 1;
    if (item === '^') y += 1;
    houses[`${x},${y}`] = true
  }
  robot = !robot
})

console.log(Object.keys(houses).length)