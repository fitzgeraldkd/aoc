const fs = require('fs');
const inputs = fs
  .readFileSync("inputs.txt", "utf8")
  .split("\n").map(item => item.split('').map(number => parseInt(number)))
  // .map(item => parseInt(item, 10));
  // .map(item => item.trim());

console.log(inputs);


const increment = inputs => {
  return inputs.map(row => row.map(value => value + 1))
};

const flash = (inputs, flashCoords, x, y) => {
  flashCoords.push(`${x},${y}`);
  for (const adj of adjacent) {
    try {
      const [thisX, thisY] = [x+adj[0], y+adj[1]]
      inputs[thisY][thisX] += 1;
      if (inputs[thisY][thisX] > 9 && !flashCoords.includes(`${thisX},${thisY}`)) {
        flash(inputs, flashCoords, thisX, thisY)
      }
    } catch (error) {
      
    }
  }
  return {inputs, flashCoords}
}

const adjacent = [
  [1, 0],
  [1, 1],
  [0, 1],
  [-1, 1],
  [-1, 0],
  [-1, -1],
  [0, -1],
  [1, -1]
];




const part1 = (inputs) => {
  let flashes = 0;
  for (let step=0; step<100; step++) {
    inputs = increment(inputs);
    let flashCoords = [];
    for (let y=0; y<inputs.length; y++) {
      for (let x=0; x<inputs[y].length; x++) {
        if (inputs[y][x] > 9 && !flashCoords.includes(`${x},${y}`)) {
          const newResults = flash(inputs, flashCoords, x, y);
          inputs = newResults.inputs;
          flashCoords = newResults.flashCoords;
        }
      }
    }
    flashes += flashCoords.length;
    for (const flashCoord of flashCoords) {
      const [x, y] = flashCoord.split(',').map(value => parseInt(value));
      inputs[y][x] = 0;
    }
  }
  return flashes;
};

const results1 = part1(inputs);

console.log(results1);

const part2 = (inputs) => {
  let flashes = 0;
  for (let step=0; step<1000; step++) {
    inputs = increment(inputs);
    let flashCoords = [];
    for (let y=0; y<inputs.length; y++) {
      for (let x=0; x<inputs[y].length; x++) {
        if (inputs[y][x] > 9 && !flashCoords.includes(`${x},${y}`)) {
          const newResults = flash(inputs, flashCoords, x, y);
          inputs = newResults.inputs;
          flashCoords = newResults.flashCoords;
        }
      }
    }
    flashes += flashCoords.length;
    for (const flashCoord of flashCoords) {
      const [x, y] = flashCoord.split(',').map(value => parseInt(value));
      inputs[y][x] = 0;
    }
    if (flashCoords.length === 100) {
      return step+1;
    }
  }
  return flashes;


};

const results2 = part2(inputs);

console.log(results2);