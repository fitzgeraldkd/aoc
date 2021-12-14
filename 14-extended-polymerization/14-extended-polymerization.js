import fs from 'fs';

const processInputs = (path="inputs.txt") => {
  return fs
    .readFileSync(path, "utf8")
    .split("\n\n")
    .map((value, index) => index === 1 ? value.split("\n") : value)
};

const insertion = (pairs, instructions) => {
  const changes = {};
  for (const instruction of instructions) {
    const [pair, element] = instruction.split(' -> ');
    const newPair1 = pair[0] + element;
    const newPair2 = element + pair[1];
    if (pair in pairs) {
      [
        {value: pair, add: false}, 
        {value: newPair1, add: true}, 
        {value: newPair2, add: true}
      ].forEach(check => {
        if (check.value in changes) {
          changes[check.value] += pairs[pair] * (check.add ? 1 : -1)
        } else {
          changes[check.value] = pairs[pair] * (check.add ? 1 : -1)
        }
      })
    }
  }
  for (const pair in changes) {
    if (pair in pairs) {
      pairs[pair] += changes[pair];
    } else {
      pairs[pair] = changes[pair];
    }
  }
}

const getPairs = (polymer) => {
  const pairs = {};
  for (let i=0; i<polymer.length-1; i++) {
    if (polymer.slice(i, i+2) in pairs) {
      pairs[polymer.slice(i, i+2)]++;
    } else {
      pairs[polymer.slice(i, i+2)] = 1;
    }
  }
  return pairs;
}

const countElements = (polymer, pairs) => {
  const elements = {};
  for (const pair in pairs) {
    [0, 1].forEach(index => {
      if (pair[index] in elements) {
        elements[pair[index]] += pairs[pair] / 2;
      } else {
        elements[pair[index]] = pairs[pair] / 2;
      }
    });
  }
  elements[polymer[0]] += 0.5;
  elements[polymer.at(-1)] += 0.5;
  return elements;
}

const getMaxDifference = (countedElements) => {
  return Object
    .values(countedElements)
    .reduce((prev, curr) => {
      prev.max = Math.max(curr, prev.max);
      prev.min = Math.min(curr, prev.min);
      prev.diff = prev.max - prev.min;
      return prev;
    }, {min: Infinity, max: 0, diff: Infinity})
    .diff
};

const runInsertions = (pairs, instructions, quantity) => {
  for (let i=0; i<quantity; i++) {
    insertion(pairs, instructions);
  }
}

const part1 = (path) => {
  const inputs = processInputs(path);
  let [polymer, instructions] = inputs;
  let pairs = getPairs(polymer);
  runInsertions(pairs, instructions, 10);
  return getMaxDifference(countElements(polymer, pairs));
};

const part2 = (path) => {
  const inputs = processInputs(path);
  let [polymer, instructions] = inputs;
  let pairs = getPairs(polymer);
  runInsertions(pairs, instructions, 40);
  return getMaxDifference(countElements(polymer, pairs));
};

export { part1, part2 };