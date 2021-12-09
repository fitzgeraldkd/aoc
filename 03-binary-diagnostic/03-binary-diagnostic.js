const fs = require('fs');
const inputs = fs
  .readFileSync("inputs.txt", "utf8")
  .split("\n")
  // .map(item => parseInt(item, 10));
  .map(item => item.trim());

const digits = [];

console.log(inputs);
inputs.forEach(item => {
  for (let i=0; i<item.length; i++) {
    if (digits[i] !== undefined) {
      if (item[i] === '1') digits[i]++
      else digits[i]--
    } else digits[i] = 1;
  }
})

const countDigits = (inputs) => {
  const digits = [];
  inputs.forEach(item => {
    for (let i=0; i<item.length; i++) {
      if (digits[i] !== undefined) {
        if (item[i] === '1') digits[i]++
        else digits[i]--
      } else digits[i] = item[i] === '1' ? 1 : -1;
    }
  })
  return digits
}

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

console.log(oxy(inputs));

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

console.log(co(inputs));