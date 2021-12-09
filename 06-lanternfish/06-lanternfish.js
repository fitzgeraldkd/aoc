const fs = require('fs');
const inputs = fs
  .readFileSync("inputs.txt", "utf8")
  .split(",")
  .map(item => parseInt(item, 10));
  // .map(item => item.trim());

console.log(inputs);

const part1 = (inputs) => {
  for (let i=0; i<80; i++) {
    let newFish = 0;
    inputs = inputs.map(input => {
      // console.log(input);
      if (input === 0) {
        // console.log(input);
        newFish++;
        return 6;
      } else {
        // console.log(input);
        return input - 1;
      }
    })
    // console.log(inputs);
    for (let i=0; i<newFish; i++) {
      inputs.push(8);
    }
  }
  return inputs
};

// const results1 = part1(inputs);

// console.log(results1.length);

// const part2 = (inputs) => {
//   let cycles = [0, 0, 0, 0, 0, 0, 0];
//   let pending = [0, 0, 0, 0, 0, 0, 0];
//   for (const input of inputs) {
//     cycles[input] = cycles[input] ? cycles[input] + 1 : 1;
//   }

//   for (let i=0; i<18; i++) {
//     const cycle = i % 7;
//     console.log(cycle);
//     console.log(cycles);
//     console.log(pending);
//     let newCycle = cycle - 1;
//     newCycle = newCycle < 0 ? newCycle + 7 : newCycle;
//     const temp = cycles[cycle]
//     cycles[newCycle] += pending[newCycle];
//     pending[newCycle] = temp;
//   }
//   return [...cycles, ...pending];

// };

const part2 = (inputs) => {
  let cycles = [0, 0, 0, 0, 0, 0, 0];
  let pending = [0, 0];
  for (const input of inputs) {
    cycles[input] = cycles[input] ? cycles[input] + 1 : 1;
  }

  for (let i=0; i<256; i++) {
    pending.push(cycles[0]);
    cycles.push(cycles.shift() + pending.shift())
  }
  return [...cycles, ...pending];
};

const results2 = part2(inputs);

// console.log(results2);

let total = 0
for (const value of results2) {
  total += value
}

console.log(total)