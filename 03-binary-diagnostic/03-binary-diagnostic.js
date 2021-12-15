import fs from 'fs';

const processInputs = (path="inputs.txt") => {
  return fs
    .readFileSync(path, "utf8")
    .split("\n")
    // .map(value => parseInt(value));
};

const countDigits = (inputs) => {
  return inputs.reduce((digits, item) => {
    for (let i=0; i<item.length; i++) {
      if (digits[i] !== undefined) {
        if (item[i] === '1') digits[i]++
        else digits[i]--
      } else digits[i] = item[i] === '1' ? 1 : -1;
    }
    return digits;
  }, []);
};

const part1 = (path) => {
  const inputs = processInputs(path);
  const digitCount = countDigits(inputs);
  const gamma = parseInt(digitCount.map(count => count > 0 ? 1 : 0).join(''), 2);
  const epsilon = parseInt(digitCount.map(count => count < 0 ? 1 : 0).join(''), 2);
  return gamma * epsilon;
};

const part2 = (path) => {
  const inputs = processInputs(path);
  
};

export { part1, part2 };

// const fs = require('fs');
// const inputs = fs
//   .readFileSync("inputs.txt", "utf8")
//   .split("\n")
//   // .map(item => parseInt(item, 10));
//   .map(item => item.trim());

// const digits = [];

// console.log(inputs);
// inputs.forEach(item => {
//   for (let i=0; i<item.length; i++) {
//     if (digits[i] !== undefined) {
//       if (item[i] === '1') digits[i]++
//       else digits[i]--
//     } else digits[i] = 1;
//   }
// })

// const countDigits = (inputs) => {
//   const digits = [];
//   inputs.forEach(item => {
//     for (let i=0; i<item.length; i++) {
//       if (digits[i] !== undefined) {
//         if (item[i] === '1') digits[i]++
//         else digits[i]--
//       } else digits[i] = item[i] === '1' ? 1 : -1;
//     }
//   })
//   return digits
// }

// console.log(digits);
// console.log(digits[1000])

const oxy = (values) => {
  for (let i=0; i<values[0].length; i++) {
    const digits = countDigits(values);
    console.log(values);
    values = values.filter(value => {
      return value[i] === (digits[i] >= 0 ? '1' : '0')
    });
    console.log(values.length, i)
    if (values.length === 1) return values[0];
  }
}

// console.log(oxy(inputs));

const co = (values) => {
  for (let i=0; i<values[0].length; i++) {
    const digits = countDigits(values);
    // console.log(values);
    values = values.filter(value => {
      return value[i] === (digits[i] < 0 ? '1' : '0')
    });
    console.log(values.length)
    if (values.length === 1) return values[0];
  }
}

// console.log(co(inputs));