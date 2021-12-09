const fs = require('fs');
const inputs = fs
  .readFileSync("inputs.txt", "utf8")
  .split("\n")
  .map(item => item.split('').map(num => parseInt(num)));
  // .map(item => item.trim());

// console.log(inputs);

const part1 = (inputs) => {
  let sum = 0;
  for (let y=0; y<inputs.length; y++) {
    for (let x=0; x<inputs[y].length; x++) {
      let value = inputs[y][x];
      if (x > 0 && inputs[y][x-1] <= value) continue;
      if (y > 0 && inputs[y-1][x] <= value) continue;
      if (x < inputs[y].length-1 && inputs[y][x+1] <= value) continue;
      if (y < inputs.length-1 && inputs[y+1][x] <= value) continue;
      sum += (value + 1);
    }
  }
  return sum;
};

const results1 = part1(inputs);

console.log(results1);

const part2 = (inputs) => {
  let lowpoints = [];
  for (let y=0; y<inputs.length; y++) {
    for (let x=0; x<inputs[y].length; x++) {
      let value = inputs[y][x];
      if (x > 0 && inputs[y][x-1] <= value) continue;
      if (y > 0 && inputs[y-1][x] <= value) continue;
      if (x < inputs[y].length-1 && inputs[y][x+1] <= value) continue;
      if (y < inputs.length-1 && inputs[y+1][x] <= value) continue;
      lowpoints.push([x, y])
    }
  }

  let basinSizes = [];
  let basins = [];
  for (const lowpoint of lowpoints) {
    let size = 0;
    let basin = [];
    let pointsToCheck = [[...lowpoint]]
    let checkedPoints = {};
    while (pointsToCheck.length > 0) {
      const [x, y] = pointsToCheck.pop();
      if (inputs[y][x] === 9 || `${x},${y}` in checkedPoints) {
        // checkedPoints[`${x},${y}`] = true;
      } else {
        size++;
        basin.push([x, y, inputs[y][x]]);
        if (x > 0) {
          if (!(`${x-1},${y}` in checkedPoints)) pointsToCheck.push([x-1, y]) 
        }
        if (y > 0) {
          if (!(`${x},${y-1}` in checkedPoints)) pointsToCheck.push([x, y-1]) 
        }
        if (x < inputs[y].length - 1) {
          if (!(`${x+1},${y}` in checkedPoints)) pointsToCheck.push([x+1, y]) 
        }
        if (y < inputs.length - 1) {
          if (!(`${x},${y+1}` in checkedPoints)) pointsToCheck.push([x, y+1]) 
        }
      }
      checkedPoints[`${x},${y}`] = true;

    }
    basinSizes.push(size);
    basins.push(basin)
  }
  
  return basinSizes.sort((a, b) => {
    if (a > b) return -1;
    if (a < b) return 1;
    return 0
  }).slice(0, 3).reduce((prev, cur) => prev * cur);
};

const results2 = part2(inputs);

console.log(results2);