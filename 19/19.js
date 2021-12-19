import fs from 'fs';

const processInputs = (path="inputs.txt") => {
  return fs
    .readFileSync(path, "utf8")
    .split("\n\n")
    .map(scanner => scanner.split('\n').slice(1).map(coords => JSON.parse(`[${coords}]`)))
    // .map(item => parseInt(item, 10));
    // .map(item => item.trim());
};

const rotations = [
  [3, 1, 2],
  [3, 2, 1],
  [1, 3, 2],
  [1, 2, 3],
  [2, 3, 1],
  [2, 1, 3],

  [-3, 1, 2],
  [-3, 2, 1],
  [1, -3, 2],
  [1, 2, -3],
  [2, -3, 1],
  [2, 1, -3],
]

const getDifference = (position1, position2) => {
  return position1.map((value, index) => value - position2[index]);
};

const rotateByAxis = ((scanner, axis) => {
  const swapped = {
    0: axis === 0 ? 0 : (axis === 1 ? 2 : 1),
    1: axis === 1 ? 1 : (axis === 2 ? 0 : 2),
    2: axis === 2 ? 2 : (axis === 0 ? 1 : 0),
  }
  const inverted = {
    0: axis === 1 ? -1 : 1,
    1: axis === 2 ? -1 : 1,
    2: axis === 0 ? -1 : 1
  }
  return scanner.map(coords => (
    [
      coords[swapped[0]] * inverted[0],
      coords[swapped[1]] * inverted[1],
      coords[swapped[2]] * inverted[2]
    ]
  ));
});

const alignScanner = ((scanner, difference) => {
  return scanner.map(coords => coords.map((coord, index) => coord + difference[index]));
});

const countAligned = ((scanner1, scanner2) => {
  const scanner2strings = scanner2.map(coord2 => coord2.toString());
  return scanner1.map(coord => coord.toString()).reduce((prev, coord) => (
    scanner2strings.includes(coord) ? prev + 1 : prev
  ), 0);
});

const checkOverlap = ((scanner1, scanner2) => {

  for (let i=0; i<scanner1.length; i++) {
    for (let j=0; j<scanner2.length; j++) {
      const difference = getDifference(scanner1[i], scanner2[j]);
      const scanner2aligned = alignScanner(scanner2, difference);
      // console.log('test')
      // console.log(scanner1);
      // console.log(scanner2);
      // console.log(scanner2aligned);
      const numberAligned = countAligned(scanner1, scanner2aligned)
      if (numberAligned >= 12) return scanner2aligned;
      
    }
  }
  return false;
});

const iterateRotationsAndCheck = ((scanner1, scanner2) => {
  // [0,0,0,1,2,1,2,0,0,0,1,2,1,0,0,0,2,1,2,1,0,0,0,1,0,0,0,2,2].forEach(axis => {
  //   const aligned = checkOverlap(scanner1, scanner2);
  //   // console.log(scanner2);
  //   if (aligned) return aligned;
  //   scanner2 = rotateByAxis(scanner2, axis)
  // })
  for (let x=0; x<4; x++) {
    scanner2 = rotateByAxis(scanner2, 0);
    for (let y=0; y<4; y++) {
      scanner2 = rotateByAxis(scanner2, 1);
      for (let z=0; z<4; z++) {
        scanner2 = rotateByAxis(scanner2, 2);
        const aligned = checkOverlap(scanner1, scanner2);
        if (aligned) return aligned;
      }
    }
  }
  return false;
});

const part1 = (path) => {
  const inputs = processInputs(path);
  const scanners = [[0, 0, 0]];
  const unalignedScanners = [...inputs];
  const alignedScanners = [unalignedScanners.shift()]
  console.log(inputs[0]);
  console.log(iterateRotationsAndCheck(inputs[0], inputs[1]))
  let iterations = 0;
  while (unalignedScanners.length > 0) {
    console.log(unalignedScanners.length, 'scanners left.', iterations++, 'iterations.')
    const thisScanner = unalignedScanners.shift();
    let isAligned;
    for (const alignedScanner of alignedScanners) {
      isAligned = iterateRotationsAndCheck(alignedScanner, thisScanner);
      if (isAligned) break;
    }
    if (isAligned) {
      alignedScanners.push(isAligned);
    } else {
      unalignedScanners.push(thisScanner);
    }
  }

  const beacons = [];
  for (const scanner of alignedScanners) {
    scanner.map(beacon => beacon.toString()).forEach(beacon => {
      if (!beacons.includes(beacon)) beacons.push(beacon);
    })
  }
  return beacons.length;

};

const part2 = (path) => {
  const inputs = processInputs(path);


};

console.log(part1());
console.log(part2());

export { part1, part2 };