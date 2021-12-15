import fs from 'fs';

const processInputs = (path="inputs.txt") => {
  return fs
    .readFileSync(path, "utf8")
    .split("\n")
    .map(instruction => 
      instruction
        .split(' ')
        .map((value, index) => index === 1 ? parseInt(value) : value));
};

const part1 = (path) => {
  const inputs = processInputs(path);
  const position = inputs.reduce((prev, curr) => {
    prev[curr[0] === 'forward' ? 'hor' : 'ver'] += curr[1] * (curr[0] === 'up' ? -1 : 1)
    return prev
  }, {hor: 0, ver: 0})
  return position.hor * position.ver;
};

const part2 = (path) => {
  const inputs = processInputs(path);
  const position = inputs.reduce((prev, curr) => {
    if (curr[0] === 'forward') {
      prev.hor += curr[1]
      prev.ver += prev.aim * curr[1]
    } else {
      prev.aim += curr[1] * (curr[0] === 'up' ? -1 : 1)
    }
    return prev
  }, {hor: 0, ver: 0, aim: 0})
  return position.hor * position.ver;
};

export { part1, part2 };