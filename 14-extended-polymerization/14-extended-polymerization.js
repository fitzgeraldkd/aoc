import fs from 'fs';

const processInputs = (path="inputs.txt") => {
  return fs
    .readFileSync("inputs.txt", "utf8")
    .split("\n\n")
    .map((value, index) => index === 1 ? value.split("\n") : value)
    // .map(item => parseInt(item, 10));
    // .map(item => item.trim());
};

// const insertion = (polymer, instructions) => {
//   const insertions = [];
//   for (const instruction of instructions) {
//     const [pair, element] = instruction.split(' -> ');
//     for (let i=0; i<polymer.length - 1; i++) {
//       if (polymer.slice(i, i+2) === pair) {
//         insertions.push({value: element, index: i+1});
//       }
//     }
//     // const index = polymer.indexOf(pair);
//     // if (index >= 0) {
//     //   insertions.push({value: element, index: index + 1})
//     // }
//   }
//   insertions.sort((a, b) => {
//     if (a.index > b.index) return -1;
//     if (a.index < b.index) return 1;
//     return 0;
//   });

//   for (const insertion of insertions) {
//     if (insertion.value === undefined) console.log(insertion);
//     polymer = polymer.slice(0, insertion.index) + insertion.value + polymer.slice(insertion.index)
//   }
//   return polymer
// };

const insertion = (pairs, instructions) => {
  const changes = {};
  for (const instruction of instructions) {
    const [pair, element] = instruction.split(' -> ');
    const newPair1 = pair[0] + element;
    const newPair2 = element + pair[1];
    if (pair in pairs) {
      if (pair in changes) {
        changes[pair] -= pairs[pair];
      } else {
        changes[pair] = -pairs[pair]
      }
      if (newPair1 in changes) {
        changes[newPair1] += pairs[pair];
      } else {
        changes[newPair1] = pairs[pair];
      }
      if (newPair2 in changes) {
        changes[newPair2] += pairs[pair];
      } else {
        changes[newPair2] = pairs[pair];
      }
    }
  }
  for (const pair in changes) {
    if (pair in pairs) {
      pairs[pair] += changes[pair];
    } else {
      pairs[pair] = changes[pair];
    }
  }
  return pairs;
}

// const countElements = (polymer) => {
//   const elements = {};
//   for (let i=0; i<polymer.length; i++) {
//     if (polymer[i] in elements) {
//       elements[polymer[i]]++;
//     } else {
//       elements[polymer[i]] = 1;
//     }
//   }
//   return elements;
// };

// const part1 = (path) => {
//   const inputs = processInputs(path);
//   let [polymer, instructions] = inputs;
//   console.log(polymer);
//   for (let i=0; i<10; i++) {
//     polymer = insertion(polymer, instructions)
//   }
//   const elementCount = countElements(polymer)
//   console.log(polymer);
//   console.log(polymer.length);
//   console.log(elementCount);
// };

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
    if (pair[0] in elements) {
      elements[pair[0]] += pairs[pair] / 2;
    } else {
      elements[pair[0]] = pairs[pair] / 2;
    }
    if (pair[1] in elements) {
      elements[pair[1]] += pairs[pair] / 2;
    } else {
      elements[pair[1]] = pairs[pair] / 2;
    }
  }
  elements[polymer[0]] += 0.5;
  elements[polymer.at(-1)] += 0.5;
  return elements;
}

const part1 = (path) => {
  const inputs = processInputs(path);
  let [polymer, instructions] = inputs;
  let pairs = getPairs(polymer);
  console.log(pairs);
  for (let i=0; i<40; i++) {
    pairs = insertion(pairs, instructions);
  }
  console.log(pairs);
  const elementCount = countElements(polymer, pairs);
  const elementQuantities = Object.values(elementCount).sort((a, b) => {
    if (a > b) return 1;
    if (a < b) return -1;
    return 0;
  })
  return elementQuantities.at(-1) - elementQuantities[0]
};

const part2 = (path) => {
  const inputs = processInputs(path);
  let [polymer, instructions] = inputs;
  console.log(polymer);
  for (let i=0; i<40; i++) {
    polymer = insertion(polymer, instructions)
  }
  const elementCount = countElements(polymer)
  // console.log(polymer);
  // console.log(polymer.length);
  console.log(elementCount);
};

console.log(part1());
// console.log(part2());

export { part1, part2 };