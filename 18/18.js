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
  // console.log(snailfish, path)
  if (Array.isArray(snailfish)) {
    if (depth === 4) {
      // console.log('TO EXPLODE:', snailfish);
      // explode('test')
      return {snailfish, path};
    }
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
    // const subPath = [...path.slice(0, path.lastIndexOf(1) + 1)];
    // subPath[subPath.length-1] = 0;
    // let affectedSnailfish = snailfish;
    // while (subPath.length > 0) {
    //   const prevSnailfish = affectedSnailfish[subPath.shift()];
    //   if (!Array.isArray(prevSnailfish)) break;
    //   affectedSnailfish = prevSnailfish;
    // }
    // let affectedIndex = 1;
    // while (Array.isArray(affectedSnailfish) && Array.isArray(affectedSnailfish[1])) {
    //   if (affectedSnailfish[1] === removedSnailfish[path.at(-1)]) {
    //     affectedIndex = 0;
    //     break;
    //   }
    //   affectedSnailfish = affectedSnailfish[1];
    // }
    // affectedSnailfish[affectedIndex] += explodePair[0];
    // console.log(affectedSnailfish);
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


    // let affectedSnailfish = snailfish;
    // while (subPath.length > 0) {
    //   const nextSnailfish = affectedSnailfish[subPath.shift()];
    //   if (!Array.isArray(nextSnailfish)) break;
    //   affectedSnailfish = nextSnailfish;
    // }
    // console.log(affectedSnailfish)
    // let affectedIndex = 0;
    // while (Array.isArray(affectedSnailfish) && Array.isArray(affectedSnailfish[0])) {
    //   if (affectedSnailfish[0] === removedSnailfish[path.at(-1)]) {
    //     affectedIndex = 1;
    //     break;
    //   }
    //   affectedSnailfish = affectedSnailfish[0];
    // }
    // console.log(affectedSnailfish)
    affectedSnailfish[affectedIndex] += explodePair[1];
  }
  
  
  
  // let removedSnailfish = snailfish;
  // let lastIndex = path.pop();
  // // console.log(path)
  // while (path.length > 0) {
  //   removedSnailfish = removedSnailfish[path.shift()];
  // }
  removedSnailfish[path.at(-1)] = 0;
  // console.log(removedSnailfish);

  // console.log('FINAL', JSON.stringify(snailfish))
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
    // console.log(affectedSnailfish)
    affectedSnailfish = affectedSnailfish[index];
  }
  affectedSnailfish[affectedIndex] = [left, right];
  // console.log(snailfish);
};

const reduce = snailfish => {

  while (true) {
    const toExplode = checkExplode(snailfish);
    // console.log(toExplode);
    if (toExplode) {
      // console.log('in the if')
      explode(snailfish, toExplode.path, toExplode.snailfish);
      continue;
    }
    const toSplit = checkSplit(snailfish);
    if (toSplit) {
      split(snailfish, toSplit);
      // console.log('test');
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
  // console.log(inputs);
  // let snailfish = [inputs.shift(), inputs.shift()]
  // console.log(snailfish)
  // snailfish = reduce(snailfish)
  let results = [inputs.shift()];
  while (inputs.length > 0) {
    results = [results, inputs.shift()];
    results = reduce(results);
  }
  // return JSON.stringify(results);
  return getMagnitude(results);

};

const part2 = (path) => {
  const inputs = processInputs(path);
  // console.log(inputs);
  for (const input of inputs) {
    // console.log(JSON.stringify(input));
  }
  const magnitudes = inputs.map(input => getMagnitude(input));
  for (const magnitude of magnitudes) {
    // console.log(JSON.stringify(magnitude))
  }

  let maxMagnitude = 0;
  let inputA;
  let inputB;
  let reduced;
  // let indeces;
  for (let i=0; i<inputs.length; i++) {
    for (let j=0; j<inputs.length; j++) {
      if (i !== j) {
        const thisInputA = JSON.parse(JSON.stringify(inputs[i]))
        const thisInputB = JSON.parse(JSON.stringify(inputs[j]))
        const thisReduced = reduce([thisInputA, thisInputB])
        const thisMagnitude = getMagnitude(thisReduced);
        // maxMagnitude = Math.max(maxMagnitude, thisMagnitude);
        if (thisMagnitude > maxMagnitude) {
          inputA = inputs[i];
          inputB = inputs[j];
          reduced = thisReduced;
          maxMagnitude = thisMagnitude;
        }
      }
    }
  }
  // console.log(JSON.stringify(inputA));
  // console.log(JSON.stringify(inputB));
  // console.log(JSON.stringify(reduced));
  return maxMagnitude

};

// console.log(part1());
console.log(part2());

// check explode
// console.log('Result:', JSON.stringify(reduce(  [[[[[9,8],1],2],3],4]  )));
// console.log('Result:', JSON.stringify(reduce(  [7,[6,[5,[4,[3,2]]]]]  )));
// console.log('Result:', JSON.stringify(reduce(  [[6,[5,[4,[3,2]]]],1]  )));
// console.log('Result:', JSON.stringify(reduce(  [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]  )));
// console.log('Result:', JSON.stringify(reduce(  [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]  )));

// check split
// console.log('Result:', JSON.stringify(reduce([[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]])));

export { part1, part2 };