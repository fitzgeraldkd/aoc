const fs = require('fs');
const inputs = fs
  .readFileSync("inputs.txt", "utf8")
  .split(",")
  // .map(item => parseInt(item, 10));
  // .map(item => item.trim());

console.log(inputs);

// const part1 = (inputs) => {
//   const crabs = [];
//   for (const input of inputs) {
//     if (crabs[input]) {
//       crabs[input]++;
//     } else {
//       crabs[input] = 1;
//     }
//   }
//   console.log(crabs);
//   let minPos;
//   let minAmount;
//   const countDiff = (crabs, pos) => {
//     let sum = 0;
//     for (let i=0; i<crabs.length; i++) {
//       if (crabs[i]) sum += crabs[i] * Math.abs(i - pos);
//     }
//     return sum;
//   }
//   for (let i=0; i<crabs.length; i++) {
//     let amount = countDiff(crabs, i);
//     if (!minAmount) {
//       minPos = i;
//       minAmount = amount;
//     }
//     if (amount < minAmount) {
//       minAmount = amount;
//       minPos = i;
//     }
//   }
//   return [minPos, minAmount];
// };

// const results1 = part1(inputs);

// console.log(results1);

const part2 = (inputs) => {
  const crabs = [];
  for (const input of inputs) {
    if (crabs[input]) {
      crabs[input]++;
    } else {
      crabs[input] = 1;
    }
  }
  console.log(crabs);
  let minPos;
  let minAmount;
  const countDiff = (crabs, pos) => {
    let sum = 0;
    for (let i=0; i<crabs.length; i++) {
      let diff = Math.abs(i - pos)
      if (crabs[i]) sum += crabs[i] * Math.abs(0.5 * diff * (diff + 1));
    }
    return sum;
  }
  for (let i=0; i<crabs.length; i++) {
    let amount = countDiff(crabs, i);
    if (!minAmount) {
      minPos = i;
      minAmount = amount;
    }
    if (amount < minAmount) {
      minAmount = amount;
      minPos = i;
    }
  }
  return [minPos, minAmount];

};

const results2 = part2(inputs);

console.log(results2);