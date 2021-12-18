import fs from 'fs';

const processInputs = (path="inputs.txt") => {
  return fs
    .readFileSync(path, "utf8")
    .split("\n")
    .map(snail => JSON.parse(snail))
    // .map(item => parseInt(item, 10));
    // .map(item => item.trim());
};

const checkExplode = (snailfish, depth=0, path=[]) => {
  if (Array.isArray(snailfish)) {
    if (depth === 4) return {snailfish, path};

    let exploded = checkExplode(snailfish[0], depth + 1, [...path, 0]);
    if (exploded) return exploded;
    
    exploded = checkExplode(snailfish[1], depth + 1, [...path, 1]);
    if (exploded) return exploded;
  }
};

const explode = (snailfish, path, explodePair) => {
  let removedSnailfish = snailfish;
  for (let i=0; i<path.length-1; i++) {
    removedSnailfish = removedSnailfish[path[i]];
  }

  if (!path.every(index => index === 0)) {    
    const subPath = [...path.slice(0, path.lastIndexOf(1) + 1)];
    subPath[subPath.length-1] = 0;

    let affectedIndex = subPath.pop();
    let affectedSnailfish = snailfish;
    for (let i=0; i<subPath.length; i++) {
      affectedSnailfish = affectedSnailfish[subPath[i]];
    }

    while (Array.isArray(affectedSnailfish[affectedIndex])) {
      affectedSnailfish = affectedSnailfish[affectedIndex];
      affectedIndex = 1;
    }
    affectedSnailfish[affectedIndex] += explodePair[0];
  }

  if (!path.every(index => index === 1)) {
    const subPath = [...path.slice(0, path.lastIndexOf(0) + 1)];
    subPath[subPath.length-1] = 1;

    let affectedIndex = subPath.pop();
    let affectedSnailfish = snailfish;
    for (let i=0; i<subPath.length; i++) {
      affectedSnailfish = affectedSnailfish[subPath[i]];
    }

    while (Array.isArray(affectedSnailfish[affectedIndex])) {
      affectedSnailfish = affectedSnailfish[affectedIndex];
      affectedIndex = 0;
    }
    affectedSnailfish[affectedIndex] += explodePair[1];
  }

  removedSnailfish[path.at(-1)] = 0;
}

const checkSplit = (snailfish, path=[]) => {
  if (Array.isArray(snailfish)) {
    let toSplit = checkSplit(snailfish[0], [...path, 0]);
    if (toSplit) return toSplit
    toSplit = checkSplit(snailfish[1], [...path, 1]);
    if (toSplit) return toSplit
  } else {
    if (snailfish > 9) return {value: snailfish, path}
  }
};

const split = (snailfish, {value, path}) => {
  const left = Math.floor(value / 2);
  const right = Math.ceil(value / 2);
  let affectedIndex = path.pop();
  let affectedSnailfish = snailfish;
  for (const index of path) {
    affectedSnailfish = affectedSnailfish[index];
  }
  affectedSnailfish[affectedIndex] = [left, right];
};

const reduce = snailfish => {

  while (true) {
    const toExplode = checkExplode(snailfish);
    if (toExplode) {
      explode(snailfish, toExplode.path, toExplode.snailfish);
      continue;
    }

    const toSplit = checkSplit(snailfish);
    if (toSplit) {
      split(snailfish, toSplit);
      continue;
    }

    break;
  }
  return snailfish;
};

const getMagnitude = snailfish => {
  let magnitude = 0;
  if (Array.isArray(snailfish[0])) {
    magnitude += 3 * getMagnitude(snailfish[0]);
  } else {
    magnitude += 3 * snailfish[0];
  }
  if (Array.isArray(snailfish[1])) {
    magnitude += 2 * getMagnitude(snailfish[1]);
  } else {
    magnitude += 2 * snailfish[1];
  }
  return magnitude;
}

const part1 = (path) => {
  const inputs = processInputs(path);
  let results = [inputs.shift()];
  while (inputs.length > 0) {
    results = [results, inputs.shift()];
    results = reduce(results);
  }
  return getMagnitude(results);
};

const part2 = (path) => {
  const inputs = processInputs(path);
  let maxMagnitude = 0;
  for (let i=0; i<inputs.length; i++) {
    for (let j=0; j<inputs.length; j++) {
      if (i !== j) {
        const thisInputA = JSON.parse(JSON.stringify(inputs[i]))
        const thisInputB = JSON.parse(JSON.stringify(inputs[j]))
        const thisReduced = reduce([thisInputA, thisInputB])
        const thisMagnitude = getMagnitude(thisReduced);
        maxMagnitude = Math.max(maxMagnitude, thisMagnitude);
      }
    }
  }
  return maxMagnitude

};

console.log(part1());
console.log(part2());

export { part1, part2 };