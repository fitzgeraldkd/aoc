const fs = require('fs');
const inputs = fs
  .readFileSync("inputs.txt", "utf8")
  .split("\n")
  // .map(item => parseInt(item, 10));
  // .map(item => item.trim());

// console.log(inputs);

const OPEN = ['[', '(', '{', '<'];
const CLOSE = [']', ')', '}', '>'];
const PAIRS = {
  '[': ']',
  '{': '}',
  '(': ')',
  '<': '>'
};
const POINTS = {
  ']': 57,
  '}': 1197,
  ')': 3,
  '>': 25137
}

const part1 = (inputs) => {
  let sum = 0;
  for (const input of inputs) {
    const stack = [];
    for (let i=0; i<input.length; i++) {
      if (input[i] in PAIRS) {
        stack.push(input[i]);
      } else {
        const prev = stack.pop();
        if (input[i] !== PAIRS[prev]) {
          sum += POINTS[input[i]];
          break;
        }
      }
    }
  }
  return sum;
};

const results1 = part1(inputs);

console.log(results1);

const part2 = (inputs) => {
  const points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
  };
  let sums = [];
  for (const input of inputs) {
    let stack = [];
    for (let i=0; i<input.length; i++) {
      if (input[i] in PAIRS) {
        stack.push(input[i]);
      } else {
        const prev = stack.pop();
        if (input[i] !== PAIRS[prev]) {
          stack = [];
          break;
        }
      }
    }
    let thisSum = 0;
    while (stack.length > 0) {
      const bracket = stack.pop();
      thisSum *= 5
      thisSum += points[PAIRS[bracket]];
    }
    sums.push(thisSum);
  }
  sums = sums.filter(value => value !== 0).sort((a, b) => {
    if (a > b) return 1;
    if (a < b) return -1;
    return 0;
  });
  return sums[(sums.length - 1) / 2]
};

const results2 = part2(inputs);

console.log(results2);