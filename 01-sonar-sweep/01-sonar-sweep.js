import fs from 'fs';

const processInputs = (path="inputs.txt") => {
  return fs.readFileSync(path, "utf8")
  .split("\n")
  .map(value => parseInt(value));
};

const countIncreases = array => {
  return array.reduce((prev, curr, ind, arr) => (
    (ind < arr.length - 1 && curr < arr[ind+1]) ? prev + 1 : prev
  ), 0);
};

const part1 = (path) => {
  const inputs = processInputs(path);
  return countIncreases(inputs);
};

const part2 = (path) => {
  const inputs = processInputs(path);
  return countIncreases(inputs
    .map((value, ind, arr) => (
      ind < arr.length - 2 ? value + arr[ind+1] + arr[ind+2] : undefined
    ))
    .filter(value => value !== undefined));
};

export { part1, part2 };