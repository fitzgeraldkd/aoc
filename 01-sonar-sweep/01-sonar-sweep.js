// import inputs from './inputs';
const inputs = require('./inputs.js')

console.log(inputs);

let count = 0;
let prev = inputs[0];
inputs.forEach(depth => {
  if (depth > prev) {
    count++;
  }
  prev = depth;
});

console.log(count)
count = 0;
let window = [inputs[0], inputs[1], inputs[2]];
for (let i=0; i<inputs.length-2;i++) {
  const prev = window[0] + window[1] + window[2];
  console.log(prev);
  window = [window[1], window[2], inputs[i+3]];
  if (window[0] + window[1] + window[2] > prev) {
    count++;
  }
}

console.log(count)