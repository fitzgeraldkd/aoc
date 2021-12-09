const fs = require('fs');
const inputs = fs
  .readFileSync("inputs.txt", "utf8")
  .split("\n")
  // .map(item => parseInt(item, 10));
  .map(item => item.trim());

console.log(inputs);

const part1 = (inputs) => {
  const coords = {};
  for (input of inputs) {
    const [start, end] = input.split(' -> ');
    const [startX, startY] = start.split(',').map(value => parseInt(value));
    const [endX, endY] = end.split(',').map(value => parseInt(value));
    if (startX === endX && startY === endY) {
      coords[`${startX},${startY}`] = coords[`${startX},${startY}`] ? coords[`${startX},${startY}`]+1 : 1;
    } else if (startX === endX) {
      const [thisStart, thisEnd] = startY < endY ? [startY, endY] : [endY, startY];
      // console.log(thisStart, thisEnd);
      for (let y = thisStart; y<=thisEnd; y++) {
        coords[`${startX},${y}`] = coords[`${startX},${y}`] ? coords[`${startX},${y}`]+1 : 1;
      }
    } else if (startY === endY) {
      const [thisStart, thisEnd] = startX < endX ? [startX, endX] : [endX, startX];
      for (let x = thisStart; x<=thisEnd; x++) {
        coords[`${x},${startY}`] = coords[`${x},${startY}`] ? coords[`${x},${startY}`]+1 : 1;
        // console.log('test');
      }
    }
    // console.log(coords);
    // return null;
  }
  // console.log(coords);
  let total = 0;
  Object.values(coords).forEach(value => {
    if (value >= 2) total++;
  })
  return coords;
};

const coords = part1(inputs);
// console.log(coords);
// console.log(Object.values(coords).length);
const part2 = (inputs, coords) => {
  // console.log(coords);
  for (input of inputs) {
    const [start, end] = input.split(' -> ');
    const [startX, startY] = start.split(',').map(value => parseInt(value));
    const [endX, endY] = end.split(',').map(value => parseInt(value));
    if ((Math.abs(startX - endX) === Math.abs(startY - endY)) && !(startX === endX || startY === endY)) {
    // if ((Math.abs(startX - endX) === Math.abs(startY - endY))) {
      // console.log(input);
      let i=0;
      // console.log(input);
      // const [thisStartX, thisEndX] = startX < endX ? [startX, endX] : [endX, startX];
      // const [thisStartY, thisEndY] = startY < endY ? [startY, endY] : [endY, startY];

      while (true) {
        const thisX = startX + (i * ((startX < endX) ? 1 : -1))
        const thisY = startY + (i * ((startY < endY) ? 1 : -1))
        // console.log(input, thisX, thisY)
        // console.log(thisX, thisY, startX, endX)
        // if (thisX === 6 && thisY === 4) console.log(input)
        coords[`${thisX},${thisY}`] = coords[`${thisX},${thisY}`] ? coords[`${thisX},${thisY}`]+1 : 1;
        // console.log(thisStartX+i, thisStartY+i);
        i++;
        if (thisX === endX) break
      }
      // return null
    } 
    // console.log(coords);
    // return null;
  }
  // console.log(coords);
  let total = 0;
  Object.values(coords).forEach(value => {
    if (value >= 2) total++;
  })
  return total;
};

console.log(part2(inputs, coords));