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
      console.log('TO EXPLODE:', snailfish);
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

  console.log('FINAL', JSON.stringify(snailfish))
}

const split = snailfish => {

}

const reduce = snailfish => {

  while (true) {
    const toExplode = checkExplode(snailfish);
    // console.log(toExplode);
    if (toExplode) {
      // console.log('in the if')
      explode(snailfish, toExplode.path, toExplode.snailfish);
      continue;
    }
    // const splitted = split(snailfish);
    // if (splitted) continue;
    break;
  }
  return snailfish;
};

const part1 = (path) => {
  const inputs = processInputs(path);
  // console.log(inputs);
  let snailfish = [inputs.shift(), inputs.shift()]
  // console.log(snailfish)
  snailfish = reduce(snailfish)

};

const part2 = (path) => {
  const inputs = processInputs(path);


};

// console.log(part1());
// console.log(part2());

// check explode
console.log('Result:', JSON.stringify(reduce(  [[[[[9,8],1],2],3],4]  )));
console.log('Result:', JSON.stringify(reduce(  [7,[6,[5,[4,[3,2]]]]]  )));
console.log('Result:', JSON.stringify(reduce(  [[6,[5,[4,[3,2]]]],1]  )));
console.log('Result:', JSON.stringify(reduce(  [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]  )));
console.log('Result:', JSON.stringify(reduce(  [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]  )));

export { part1, part2 };