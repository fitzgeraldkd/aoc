import fs from 'fs';

const processInputs = (path="inputs.txt") => {
  return fs
    .readFileSync("inputs.txt", "utf8")
    .split("\n")
    // .map(item => parseInt(item, 10));
    // .map(item => item.trim());
};

const part1 = (path) => {
  const inputs = processInputs(path);

};

const part2 = (path) => {
  const inputs = processInputs(path);

};

console.log(part1());
console.log(part2());

export { part1, part2 };